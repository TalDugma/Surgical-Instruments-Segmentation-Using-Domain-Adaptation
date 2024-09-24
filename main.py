#imports
import blenderproc as bproc
from blenderproc.python.camera import CameraUtility
import bpy
import numpy as np
import argparse
import random
import os
import glob
import json
from colorsys import hsv_to_rgb
import csv

# Define a list to store the statistics of the generated images
statistics = []

def get_hdr_img_paths_from_haven(data_path: str) -> str:
    """ Returns .hdr file paths from the given directory.

    :param data_path: A path pointing to a directory containing .hdr files.
    :return: .hdr file paths
    """

    if os.path.exists(data_path):
        data_path = os.path.join(data_path, "hdris")
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"The folder: {data_path} does not contain a folder name hdfris. "
                                    f"Please use the download script.")
    else:
        raise FileNotFoundError(f"The data path does not exists: {data_path}")

    hdr_files = glob.glob(os.path.join(data_path, "*", "*.hdr"))
    # this will be ensure that the call is deterministic
    hdr_files.sort()
    return hdr_files


parser = argparse.ArgumentParser()
parser.add_argument('--nh', default='surgical_tools_models/needle_holder/NH10.obj', help="Path to the needle holder object file.")
parser.add_argument('--tw', default="surgical_tools_models/tweezers/T10.obj", help="Path to the tweezers object file.")
parser.add_argument('--camera_params', default="camera.json", help="Camera intrinsics in json format")
parser.add_argument('--output_dir', default="", help="Path to where the final files, will be saved")
parser.add_argument('--num_images', type=int, default=10, help="Number of images to generate")
parser.add_argument('--haven_path', default="/datashare/project/haven/", help="Path to the haven hdri images")
parser.add_argument('--debug', action='store_true', help="Enable debug mode")
parser.add_argument('--motion_blur', type=int, default=0.01, help="Set to 0 if do not want motion blur")
parser.add_argument('--image_dataset_folder_name', default="coco_data", help="Name of the folder where the images will be saved")

args = parser.parse_args()

bproc.init()

if args.debug:
    import debugpy
    debugpy.listen(5678)
    print("Waiting for debugger attach")
    debugpy.wait_for_client()

# load the objects into the scene (obj1, obj2 are the objects to be detected, obj3, obj4 are decoy objects)
obj1 = bproc.loader.load_obj(args.nh)[0]
obj1.set_cp("category_id", 1)
obj2 = bproc.loader.load_obj(args.tw)[0]
obj2.set_cp("category_id", 2)
obj3 = bproc.loader.load_obj("hand.obj")[0]
obj3.set_cp("category_id", 3)
obj4 = bproc.loader.load_obj("hand.obj")[0]
obj4.set_cp("category_id", 4)




#set the objects location relative to each other:

obj2.set_location(bproc.sampler.shell(
    center=obj1.get_location(),
    radius_min=1,
    radius_max=3,
    elevation_min=1,
    elevation_max=89
))

# decoy objects

obj3.set_location(bproc.sampler.shell(
    center=obj1.get_location(),
    radius_min=0.25,
    radius_max=0.5,
    elevation_min=1,
    elevation_max=89
))

obj4.set_location(bproc.sampler.shell(
    center=obj2.get_location(),
    radius_min=0.25,
    radius_max=0.5,
    elevation_min=1,
    elevation_max=89
))


# Generate random Euler angles in radians
random_euler_angles = np.random.uniform(0, 2 * np.pi, 3)
random_euler_angles2 = np.random.uniform(0, 2 * np.pi, 3)
random_euler_angles3 = np.random.uniform(0, 2 * np.pi, 3)
random_euler_angles4 = np.random.uniform(0, 2 * np.pi, 3)


# Set the object's rotation to these random angles
obj2.set_rotation_euler(random_euler_angles)
obj3.set_rotation_euler(random_euler_angles2)
obj4.set_rotation_euler(random_euler_angles3)

# random scale for the objects
scale_obj1 = np.random.uniform(0.5, 1.25)
scale_obj2 = np.random.uniform(0.5, 1.25)
scale_obj3 = np.random.uniform(0.05, 0.1)
scale_obj4 = np.random.uniform(0.05, 0.1)

obj1.set_scale([scale_obj1, scale_obj1, scale_obj1])
obj2.set_scale([scale_obj2, scale_obj2, scale_obj2])
obj3.set_scale([scale_obj3, scale_obj3, scale_obj3])
obj4.set_scale([scale_obj4, scale_obj4, scale_obj4])



# Create new light- one for each object to be detected
lights_types = ["POINT", "SPOT", "AREA"]
light1 = bproc.types.Light()
light1.set_type(random.choice(lights_types))

light2 = bproc.types.Light()
light2.set_type(random.choice(lights_types))

# Sample its location around the object
light1.set_location(bproc.sampler.shell(
    center=obj1.get_location(),
    radius_min=1,
    radius_max=5,
    elevation_min=1,
    elevation_max=89
))

light2.set_location(bproc.sampler.shell(
    center=obj2.get_location(),
    radius_min=1,
    radius_max=5,
    elevation_min=1,
    elevation_max=89
))


