# Task B: Monocular Depth Estimation — 5 моделей

## Цель
Запустить 5 моделей моноокулярной глубины на всех 90 изображениях, сохранить карты глубины как 32-bit TIFF.

## Входные данные
- Изображения: `dataset/Dataset/images/{wf,mf00..mf07}/` — 90 JPG
- Интринсики камер: `dataset/Dataset/cameras.json` (нужны для UniDepth и Metric3D)
- **GPU**: NVIDIA GPU с CUDA (обязательно)

## Модели

### 1. Depth Anything v2 (ViT-Large)
- **Тип**: relative depth
- **Repo**: `https://github.com/DepthAnything/Depth-Anything-V2`
- **HuggingFace**: `depth-anything/Depth-Anything-V2-Large-hf`
- **Install**: `pip install transformers torch`
- **Inference**:
```python
from transformers import pipeline
pipe = pipeline("depth-estimation", model="depth-anything/Depth-Anything-V2-Large-hf", device="cuda")
result = pipe(image)
depth = np.array(result["depth"])  # relative depth
```

### 2. Marigold
- **Тип**: relative depth (diffusion-based, affine-invariant)
- **Repo**: `https://github.com/prs-eth/Marigold`
- **HuggingFace**: `prs-eth/marigold-lcm-v1-0`
- **Install**: `pip install diffusers transformers accelerate`
- **Inference**:
```python
from diffusers import MarigoldDepthPipeline
pipe = MarigoldDepthPipeline.from_pretrained("prs-eth/marigold-lcm-v1-0", torch_dtype=torch.float16)
pipe.to("cuda")
output = pipe(image, num_inference_steps=4)  # LCM = fast
depth = output.prediction[0]  # [H, W] float
```

### 3. UniDepth
- **Тип**: metric depth (camera-aware)
- **Repo**: `https://github.com/lpiccinelli-eth/UniDepth`
- **Install**: `pip install unidepth` или клонировать repo
- **Inference**:
```python
from unidepth.models import UniDepthV2
model = UniDepthV2.from_pretrained("lpiccinelli/unidepth-v2-vitl14")
predictions = model.infer(rgb_image, intrinsics_matrix)
depth = predictions["depth"]  # [1, 1, H, W] metric
```
- **Примечание**: передавать K-матрицу из `cameras.json` (fx, fy, cx, cy)

### 4. ZoeDepth
- **Тип**: metric depth
- **Repo**: `https://github.com/isl-org/ZoeDepth`
- **HuggingFace**: `Intel/zoedepth-nk`
- **Install**: `pip install transformers torch`
- **Inference**:
```python
from transformers import pipeline
pipe = pipeline("depth-estimation", model="Intel/zoedepth-nk", device="cuda")
result = pipe(image)
depth = np.array(result["depth"])
```

### 5. Metric3D v2
- **Тип**: metric depth (canonical camera transform)
- **Repo**: `https://github.com/YvanYin/Metric3D`
- **Install**: клонировать repo + `pip install timm`
- **Inference**:
```python
import torch
model = torch.hub.load('yvanyin/metric3d', 'metric3d_vit_large', pretrain=True)
depth, confidence, output_dict = model.inference({'input': rgb_tensor})
# Нужна canonical intrinsic transform — см. README проекта
```

## Что нужно сделать

### 1. Обновить `requirements.txt`
Добавить зависимости для всех моделей:
```
torch
torchvision
transformers
diffusers
accelerate
safetensors
timm
Pillow
tifffile
```
Отдельные модели (UniDepth, Metric3D) могут потребовать `pip install` из их git repo.

### 2. Написать `scripts/run_depth_inference.py`
Единый скрипт с CLI:
```bash
python scripts/run_depth_inference.py --model depth_anything_v2
python scripts/run_depth_inference.py --model marigold
python scripts/run_depth_inference.py --model unidepth
python scripts/run_depth_inference.py --model zoedepth
python scripts/run_depth_inference.py --model metric3d
python scripts/run_depth_inference.py --model all  # все модели
```

Для каждого изображения:
1. Загрузить JPG
2. Прогнать через модель → depth map
3. Сохранить как `depth_maps/<model>/<image_stem>.tif` (float32)
4. Записать время инференса

### 3. Структура каждого model wrapper
```python
class DepthModel(ABC):
    @abstractmethod
    def load(self): ...
    @abstractmethod
    def predict(self, image: np.ndarray) -> np.ndarray: ...
    # Returns float32 depth map [H, W]

class DepthAnythingV2(DepthModel): ...
class MarigoldModel(DepthModel): ...
class UniDepthModel(DepthModel): ...
class ZoeDepthModel(DepthModel): ...
class Metric3DModel(DepthModel): ...
```

## Выходные данные
```
depth_maps/
├── depth_anything_v2/
│   ├── wf_100.tif
│   ├── wf_101.tif
│   └── ...  (90 файлов)
├── marigold/
│   └── ...
├── unidepth/
│   └── ...
├── zoedepth/
│   └── ...
└── metric3d/
    └── ...

# + лог
results/depth_inference_log.json  # {model, image, time_sec, shape}
```

## Проверка
- 90 файлов `.tif` на каждую модель (450 всего)
- Все файлы float32, без NaN/Inf
- Размер depth map совпадает с размером исходного изображения
- Время инференса записано
