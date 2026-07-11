import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Student Information System",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Information System")

# Developer Name
st.markdown("### 👨‍💻 Developed by: **Harsha**")

st.write("Fill in the student details below.")

# Inputs
name = st.text_input("Student Name")
roll = st.text_input("Roll Number")
marks = st.number_input("Marks", min_value=0, max_value=100)

# Button
if st.button("Submit"):

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    st.success("Student Details Submitted Successfully!")

    st.subheader("📋 Student Details")
    st.write("**Student Name:**", name)
    st.write("**Roll Number:**", roll)
    st.write("**Marks:**", marks)
    st.write("**Grade:**", grade)

# Footer
st.markdown("---")
st.caption("Student Information System | Developed by Harsha")