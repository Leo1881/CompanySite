import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("Design Works")
content = """Our company is a dynamic blend of graphic design, Python programming, and web development expertise. 
We excel in creating visually stunning designs, building responsive and user-friendly websites, and developing 
efficient Python solutions. With a commitment to quality and innovation, we deliver tailored solutions that meet 
client needs and exceed expectations."""
st.write(content)
st.subheader("Our Team")

df = pandas.read_csv("data.csv", sep=",")

col1, col2, col3, col4 = st.columns(4)

with col1:
    for index, row in df[:3].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"], width=250)

with col2:
    for index, row in df[3:6].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"], width=250)

with col3:
    for index, row in df[6:9].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"], width=250)

with col4:
    for index, row in df[9:12].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.write(row["role"])
        st.image("images/" + row["image"], width=250)



