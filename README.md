# 🦺 Worker Safety Detection with YOLOv8

A Streamlit web app that uses YOLOv8 to detect if workers are wearing safety equipment like helmets and vests from uploaded images.

*ACCURACY OF THE DATASET*: ~75%
---

## 🚀 Features

- Upload images and detect PPE
- YOLOv8 powered detection
- Simple UI with Streamlit
- Runs on CPU or GPU

---

## 🧠 Tech Stack

- Python
- Streamlit
- YOLOv8 (Ultralytics)
- PyTorch
- Pillow
- NumPy

---

## 🛠️ How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Its-me-darsanms/Workers-Safety-Detection.git
cd Workers-Safety-Detection

python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

Install every required library from requirements.txt(Ensure your venv is active).

streamlit run app.py

Workers-Safety-Detection/
│
├── app.py               # Main Streamlit app
├── best.pt              # YOLOv8 trained model
├── requirements.txt     # Dependencies
└── README.md            # Project info

