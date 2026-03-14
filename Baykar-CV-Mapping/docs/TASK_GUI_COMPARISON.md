# Task: Streamlit GUI — Сравнение результатов

## Цель
Streamlit-приложение для визуального и количественного сравнения результатов SfM (Task A) и моноокулярной глубины (Task B).

## Зависимости от других задач
- **Task A** (любой из A1/A2/A3): нужны `sfm_output/<tool>/poses.json` и `points3d.json`
- **Task B**: нужны `depth_maps/<model>/*.tif`

> Если результаты ещё не готовы, GUI должен показать placeholder/заглушку.

## Что нужно сделать

### 1. Установить Streamlit
```bash
pip install streamlit streamlit-image-comparison
```

### 2. Написать `scripts/depth_viewer_gui.py`

#### Tab 1: Depth Maps Comparison
- **Sidebar**:
  - Dropdown: выбор изображения (из 90)
  - Multi-select: выбор моделей для отображения (1..5)
  - Colourmap: viridis / inferno / turbo / magma / plasma
  - Checkbox: нормализовать глубины к одному диапазону
- **Main area**:
  - Ряд 1: оригинальное изображение
  - Ряд 2: N колонок — depth map каждой выбранной модели (цветовая карта)
  - Ряд 3: гистограмма распределения глубины для каждой модели

#### Tab 2: SfM Comparison
- **Sidebar**:
  - Checkboxes: COLMAP / OpenMVG / GLOMAP (показать какие доступны)
- **Main area**:
  - Таблица: num registered images | num 3D points | mean reprojection error | runtime
  - 3D scatter plot (plotly) облака точек из каждого инструмента
  - Overlay: проекция SfM-точек на выбранное изображение

#### Tab 3: Head-to-Head
- Slider для side-by-side сравнения двух depth map (модель A vs модель B)
- Разница (diff map) между двумя моделями

#### Tab 4: Stats Table
- Сводная таблица по всем моделям × всем изображениям:
  - min / max / mean / std глубины
  - inference time
- Скачать как CSV

### 3. Написать `scripts/compare_results.py`
CLI-скрипт для генерации статичных сравнений (чтобы не нужен был Streamlit):
```bash
python scripts/compare_results.py
# Генерирует:
#   results/sfm_comparison.csv
#   results/depth_comparison.csv
#   results/depth_comparison_wf_100.png  (пример side-by-side)
```

## Запуск
```bash
source venv/bin/activate
streamlit run scripts/depth_viewer_gui.py --server.port 8501
# Открыть http://localhost:8501
```

## Выходные данные
```
scripts/depth_viewer_gui.py    # Streamlit app
scripts/compare_results.py     # CLI comparison generator
results/
├── sfm_comparison.csv
├── depth_comparison.csv
└── *.png                      # Static comparison images
```
