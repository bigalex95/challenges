# Task A2: SfM — OpenMVG (CPU)

## Цель
Запустить Structure-from-Motion через OpenMVG на 90 изображениях. Альтернативное SfM-решение для сравнения с COLMAP.

## Входные данные
- Изображения: `dataset/Dataset/images/{wf,mf00..mf07}/` — 90 JPG
- Интринсики камер: `dataset/Dataset/cameras.json` (PINHOLE)
- **GPU**: не требуется (CPU-only)

## Что нужно сделать

### 1. Установить OpenMVG
```bash
sudo apt-get install -y libopenmvg-dev openmvg-tools
# Или собрать из исходников: https://github.com/openMVG/openMVG
```

### 2. Написать `scripts/run_sfm_openmvg.sh`
```bash
DATASET_DIR="dataset/Dataset/images"
OUTPUT_DIR="sfm_output/openmvg"

# 1) Image Listing (с известными интринсиками из cameras.json)
openMVG_main_SfMInit_ImageListing \
    -i $DATASET_DIR \
    -o $OUTPUT_DIR/matches \
    -d <sensor_database> \
    -c 1  # PINHOLE_CAMERA

# 2) Compute Features (SIFT)
openMVG_main_ComputeFeatures \
    -i $OUTPUT_DIR/matches/sfm_data.json \
    -o $OUTPUT_DIR/matches

# 3) Compute Matches
openMVG_main_ComputeMatches \
    -i $OUTPUT_DIR/matches/sfm_data.json \
    -o $OUTPUT_DIR/matches

# 4) Incremental SfM
openMVG_main_SfM \
    -s INCREMENTAL \
    -i $OUTPUT_DIR/matches/sfm_data.json \
    -m $OUTPUT_DIR/matches \
    -o $OUTPUT_DIR/reconstruction

# 5) Export to JSON (встроенный формат OpenMVG)
# sfm_data.bin → sfm_data.json
openMVG_main_ConvertSfM_DataFormat \
    -i $OUTPUT_DIR/reconstruction/sfm_data.bin \
    -o $OUTPUT_DIR/reconstruction/sfm_data.json
```

### 3. Написать парсер OpenMVG JSON → unified JSON
Добавить в `scripts/sfm_to_json.py` ветку `--format openmvg` для парсинга.
Формат тот же: `poses.json` + `points3d.json` + `stats.json`.

## Выходные данные
```
sfm_output/openmvg/
├── matches/               # Features + matches
├── reconstruction/        # SfM result
├── poses.json
├── points3d.json
└── stats.json
```

## Проверка
- Все 90 изображений зарегистрированы
- Mean reprojection error < 1.0 px
- Сравнить количество 3D-точек с COLMAP
