import streamlit as st
from PIL import Image
from math import pi, sin, exp, radians
from PIL import Image

def engineer(age, unit):
    if unit == 'Degrees':
        return sin(radians(age*(pi/exp(1)*9.81/10)))
    else:
        return sin(age*(pi/exp(1)*-9.81/10))

st.set_page_config(page_title='Engineering Math Magic')
def main():
    image = Image.open('./meme.png')
    st.title('Engineering Math Magic')
    st.latex(r''' \text{engineer age} = \sin\left(\frac{\text{age} \cdot \pi  \cdot g}{10 \cdot e}\right) ''')
    """Please select a unit that best reflects your own circumstances."""
    unit = st.selectbox('Unit', ['Degrees', 'Radians'])
    age = st.slider('Select your age', min_value=0, max_value=100, value=21)
    magic = engineer(age, unit)
    st.metric(label="Your age in engineering", value = magic)
    st.image(image)

if __name__ == "__main__":
    main()
