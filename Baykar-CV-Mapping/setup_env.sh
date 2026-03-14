#!/usr/bin/env bash
# ============================================================================
# setup_env.sh — Hybrid C++ / Python environment setup
# Target OS : Ubuntu 22.04
# Project   : Baykar CV Mapping
# ============================================================================
set -euo pipefail

PROJECT_DIR="/home/bigalex95/Projects/challenges/Baykar-CV-Mapping"

echo "============================================"
echo " Baykar CV-Mapping — Environment Setup"
echo "============================================"

# ── 1. System dependencies (C++ toolchain) ───────────────────────────────────
echo ""
echo "[1/6] Installing system packages..."
sudo apt-get update -qq
sudo apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libeigen3-dev \
    libgtest-dev \
    nlohmann-json3-dev \
    python3-venv \
    python3-pip

# Verify cmake version ≥ 3.22
CMAKE_VER=$(cmake --version | head -1 | awk '{print $3}')
REQUIRED_VER="3.22"
if [ "$(printf '%s\n' "$REQUIRED_VER" "$CMAKE_VER" | sort -V | head -1)" != "$REQUIRED_VER" ]; then
    echo "ERROR: cmake $CMAKE_VER is below the required $REQUIRED_VER"
    exit 1
fi
echo "  ✓ cmake $CMAKE_VER (≥ $REQUIRED_VER)"

# ── 2. Project directory structure ───────────────────────────────────────────
echo ""
echo "[2/6] Creating project directories..."
mkdir -p "$PROJECT_DIR"/{src,test,scripts,dataset,build}
echo "  ✓ src/ test/ scripts/ dataset/ build/"

# ── 3. Scaffold source files ────────────────────────────────────────────────
echo ""
echo "[3/6] Creating scaffold files..."

touch "$PROJECT_DIR/src/depth_densifier.hpp"
touch "$PROJECT_DIR/src/depth_densifier.cpp"
touch "$PROJECT_DIR/test/depth_densifier_test.cpp"
touch "$PROJECT_DIR/README.md"

echo "  ✓ depth_densifier.hpp / .cpp, depth_densifier_test.cpp, README.md"

# ── 4. Python virtual environment ───────────────────────────────────────────
echo ""
echo "[4/6] Creating Python virtual environment..."
python3 -m venv "$PROJECT_DIR/venv"
echo "  ✓ venv created at $PROJECT_DIR/venv"

# ── 5. Install Python dependencies ──────────────────────────────────────────
echo ""
echo "[5/6] Installing Python packages into venv..."
"$PROJECT_DIR/venv/bin/pip" install --upgrade pip
"$PROJECT_DIR/venv/bin/pip" install -r "$PROJECT_DIR/requirements.txt"
echo "  ✓ Python dependencies installed"

# ── 6. Build C++ project ────────────────────────────────────────────────────
echo ""
echo "[6/6] Configuring & building C++ project..."
cmake -S "$PROJECT_DIR" -B "$PROJECT_DIR/build" -DCMAKE_BUILD_TYPE=Release
cmake --build "$PROJECT_DIR/build" -j"$(nproc)"
echo "  ✓ C++ build complete"

# ── Done ─────────────────────────────────────────────────────────────────────
echo ""
echo "============================================"
echo " Setup complete!"
echo ""
echo " Activate Python env:  source $PROJECT_DIR/venv/bin/activate"
echo " Run C++ tests:        cd $PROJECT_DIR/build && ctest --output-on-failure"
echo "============================================"
