import streamlit as st
from math import pi, sin, exp
from PIL import Image

def engineer(age):
    return sin(age*(pi/exp(1)*-9.81/10))

def main():
    image = Image.open('./meme.png')
    st.title('Engineering Math Magic')
    age = st.slider('Select your age', min_value=0, max_value=100)
    magic = engineer(age)
    st.metric(label="Your age", value = magic)
    st.image(image)

if __name__ == "__main__":
    main()
