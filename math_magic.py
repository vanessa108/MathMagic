import streamlit as st
from math import pi, sin, exp

def engineer(age):
    return sin(age*(pi/exp(1)*-9.81/10))

def main():
    st.title('Engineering Math Magic')
    age = st.slider('Select your age', min_value=0, max_value=100)
    magic = engineer(age)
    st.metric(label="Your age", value = magic)

if __name__ == "__main__":
    main()
