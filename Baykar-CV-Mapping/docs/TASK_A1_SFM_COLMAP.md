# Task A1: SfM — COLMAP (GPU)

## Цель
Запустить Structure-from-Motion через COLMAP на 90 изображениях (9 камер × 10 снимков). Получить позы камер и разреженное облако 3D-точек.

## Входные данные
- Изображения: `dataset/Dataset/images/{wf,mf00..mf07}/` — 90 JPG
- Интринсики камер: `dataset/Dataset/cameras.json` (PINHOLE модель)
- **GPU**: требуется NVIDIA GPU с CUDA

## Что нужно сделать

### 1. Установить COLMAP
```bash
sudo apt-get install -y colmap
# Проверить GPU-поддержку:
colmap -h | grep -i cuda
```

### 2. Написать `scripts/run_sfm_colmap.sh`
Скрипт должен выполнить:
```bash
DATASET_DIR="dataset/Dataset/images"
OUTPUT_DIR="sfm_output/colmap"

# 1) Feature Extraction (GPU SIFT)
colmap feature_extractor \
    --database_path $OUTPUT_DIR/db.db \
    --image_path $DATASET_DIR \
    --ImageReader.single_camera_per_folder 1 \
    --ImageReader.camera_model PINHOLE \
    --SiftExtraction.use_gpu 1

# 2) Exhaustive Matching (90 изображений — exhaustive OK)
colmap exhaustive_matcher \
    --database_path $OUTPUT_DIR/db.db \
    --SiftMatching.use_gpu 1

# 3) Mapper (Incremental SfM + Bundle Adjustment)
colmap mapper \
    --database_path $OUTPUT_DIR/db.db \
    --image_path $DATASET_DIR \
    --output_path $OUTPUT_DIR/sparse

# 4) Export to TXT
colmap model_converter \
    --input_path $OUTPUT_DIR/sparse/0 \
    --output_path $OUTPUT_DIR/sparse_txt \
    --output_type TXT
```

### 3. Написать `scripts/sfm_to_json.py` — парсер COLMAP TXT → JSON
Парсит `images.txt`, `points3D.txt`, `cameras.txt` → два JSON:
- `sfm_output/colmap/poses.json` — массив `{image_name, R[3×3], t[3], K{fx,fy,cx,cy}, width, height}`
- `sfm_output/colmap/points3d.json` — массив `{id, xyz[3], rgb[3], error, track[{image_id, point2d_idx}]}`

## Выходные данные
```
sfm_output/colmap/
├── db.db                  # COLMAP database
├── sparse/0/              # Binary reconstruction
├── sparse_txt/            # TXT export (images.txt, points3D.txt, cameras.txt)
├── poses.json             # Parsed poses
├── points3d.json          # Parsed sparse points
└── stats.json             # {num_images, num_points, mean_reproj_error, runtime_sec}
```

## Проверка успешности
- Все 90 изображений зарегистрированы (проверить `images.txt`)
- Mean reprojection error < 1.0 px
- Количество 3D-точек > 1000
- `stats.json` содержит время выполнения

## Формат камерной конвенции
x-right, y-down, z-forward. Depth = z-component в camera frame.
