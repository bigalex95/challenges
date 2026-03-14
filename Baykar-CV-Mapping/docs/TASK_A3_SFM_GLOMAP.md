# Task A3: SfM — GLOMAP (GPU)

## Цель
Запустить Structure-from-Motion через GLOMAP (Global SfM от авторов COLMAP). Быстрее COLMAP за счёт глобальной оптимизации вместо инкрементальной.

## Входные данные
- Изображения: `dataset/Dataset/images/{wf,mf00..mf07}/` — 90 JPG
- Интринсики камер: `dataset/Dataset/cameras.json` (PINHOLE)
- **GPU**: требуется NVIDIA GPU с CUDA

## Что нужно сделать

### 1. Установить GLOMAP
```bash
# GLOMAP пока нет в apt, собираем из исходников
git clone https://github.com/colmap/glomap.git /tmp/glomap
cd /tmp/glomap
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
sudo make install
```

### 2. Написать `scripts/run_sfm_glomap.sh`
GLOMAP использует COLMAP для feature extraction и matching, затем свой глобальный mapper:
```bash
DATASET_DIR="dataset/Dataset/images"
OUTPUT_DIR="sfm_output/glomap"

# 1-2) Feature extraction + matching (идентично COLMAP)
colmap feature_extractor \
    --database_path $OUTPUT_DIR/db.db \
    --image_path $DATASET_DIR \
    --ImageReader.single_camera_per_folder 1 \
    --SiftExtraction.use_gpu 1

colmap exhaustive_matcher \
    --database_path $OUTPUT_DIR/db.db \
    --SiftMatching.use_gpu 1

# 3) GLOMAP Global Mapper
glomap mapper \
    --database_path $OUTPUT_DIR/db.db \
    --image_path $DATASET_DIR \
    --output_path $OUTPUT_DIR/sparse

# 4) Export to TXT (GLOMAP выводит в формате COLMAP)
colmap model_converter \
    --input_path $OUTPUT_DIR/sparse/0 \
    --output_path $OUTPUT_DIR/sparse_txt \
    --output_type TXT
```

### 3. Парсер
Формат GLOMAP совпадает с COLMAP TXT → переиспользовать `sfm_to_json.py --format colmap`.

## Выходные данные
```
sfm_output/glomap/
├── db.db
├── sparse/0/
├── sparse_txt/
├── poses.json
├── points3d.json
└── stats.json
```

## Проверка
- Все 90 изображений зарегистрированы
- Сравнить скорость и качество с COLMAP и OpenMVG
