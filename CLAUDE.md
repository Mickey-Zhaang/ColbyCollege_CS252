# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Linting

```bash
pylint <file.py>
```

Pylint is configured via `.pylintrc`: runs 8 parallel jobs, `line-too-long` is disabled.

## Running Tests (Project1)

```bash
# Run a single test
python Project1/test01.py

# Run all tests
for f in Project1/test*.py; do python "$f"; done
```

## Repository Structure

This is a **CS 251/252 Data Analysis and Visualization** course repository. Work is organized into:

- `Labs/` — Weekly lab notebooks and scripts (Lab01, Lab02a/b/c, Lab03, lab1b)
- `Project1/` — Data I/O framework: `data.py` (core `Data` class), `analysis.py`, 6 test files
- `Project2/` — Regression analysis: `linear_regression.py`, `data.py` (extended), notebooks for linear/polynomial regression and QR solving
- `Projct3/` — K-means clustering: `kmeans.py`, image segmentation notebook

## Architecture

### Data class (`data.py`)

The `Data` class is the foundation used across projects. It reads CSV files and stores:
- Numeric columns as a 2D NumPy array
- Categorical columns separately
- Column headers and types

Project2's `data.py` extends Project1's with additional features needed for regression (e.g., adding a bias column, selecting subsets).

### Analysis/Regression (`analysis.py`, `linear_regression.py`)

`analysis.py` operates on `Data` objects to compute statistics. `linear_regression.py` implements regression using the normal equation and/or QR decomposition — the QR solver is explored separately in `qr_solver.ipynb`.

### K-Means (`kmeans.py`)

Standalone implementation of k-means clustering, used in both `kmeans.ipynb` and `image_segmentation.ipynb`.
