# Surgical Instruments Segmentation Using Domain Adaptation

This repository provides the **model weights**, **code**, and **final report** for the semantic segmentation of surgical instruments. The project uses synthetic data and a domain adaptation approach inspired by Google's **Noisy Student** self-training method.

## Repository Usage:
First, clone and go to the repository:
```bash
git clone repo
cd repo
```
Then, you can try out the synthetic data generator, and model predictions over images or videos.

## Generate Synthetic Data
To create a Conda environment and install dependencies for synthetic data generation, run the following:

```bash 
conda create --name synth python=3.8 pip
conda activate synth
pip install -r requirements_synth.txt
```
Then, go to the `Synthetic` folder, and git clone BlenderProc:
```bash
cd Synthetic
git clone https://github.com/DLR-RM/BlenderProc
cd BlenderProc
pip install -e
cd ..
```
(You can also use pip to install it, on my VM it didn't work)
Now, you are ready to run the synthetic data generator. You can change the configurations. 
``bash
python synthetic_data_generator.y

### 1. `synthetic_data_generator.py`
   - **Purpose**: Generate synthetic tool data as the report outlines.
   - **Configuration**: Controlled by `configurations.py`.
   - **Requirements**: 
     - Use a conda environment with dependencies from `requirements_synth.py`.
     - Place in the same folder as BlenderProc. (I used BlenderProc git clone)
   - **Usage**: Run to create synthetic data for training.
### 2. 'main.py', 'configuration.py':
   - **Purpose**: Files used by `synthetic_data_generator.py`, place in the same folder. 


## Run Model Predictions:
To create a Conda environment and install dependencies for model predictions, run the following:

```bash 
conda create --name visualize python=3.8 pip
conda activate visualize
pip install -r requirements_yolo.txt
```

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

## Weights
- **Final Model Weights**: [Download from Google Drive](#) (replace with actual URL)
