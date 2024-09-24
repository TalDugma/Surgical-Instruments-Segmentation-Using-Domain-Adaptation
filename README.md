# Surgical Instruments Segmentation Using Domain Adaptation

This repository provides the **model weights**, **code**, and **final report** for the semantic segmentation of surgical instruments. The project uses synthetic data and a domain adaptation approach inspired by Google's **Noisy Student** self-training method, to provide YOLO semantic segmentation for tools in the operating room.

## Repository Usage:
First, clone and go to the repository:
```bash
git clone https://github.com/TalDugma/Surgical-Instruments-Segmentation-Using-Domain-Adaptation
cd Surgical-Instruments-Segmentation-Using-Domain-Adaptation
```
Then, you can try out the synthetic data generator, and model predictions over images or videos.

## Generate Synthetic Data
To create a Conda environment and install dependencies for synthetic data generation, run the following:

```bash 
conda create --name synth python=3.10 pip
conda activate synth
pip install -r requirements_synth.txt
```
Then, go to the `Synthetic` folder, and git clone BlenderProc:
```bash
cd Synthetic
```
(You can also use pip to install it, on my VM it didn't work)
Now, you are ready to run the synthetic data generator. You can change the configurations. 


### 1. `synthetic_data_generator.py`
   - **Purpose**: Generate synthetic tool data as the report outlines.
   - **Configuration**: Controlled by `configurations.py`.
   - **Requirements**: 
     - Use a conda environment with dependencies from `requirements_synth.py`.
     - Place in the same folder as BlenderProc. (I used BlenderProc git clone)
     - HDRI files folder (not added in git repo, change in `configurations.py`)
     - Surgical tools .obj files are only examples in the git repo (not all articulations).
   - **Usage**: Run to create synthetic data for training.
```bash
python synthetic_data_generator.py
```

## Run Model Predictions:
To create a Conda environment and install dependencies for model predictions, run the following:

```bash 
conda create --name visualize python=3.8 pip
conda activate visualize
pip install -r requirements_yolo.txt
cd Model_Predict
```
Now, you are ready to run model predictions. 

### 1. `predict.py`
   - **Purpose**: Run model predictions on a single image.
   - **Requirements**: 
     - Use a conda environment with dependencies from `requirements_yolo.py`.
   - **Usage**: Provide the image and model paths to make predictions.
```bash
python predict.py --image_path [/path/to/image.png] --model_path [/path/to/weights.pt] --confidence [conf (float)]
```

### 2. `video.py`
   - **Purpose**: Run model predictions on a video.
   - **Requirements**: 
     - Use a conda environment with dependencies from `requirements_yolo.py`.
   - **Usage**: Provide the video and model paths to make predictions.
```bash
python video.py --video_path [/path/to/video.mp4] --model_path [/path/to/weights.pt] --confidence [conf (float)]
```

## Weights
- **Final Model Weights**: [Download from Google Drive](#) (replace with actual URL)
