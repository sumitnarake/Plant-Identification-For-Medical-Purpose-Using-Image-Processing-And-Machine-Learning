import streamlit as st
import cv2
import os
from PIL import Image
import detect as dt
st.title('PLANT LEAF DETECTION FOR MEDICAL PURPOSE')
st.sidebar.subheader("Mini Project-1")

def load_image(image_file):
	img = Image.open(image_file)
	return img

source = ("from file", "camera")
source_index = st.sidebar.selectbox("select Images", range(len(source)), format_func=lambda x: source[x])

if source_index==0:
    st.sidebar.subheader("Image")
    image_file = st.sidebar.file_uploader("Upload Images", type=["png","jpg","jpeg"])


if source_index==1:
    image_file = st.camera_input("Take a picture")

if image_file is not None:
    st.subheader("Original Image")
    st.image(load_image(image_file),width=400)
    target="data\\images\\"
    ext=['.jpeg','.png','.jpg','.svg','.gif']
    for file in os.listdir(target): 
        if file.endswith(tuple(ext)):
            os.remove(target + file)
    with open(os.path.join("data\images",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    try:
        c=dt.main()
        if c==0:
            st.subheader("Detected Images is aloe vera")
        if c==1:
            st.subheader("Detected Images is basil")
        if c==2:
            st.subheader("Detected Images is papaya")
        a=Image.open("runs\detect\sumit.jpg")
        st.image(a,width=400)
        if c==2:
            st.write("Click here for Medical uses")
            ok=st.button("papaya")
            if ok:
                filename = "papaya.txt"
                with open(filename,encoding='utf8') as input:
                    st.text(input.read())
        if c==1:
            st.write("Click here for Medical uses")
            ok=st.button("basil")
            if ok:
                filename = "basil.txt"
                with open(filename,encoding='utf8') as input:
                    st.text(input.read())
        if c==0:
            st.write("Click here for Medical uses")
            ok=st.button("aloe vera")
            if ok:
                filename = "aloe vera.txt"
                with open(filename,encoding='utf8') as input:
                    st.text(input.read())

    except Exception as e:
        st.title("OOPs somethings went wrong !!!\ncan not detect please try again")
       