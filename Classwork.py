import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Smart Photo Editor", layout="wide")

st.title("Smart Photo Editor")
st.write("Завантажте своє фото та застосуйте до нього фільтри")
st.sidebar.header("Налаштування фільтрів")



uploaded_file = st.file_uploader("Оберіть зображення...", type = ["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    img_array = np.array(image)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Оригінальне фото")
        st.image(img_array, use_container_width = True)

    filter_option = st.sidebar.selectbox("Оберіть ефект:",
                                     ["Оригінал","Чорно-Білий",
                                      "Розмиття","Збільшити яскравіть",
                                      "Інверсія"])
    processed_img = img_array.copy()

    if filter_option == "Чорно-Білий":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    elif filter_option == "Розмиття":
        processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)

    elif filter_option == "Збільшити яскравіть":
        processed_img = cv2.convertScaleAbs(img_array, alpha = 1.0, beta = 50)

    elif filter_option == "Інверсія":
        processed_img = 255 - img_array

    with col2:
        st.subheader("Оброблене фото")
        st.image(processed_img, use_container_width = True)

        result_img = Image.fromarray(processed_img)

        import io
        buf = io.BytesIO()
        result_img.save(buf, format = "JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label = "Завантажити",
            data = byte_im,
            file_name = "smart_edit.jpeg",
            mime = "image/jpeg"
        )
