# Surgical Instruments Segmentation Using Domain Adaptation

This repository provides the **model weights**, **code**, and **final report** for the semantic segmentation of surgical instruments. The project uses synthetic data and a domain adaptation approach inspired by Google's **Noisy Student** self-training method.

## Weights
- **Final Model Weights**: [Download from Google Drive](#) (replace with actual URL)

## Files Overview
## Run Model Predictions:

### 1. `predict.py`
   - **Purpose**: Run model predictions on a single image.
   - **Requirements**: 
     - Place model weights in the same folder as `predict.py`.
     - Use a conda environment with dependencies from `requirements_yolo.py`.
   - **Usage**: Provide the image path to make predictions.

### 2. `video.py`
   - **Purpose**: Run model predictions on a video.
   - **Requirements**: 
     - Place model weights in the same folder as `video.py`.
     - Use a conda environment with dependencies from `requirements_yolo.py`.
   - **Usage**: Provide the video path to make predictions.

## Generate Synthetic Data

### 3. `synthetic_data_generator.py`
   - **Purpose**: Generate synthetic tool data as the report outlines.
   - **Configuration**: Controlled by `configurations.py`.
   - **Requirements**: 
     - Use a conda environment with dependencies from `requirements_synth.py`.
     - Place in the same folder as BlenderProc. (I used BlenderProc git clone)
   - **Usage**: Run to create synthetic data for training.
### 4. 'main.py', 'configuration.py':
   - **Purpose**: Files used by `synthetic_data_generator.py`, place in the same folder. 

## Final Report
- **Report**: Detailed explanation of the project, including methodology and results. [Link to report](#) (replace with actual URL).
