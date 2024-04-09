import streamlit as st

def calculate_sum(num1, num2):
    return num1 + num2

st.title('Simple Calculator')

num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

if st.button('Calculate Sum'):
    result = calculate_sum(num1, num2)
    st.write(f'The sum of {num1} and {num2} is: {result}')
