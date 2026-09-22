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
<<<<<<< HEAD
                                      "Розмиття","Налаштування яскравості", "Налаштування контрасту",
                                      "Інверсія", "Горизонтальне відзеркалення", "Вертикальне відзеркалення"])
=======
                                      "Розмиття","Збільшити яскравіть",
                                      "Інверсія"])
>>>>>>> c5fc64a9de0153e443bf6076d5d5baa94cc3cc56
    processed_img = img_array.copy()

    if filter_option == "Чорно-Білий":
        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    elif filter_option == "Розмиття":
        processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)

<<<<<<< HEAD
    elif filter_option == "Налаштування яскравості":
         brightness_val = st.sidebar.slider("Рівень яскравості", -100, 100, 0)
         processed_img = cv2.convertScaleAbs(img_array, alpha = 1.0, beta = brightness_val)

    elif filter_option == "Налаштування контрасту":
             contrast_val = st.sidebar.slider("Рівень контрасту", 0.5, 3.0, 1.0, step=0.1)
             processed_img = cv2.convertScaleAbs(img_array, alpha = contrast_val, beta = 0)
=======
    elif filter_option == "Збільшити яскравіть":
        processed_img = cv2.convertScaleAbs(img_array, alpha = 1.0, beta = 50)
>>>>>>> c5fc64a9de0153e443bf6076d5d5baa94cc3cc56

    elif filter_option == "Інверсія":
        processed_img = 255 - img_array

<<<<<<< HEAD
    elif filter_option == "Горизонтальне відзеркалення":
        processed_img = cv2.flip(img_array, 1)

    elif filter_option == "Вертикальне відзеркалення":
            processed_img = cv2.flip(img_array, 0)

=======
>>>>>>> c5fc64a9de0153e443bf6076d5d5baa94cc3cc56
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
