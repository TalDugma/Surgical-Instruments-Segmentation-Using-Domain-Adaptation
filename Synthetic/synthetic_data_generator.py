from configurations import DATA_GENERATOR as DG
import os
import subprocess
import random
from tqdm import tqdm

def get_random_object(tweezers_objects_folder_path, needle_holder_objects_folder_path):
    """
    Function to get random articulation from the tweezers and needle holder object folders 
    """
    tweezers_objects = os.listdir(tweezers_objects_folder_path)
    needle_holder_objects = os.listdir(needle_holder_objects_folder_path)
    tweezers_object = random.choice(tweezers_objects)
    needle_holder_object = random.choice(needle_holder_objects)
    
    while needle_holder_object.endswith(".mtl") or tweezers_object.endswith(".mtl"):
        # if chose a .mtl file instead of .obj, choose another object
        if needle_holder_object.endswith(".mtl"):
            needle_holder_object = random.choice(needle_holder_objects)
        if tweezers_object.endswith(".mtl"):
            tweezers_object = random.choice(tweezers_objects)
    
    tweezers_object = os.path.join(tweezers_objects_folder_path, tweezers_object)
    needle_holder_object = os.path.join(needle_holder_objects_folder_path, needle_holder_object)
    return tweezers_object, needle_holder_object

# Path to the other Python file you want to run
script_path = "main.py"

# print configuration
print(DG)

for i in tqdm(range(DG["num_scenes"])):
    tweezers_objects_folder_path = DG["tweezers_object_folder_path"]
    needle_holder_objects_folder_path = DG["needle_holder_object_folder_path"]

    # Choose random objects from each type
    tweezers_object, needle_holder_object = get_random_object(tweezers_objects_folder_path, needle_holder_objects_folder_path)
    
    # Sample if motion blur is needed
    motion_blur = random.random() < float(DG["motion_blur_ratio"])
    
    # Set up arguments based on motion blur
    args = [
    "--nh", os.path.abspath(needle_holder_object), 
    "--tw", os.path.abspath(tweezers_object),
    "--num_images", f"{DG['num_images_per_scene']}",
    "--image_dataset_folder_name", f"{DG['image_dataset_folder_name']}"  # Updated key
    "--haven_path", f"{DG['haven_path']}"
]
    
    if not motion_blur:
        args += ["--motion_blur", "0"]
    
    # Combine script path and arguments into a single list
    command = ["blenderproc", "run", script_path] + args

    try:
        # Run the script
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}\n")
        print(e.stderr)
