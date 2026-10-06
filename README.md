# Multimodal Target Tracking and State Estimation for Counter-UAV Air Defense Systems

An academic machine learning and state estimation project designed to simulate robust, real-time aerial threat detection and 3D trajectory tracking through sensor fusion of a passive electro-optical (EO) camera and an active 3D radar.

## Project Overview
Modern air defense and counter-UAV (Unmanned Aerial Vehicle) systems operate in highly contested environments where individual sensors can be degraded by weather, counter-measures, or electronic jamming. This project implements a multimodal perception and tracking pipeline that fuses 2D camera detections with noisy 3D radar telemetry to estimate and predict the flight paths of incoming aerial targets.

## System Architecture
* **Perception Layer (Camera):** A YOLOv8 convolutional neural network trained on over 7,000 aerial images to detect and classify drones under variable lighting conditions.
* **Simulation Layer (Radar):** A synthetic 3D radar telemetry generator that simulates realistic target trajectories with injected Gaussian measurement noise and sensor dropouts.
* **Fusion & Tracking Layer:** A centralized Extended Kalman Filter (EKF) that handles data association and multi-sensor fusion to perform continuous state estimation and multi-frame trajectory prediction.

## Team & Responsibilities
* **HarryVat (ML Architect & Perception):** Responsible for data pipeline ingestion, training the object detection model, and extracting pixel-coordinate bounding boxes.
* **[Partner's Name] (State Estimation & Tracking):** Responsible for developing the 3D target simulator, writing the Kalman filtering algorithms, and handling multi-sensor data fusion.

## Getting Started

### Prerequisites
* Python 3.10+
* PyTorch & Ultralytics YOLO
* NumPy, SciPy & OpenCV

### Installation
```bash
git clone https://github.com
cd multimodal-sensor-fusion
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Dataset Setup
The vision pipeline utilizes a customized Roboflow dataset comprising ~7,000 annotated drone instances. The dataset structure is formatted as follows:
```text
multimodal-sensor-fusion/
├── drone-detection-2/
│   ├── train/
│   ├── valid/
│   ├── test/
│   └── data.yaml
```

## Future Extensions (SAAB Robustness Testing)
* Evaluation of tracking accuracy under simulated camera noise (e.g., fog/smoke).
* Robustness benchmarks against simulated radar jamming (electronic counter-measures).

## License
This project is open-source and developed for academic portfolio purposes.

