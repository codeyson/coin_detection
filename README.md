# 🪙 YOLOv8 Coin Denomination Detection

A computer vision project that uses **YOLOv8** to detect and classify coin denominations in real time using a webcam.

---

## 🚀 Getting Started

### 1️⃣ Train the Model

1. Open `main.ipynb`
2. Run all cells to train the model.
3. After training completes, locate the generated weights file:

`runs/detect/train/weights/best.pt`

4. Copy `best.pt` into the root directory of the project (same folder as `test.py`).

---

### 2️⃣ Run Real-Time Detection

Make sure `best.pt` is in the same directory as `test.py`, then run:

`python test.py`


The script will:
- Load the trained model (`best.pt`)
- Open your webcam
- Detect and classify coin denominations in real time

---

## 📦 Installation

Install the required dependencies:
`pip install ultralytics opencv-python`