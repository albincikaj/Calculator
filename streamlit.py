import streamlit as st
import json
import requests

st.title("Basic Calculator App ")

# taking user inpputs
option = st.selectbox("What operation You want to perform?",
                     ("Addition", "Substraction", "Multiplication", "Division"))

st.write("")
st.write("Select the number from the slider below ")
x = st.slider("X", 0, 100, 20)
y = st.slider("Y", 0, 130, 10)

# Converting the input to a json format
inputs = {"operation": option, "x": x, "y": y}

# When the user clicks on button it will fetch the API
if st.button('Calculate'):
    res = requests.post(url = "http://127.0.0.1:8000/calculate", data=json.dumps(inputs))

    st.subheader(f"Response from API = {res.text}")
