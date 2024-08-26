import streamlit as st
import pandas
from send_email import send_email


st.header("Contact Us")

csv_file = "/Users/leaveiljohnson/Documents/Python Projects/CompanySite/topics.csv"
df = pandas.read_csv(csv_file, sep=",")

dropdown_options = df['topic'].tolist()

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    selected_option = st.selectbox(
        'What topic do you want to discuss:',
        dropdown_options
    )
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{selected_option}
{raw_message}
"""
    button = st.form_submit_button("Send")
    if button:
        send_email(message)
        st.info("Your email was sent")
