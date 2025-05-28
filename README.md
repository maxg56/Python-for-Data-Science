# Python-for-data-science

Welcome to this educational Python project for learning data science. It consists of a series of progressive exercises across multiple modules — from basic Python syntax to image processing, data tables, object-oriented programming (OOP), and data-oriented design (DoD) concepts.

## 📁 Project Structure

```bash
Python-for-data-science/
├── 0-Starting/        # Python basics
├── 1-Array/           # Working with arrays (Numpy, PIL)
├── 2-DataTable/       # Working with data (Pandas, CSV)
├── 3-POO/             # Object-Oriented Programming
├── 4- Dod/            # Data-Oriented Design
````

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone <REPO_URL>
cd python-for-data-science
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Exercises

Each exercise folder contains Python scripts, usually with a `tester.py` to try out the solution.

Example:

```bash
cd 0-Starting/ex01/
python3 format_ft_time.py
```

---

## 📦 Python Package

A small Python package is built in `0-Starting/ex09/base-ft_package`. You can build and install it as follows:

```bash
cd 0-Starting/ex09/base-ft_package
pip install build
python3 -m build
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

---

## 📚 Module Overview

* **0-Starting/**: Basic Python features (types, formatting, input/output, Morse, progress bars…)
* **1-Array/**: Numpy arrays and image processing using PIL.
* **2-DataTable/**: Data analysis with Pandas and visualization with Matplotlib.
* **3-POO/**: Class inheritance, method overriding, operator overloading.
* **4- Dod/**: Functional programming and data-oriented architecture using decorators and dataclasses.

---

## ✅ Requirements

* Python ≥ 3.10
* Dependencies listed in `requirements.txt`
* Basic command-line experience



