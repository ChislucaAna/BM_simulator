# 🎥 Brownian Motion Project

## 🛠️ Requirements

- Python 3.7 to 3.12
- pip (Python package installer)

## 🚀 Getting Started

### 1. Clone the repository (if using Git)
```bash
git clone <your-repo-url>
cd <project-folder>
````

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the virtual environment

#### ▸ On Windows:

```bash
env\Scripts\activate
```

#### ▸ On macOS / Linux:

```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

To render a scene use:

```bash
manim -pql example.py MyFirstScene
```

* `-p` = preview after rendering
* `-q` = quality (`l` = low, `m` = medium, `h` = high)

Output videos will be saved in the `media/` directory.

---

## 🔚 Deactivate Environment

When finished, you can deactivate the environment:

```bash
deactivate
```