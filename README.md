# Multimodal Sensor Fusion & Target Tracking System

An academic machine learning project designed to simulate robust, real-time object detection and tracking in low-visibility environments using synchronized camera and radar sensor data.

## Project Overview
Modern autonomous and defense systems require robust perception pipelines that do not fail when a single sensor is compromised or degraded by environmental noise (e.g., fog, darkness, or electronic interference). This project implements a multimodal sensor fusion framework combining RGB imagery with radar point clouds to maintain high-accuracy target tracking.

## System Architecture
* **Data Ingestion:** Synchronizes multi-channel RGB frames with sparse radar depth and velocity data.
* **Perception Layer:** Multimodal neural network architecture processing fused tensor inputs.
* **Tracking Layer:** Extended Kalman Filter (EKF) and tracking-by-detection algorithm for state estimation and trajectory prediction.

## Team & Responsibilities
* **[Harry Vatsios]** – *ML Architect & Perception:* Data pipeline alignment, multimodal neural network design, and model training.
* **[Arvid Almlöf]** – *State Estimation & Tracking:* Kalman filter implementation, multi-object tracking integration, and noise/robustness evaluation.

## Getting Started

### Prerequisites
* Python 3.10+
* PyTorch
* nuScenes Devkit

### Installation
```bash
git clone https://github.com
cd multimodal-sensor-fusion
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Dataset Setup
Download the [nuScenes Mini Dataset](https://nuscenes.org) and place it inside a local `data/` directory.

## License
This project is open-source and developed for academic portfolio purposes.
