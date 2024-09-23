# Surgical Instruments Segmentation Using Domain Adaptation

This repository provides the **model weights**, **code**, and **final report** for the semantic segmentation of surgical instruments. The project uses synthetic data and a domain adaptation approach inspired by Google's **Noisy Student** self-training method.

## Weights
- **Final Model Weights**: [Download from Google Drive](#) (replace with actual URL)

## Files Overview

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

### 3. `synthetic_data_generator.py`
   - **Purpose**: Generate synthetic tool data as outlined in the report.
   - **Configuration**: Controlled by `configurations.py`.
   - **Requirements**: 
     - Use a conda environment with dependencies from `requirements_synth.py`.
   - **Usage**: Run to create synthetic data for training.

## Final Report
- **Report**: Detailed explanation of the project, including methodology and results. [Link to report](#) (replace with actual URL).
