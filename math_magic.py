import streamlit as st
from math import pi, sin, exp, radians

def engineer(age, unit):
    if unit == 'Degrees':
        return sin(radians(age*(pi/exp(1)*9.81/10)))
    else:
        return sin(age*(pi/exp(1)*-9.81/10))

def main():
    st.title('Engineering Math Magic')
    st.latex(r''' \text{engineer age} = \sin\left(\frac{\text{age} \cdot \pi \cdot e \cdot g}{10}\right) ''')
    unit = st.selectbox('Unit', ['Degrees', 'Radians'])
    age = st.slider('Select your age', min_value=0, max_value=100, value=21)
    magic = engineer(age, unit)
    st.metric(label="Your age", value = magic)

if __name__ == "__main__":
    main()
