# challenges

Solutions to a few coding challenges, kept as a personal archive. Not a maintained project.

## What's inside

```
yandex-cup/   Yandex Cup problems A-G: Python solutions (src/), pytest tests (tests/), problem statements (data/)
polonom/      Small C/C++ interview task from Polonom Robotics (2021)
```

- `yandex-cup/` - one module per problem (`src/A_solution.py` ... `G_solution.py`), each exposing `solve()` that reads stdin. Problem E is interactive and its test is skipped. See [yandex-cup/README.md](yandex-cup/README.md).
- `polonom/` - Turkish-language notes (`README.adoc`) and two answers: `soru_1` (C++ program linking a precompiled object, built with CMake in two variants) and `soru_2` (C program that checks whether points fall inside a rectangle on a canvas). The original exam PDF belonged to the company and is not included.

## Run

```bash
cd yandex-cup && pytest -q
```

```bash
cd polonom/soru_2 && gcc find_point.c && ./a.out
```

## Status

Old solutions, not maintained. Test coverage for the Yandex problems is basic.

## Credits

Problem statements in `yandex-cup/data/` come from Yandex Cup. The Polonom task belongs to Polonom Robotics.
