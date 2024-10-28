import streamlit as st

st.title("Sean's JSON Parser")
st.text("Insert JSON below, then we will do some parsing")


json = st.text_input(label='Paste JSON here')
st.write("The JSON looks like this ", json)
