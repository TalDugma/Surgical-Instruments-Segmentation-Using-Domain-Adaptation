import argparse
from ultralytics import YOLO

# Define argument parser
parser = argparse.ArgumentParser(description="Run YOLOv8 model predictions on an image.")
parser.add_argument("--image_path", type=str, required=True, help="Path to the input image")
parser.add_argument("--model_path", type=str, required=True, help="Path to the YOLO model weights file")
parser.add_argument("--confidence", type=float, default=0.5, help="Confidence threshold for predictions")

# Parse arguments
args = parser.parse_args()

# Load model
model = YOLO(args.model_path)

# Run predictions on image with given confidence level
model.predict(args.image_path, conf=args.confidence, save=True)
