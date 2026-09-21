# 🚗 DQN Autonomous Vehicle Navigation

> **Safety-Aware Deep Q-Network Variants for Lightweight Sensor-Based Collision Avoidance in Autonomous Vehicles**

A 2D Deep Q-Network simulation focusing on robust collision avoidance for Autonomous Vehicles (AVs). This repository serves as the official implementation for our research, utilizing a curriculum learning approach and rigorous tester-stage validation to train a safe and efficient driving agent.

## ✨ Research Overview

This project implements a lightweight, sensor-based Autonomous Vehicle navigation system. The agent learns to navigate a dynamic three-lane highway while prioritizing safety and smooth driving behavior. We focus on enhancing safety-awareness in Deep Q-Network variants for collision avoidance, ensuring that the model performs reliably even in dense and unpredictable traffic scenarios.

## 🔥 Key Features

- **🧠 Deep Q-Network Training**: Implements robust DQN with a replay buffer and target network.
- **📚 Curriculum Learning**: Progressive difficulty stages to incrementally train the autonomous agent.
- **🛡️ Safety-Aware Mechanics**: Specialized reward and penalty systems encouraging centerline adherence and high collision avoidance.
- **✅ Tester-Stage Validation**: Curated obstacle suites for rigorous evaluation before model promotion.
- **🎮 Real-Time Visualization**: Interactive PyGame-based simulation for live behavior inspection and evaluation.
- **⚙️ Centralized Configuration**: Easy parameter tuning and simulation adjustments located entirely in `config_simulation.py` (obstacles in `config_obstacle.py`).

## 🗂️ Repository Structure

- `config_simulation.py`: Centralized configuration for simulation, rewards, and environment geometry.
- `config_obstacle.py`: Obstacle seed configurations (training + tester) with a named selector.
- `main_environment.py`: Dynamics, sensor logic, and state management.
- `main_dqn_agent.py`: DQN architecture, memory buffers, and train step functions.
- `run_train.py`: Primary training loop, curriculum management, and validation logic.
- `run_loadmodel.py`: Load a trained model and run real-time PyGame simulation / model evaluation.
- `TRAINED_DATA/`: Researh related logs, models and performance results.

## 🚀 Setup & Installation

```bash
# Set up virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
*(Python 3.10+ is recommended)*

### ⚠️ Troubleshooting: Pygame Issues

If you encounter errors when running the program (e.g., `ModuleNotFoundError: No module named 'pygame'` or compatibility issues), try installing **pygame-ce** (Community Edition) instead:

```bash
# Uninstall old pygame first
pip uninstall pygame

# Install pygame-ce
pip install pygame-ce

# Or install with specific version
pip install pygame-ce>=2.5.2
```

**Alternative:** Update your `requirements.txt` to use pygame-ce:

```
# Visualization
pygame-ce>=2.5.2
```

Then reinstall:
```bash
pip install -r requirements.txt --upgrade
```

> **Note:** `pygame-ce` is a more actively maintained fork of pygame with better performance and additional features. It's fully compatible as a drop-in replacement.


## 💡 Running Tips

For detailed command-line instructions on how to run both training and evaluation processes, please refer to the `CLI_Snippets.txt` file included in the repository. This file contains:

* **Training Commands**: Complete CLI examples for starting the DQN training with various configurations
* **Evaluation Commands**: Pre-built scripts for testing trained models on different obstacle scenarios

The snippets are organized by use case, making it easy to copy-paste and run the exact command you need for your workflow.

### 🚀 Running Manually

**Training:**

```bash
python run_train.py --episodes 2500 
python run_train.py --episodes 2500 --ddqn
python run_train.py --episodes 2500 --d3qn

```

**Loading Models:**

```bash
python run_loadmodel.py --model models/modelfile.pth 
python run_loadmodel.py --model models/modelfile.pth --ddqn
python run_loadmodel.py --model models/modelfile.pth --d3qn

```

## 📦 Outputs

- 💾 Trained models, logs, and checkpoints are stored in the `models/` directory.
- 📈 Real-time evaluation outputs CSV logs into `visualize_logs/`.

## 👨‍💻 Author

Created and developed by **Richky Abednego** and co for autonomous vehicle research.

