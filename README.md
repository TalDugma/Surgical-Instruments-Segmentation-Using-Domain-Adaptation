# Surgical-Instruments-Segmentation-Using-Domain-Adaptation
This repository contains model weights, final report, and code for semantic segmentation of surgical instruments using synthetic data and a domain adaptation method inspired by Google's "Noisy Student" self-training method. 

weights:
  - final model weights drive URL

files: 
  - predict.py: Runs model predictions on an image (given an image path). Assuming the model is saved in the same parent folder as predict.py. Requires using a conda environment that contains requirements_yolo.py.
  - video.py: Runs model predictions on a video (given a video path). Assuming the model is saved in the same parent folder as predict.py. Requires using a conda environment that contains requirements_yolo.py.
  - synthetic_data_generator.py: Generates synthetic data of tools as described in report.pdf. Configured using configurations.py. Requires using a conda environment that contains requirements_synth.py.
