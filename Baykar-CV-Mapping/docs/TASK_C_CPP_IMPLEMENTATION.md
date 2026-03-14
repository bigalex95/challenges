# Task C + D: C++ Implementation + Tests (later)

## Цель
Реализовать polynomial OLS densification pipeline на C++17 + написать GoogleTest тесты. **Выполняется ПОСЛЕ выбора лучших инструментов в Tasks A и B.**

## Зависимости от других задач
- Выбранный SfM → `sfm_output/<best>/poses.json` + `points3d.json`
- Выбранная модель глубины → `depth_maps/<best>/*.tif`

## Что нужно реализовать

### `src/depth_densifier.hpp` + `src/depth_densifier.cpp`

1. **PolynomialTransformer** — строит мономиальную матрицу фичей Ψ для degree k
   - `transform(d_tilde, u_norm, v_norm) → VectorXd` — одна строка фичей
   - `fit_transform(anchors) → MatrixXd` — полная design matrix N×M
   - M = C(3+k, k): degree 1→4, degree 2→10, degree 3→20
   - Порядок: graded lexicographic по (p,q,r), p+q+r ≤ k

2. **DepthDensifier** — OLS-фит из якорей + применение к full depth map
   - `fit(anchors) → bool` — решает β̂ = (ΨᵀΨ)⁻¹Ψᵀy через ColPivHouseholderQR
   - `densify(relative_depth, W, H, cx, cy) → MatrixXd` — метрическая карта глубины

3. **ResidualAnalyzer** — MAE, RMSE, max_error, quality check

### `test/depth_densifier_test.cpp`

11 обязательных тестов (см. PDF таблицу) + дополнительные.

## Отложено до завершения Tasks A + B
Не начинать эту задачу, пока не выбраны лучшие инструменты SfM и Depth.