light1.set_energy(random.uniform(0, 1500))
light2.set_energy(random.uniform(0, 1500))

# Set camera intrinsics parameters
with open(args.camera_params, "r") as file:
    camera_params = json.load(file)

fx = camera_params["fx"]
fy = camera_params["fy"]
cx = camera_params["cx"]
cy = camera_params["cy"]
im_width = camera_params["width"]
im_height = camera_params["height"]
K = np.array([[fx, 0, cx], 
              [0, fy, cy], 
              [0, 0, 1]])
CameraUtility.set_intrinsics_from_K_matrix(K, im_width, im_height) 

# load hdris
hdr_files = get_hdr_img_paths_from_haven(args.haven_path)

# Sample camera poses
poses = 0
tries = 0
while tries < 10000 and poses < args.num_images:

    # Set a random world lighting strength
    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[1].default_value = np.random.uniform(0.1, 1.5)

    # Set a random hdri from the given haven directory as background
    random_hdr_file = random.choice(hdr_files)
    bproc.world.set_world_background_hdr_img(random_hdr_file)

    # Sample random camera location around the point between the two objects
    location = bproc.sampler.shell(
        center=(obj1.get_location()+obj2.get_location())/2,
        radius_min=10,
        radius_max=15,
        elevation_min=-90,
        elevation_max=90
    )
    # Compute rotation based lookat point which is placed randomly around the object
    lookat_point = (obj1.get_location()+obj2.get_location())/2 + np.random.uniform([-1, -1, -1], [1, 1, 1])
    rotation_matrix = bproc.camera.rotation_from_forward_vec(lookat_point - location, inplane_rot=np.random.uniform(-0.7854, 0.7854))
    # Add homog cam pose based on location an rotation
    cam2world_matrix = bproc.math.build_transformation_mat(location, rotation_matrix)

    # Only add camera pose if one object is still visible
    if obj1 in bproc.camera.visible_objects(cam2world_matrix) or obj2 in bproc.camera.visible_objects(cam2world_matrix):
    # if True:    
        bproc.camera.add_camera_pose(cam2world_matrix, frame=poses)
        # Append current settings to the statistics list
        statistics.append({
            "pose_index": poses,
            "camera_needle_holder_distance": round(np.linalg.norm(location - obj1.get_location()), 3),
            "camera_tweezers_distance": round(np.linalg.norm(location - obj2.get_location()), 3),
            "camera_location": [round(coord, 3) for coord in location.tolist()],
            "needle_holder_visible": int(obj1 in bproc.camera.visible_objects(cam2world_matrix)),
            "tweezers_visible": int(obj2 in bproc.camera.visible_objects(cam2world_matrix)),
            "needle_holder_location": [round(coord, 3) for coord in obj1.get_location().tolist()],
            "needle_holder_rotation": [round(angle, 3) for angle in obj1.get_rotation_euler().tolist()],
            "tweezers_location": [round(coord, 3) for coord in obj2.get_location().tolist()],
            "tweezers_rotation": [round(angle, 3) for angle in obj2.get_rotation_euler().tolist()],
            "camera_rotation_matrix": [[round(value, 3) for value in row] for row in rotation_matrix.tolist()],
            "lighting_strength": round(light1.get_energy(), 3),
            "hdr_file": random_hdr_file,
            "tweezer_object": args.tw,
            "needle_holder_object": args.nh,
            "motion_blur": int(args.motion_blur > 0)
        })
        poses += 1
    tries += 1
    print(tries)

# Define CSV header
csv_header = [
    "pose_index", 
    "camera_needle_holder_distance",
    "camera_tweezers_distance",
    "camera_location", 
    "needle_holder_visible",
    "tweezers_visible",
    "lighting_strength", 
    "hdr_file",
    "needle_holder_rotation", 
    "tweezers_rotation", 
    "needle_holder_location", 
    "tweezers_location",
    "camera_rotation_matrix",
    "tweezer_object",
    "needle_holder_object",
    "motion_blur"
]
# Append the statistics to an existing CSV file
with open(os.path.join(args.output_dir, 'statistics.csv'), 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=csv_header)
    # Write the header if the file is empty
    if os.stat(os.path.join(args.output_dir, 'statistics.csv')).st_size == 0:
        writer.writeheader()
    for data in statistics:
        writer.writerow(data)

bproc.renderer.set_max_amount_of_samples(100) # to speed up rendering, reduce the number of samples
# Disable transparency so the background becomes transparent
bproc.renderer.set_output_format(enable_transparency=False)
# add segmentation masks (per class and per instance)
bproc.renderer.enable_segmentation_output(map_by=["category_id", "instance", "name"])
if args.motion_blur != 0:
    bproc.renderer.enable_motion_blur(motion_blur_length=0.001)



# Render RGB images
data = bproc.renderer.render()
# Write data to coco file
bproc.writer.write_coco_annotations(os.path.join(args.output_dir, args.image_dataset_folder_name),
                        instance_segmaps=data["instance_segmaps"],
                        instance_attribute_maps=data["instance_attribute_maps"],
                        colors=data["colors"],
                        mask_encoding_format="polygon",
                        append_to_existing_output=True)

