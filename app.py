import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

CLASSES = ["airplane","automobile","bird","cat","deer",
           "dog","frog","horse","ship","truck"]

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("cnn_cifar10_optimized.keras")

model = load_model()
st.title("Klasifikasi Gambar CIFAR-10")

file = st.file_uploader("Upload gambar", type=["jpg","jpeg","png"])
if file:
    img = Image.open(file).convert("RGB")
    st.image(img, caption="Gambar diunggah", use_container_width=True)

    x = np.array(img.resize((32, 32)), dtype="float32")  # 0-255, tanpa /255
    probs = model.predict(x[np.newaxis, ...])[0]

    top3 = np.argsort(probs)[::-1][:3]
    st.subheader(f"Prediksi: {CLASSES[top3[0]]}")
    for i in top3:
        st.write(f"{CLASSES[i]}: {probs[i]*100:.2f}%")
        st.progress(float(probs[i]))