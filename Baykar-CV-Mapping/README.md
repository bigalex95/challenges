# Baykar CV Mapping

This project implements a hybrid C++ and Python pipeline for Computer Vision Mapping tasks, encompassing depth densification and evaluation.

## Prerequisites
- **OS**: Ubuntu 22.04 LTS (recommended)
- **Git**: Installed system-wide
- An active internet connection for installing system dependencies and pip packages.

## Getting Started

Follow these steps to clone the repository and set up the complete environment. 

### 1. Clone the Repository
If this project is still in a separate branch (`baykar-cv`), you can clone it and check out the correct branch:

```bash
# Clone the repository (replace <repository_url> with the actual URL)
git clone <repository_url>

# Navigate into the cloned directory
cd challenges

# Switch to the correct branch
git checkout baykar-cv

# Go into the project directory
cd Baykar-CV-Mapping
```

*(Note: If the project has already been merged to `main`, you can just clone and `cd Baykar-CV-Mapping` directly on the `main` branch).*

### 2. Environment Setup

The repository comes with an automated `setup_env.sh` script that handles installing all system-level dependencies (CMake, Eigen3, GTest, Nlohmann JSON) as well as creating a Python virtual environment with libraries from `requirements.txt`. Finally, it builds the C++ project automatically.

Make the script executable and run it:
```bash
chmod +x setup_env.sh
./setup_env.sh
```

**What this script does:**
1. Installs C++ tools: `build-essential`, `cmake`, `libeigen3-dev`, `libgtest-dev`, `nlohmann-json3-dev`.
2. Creates source, test, script, and build directories.
3. Sets up a local Python virtual environment at `./venv`.
4. Installs the Python packages listed in `requirements.txt`.
5. Finally, uses CMake to build the C++ project in the `build/` directory.

### 3. Usage & Running

After the `setup_env.sh` script finishes successfully, the C++ binaries and Python virtual environment are ready.

**Activating the Python Environment:**
If you want to run Python scripts later, always activate the virtual environment first:
```bash
source venv/bin/activate
```

**Running the C++ Tests:**
To verify the core C++ behavior and tests, you can use `ctest`:
```bash
cd build
ctest --output-on-failure
```

*For more details on specific sub-tasks, refer to the individual Markdown docs inside the `docs/` folder.*
