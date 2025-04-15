import streamlit as st
import torch
from PIL import Image
from ultralytics import YOLO
import numpy as np
import io

# Load YOLOv8 model
MODEL_PATH = "best.pt"
model = YOLO(MODEL_PATH)

st.title("Worker Safety Detection with YOLOv8")
st.write("Upload an image and the model will detect safety equipment.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert to PIL image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Run YOLO inference
    st.write("Running detection...")
    results = model.predict(image, device="cpu")  # Change to 'cuda' if running on GPU
    
    # Draw results
    for r in results:
        img_array = np.array(r.plot())  # Get result image
        st.image(img_array, caption="Detection Results", use_column_width=True)

st.write("### Model Information")
st.write(f"Loaded Model: {MODEL_PATH}")

