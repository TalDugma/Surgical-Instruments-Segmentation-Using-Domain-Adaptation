import argparse
from ultralytics import YOLO

# Define argument parser
parser = argparse.ArgumentParser(description="Run YOLOv8 model predictions on a video.")
parser.add_argument("--video_path", type=str, required=True, help="Path to the input video")
parser.add_argument("--model_path", type=str, required=True, help="Path to the YOLO model weights file")
parser.add_argument("--confidence", type=float, default=0.5, help="Confidence threshold for predictions")

# Parse arguments
args = parser.parse_args()

# Load model
model = YOLO(args.model_path)

# Run predictions on video with given confidence level
model.predict(args.video_path, conf=args.confidence, save=True)
