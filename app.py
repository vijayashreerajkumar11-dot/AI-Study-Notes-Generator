import streamlit as st
from note_generator import generate_notes


st.title("📚 AI Study Notes Generator")


topic = st.text_input(
    "Enter a topic"
)


if st.button("Generate Notes"):

    if topic:

        notes = generate_notes(topic)

        st.write(notes)


        with open("history.txt", "a") as file:
            file.write(topic + "\n")

    else:
        st.warning("Enter a topic")



st.subheader("Previous Topics")


try:
    file = open("history.txt", "r")

    history = file.readlines()

    for item in history:
        st.write("📌", item)

except:
    st.write("No history available")