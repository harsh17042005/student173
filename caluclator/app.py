import streamlit as st

# Title
st.title("🏋️ BMI Calculator")

# Your Name
st.markdown("### 👨‍💻 Developed by: **Harsha**")

st.write("Enter your details below to calculate your BMI.")

# Input
weight = st.number_input("Enter Weight (kg)", min_value=1.0, value=50.0)
height = st.number_input("Enter Height (m)", min_value=0.5, value=1.60)

# Button
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)

    st.subheader(f"Your BMI: {bmi:.2f}")

    if bmi < 18.5:
        st.info("🟡 Category: Underweight")
    elif bmi < 25:
        st.success("🟢 Category: Normal")
    elif bmi < 30:
        st.warning("🟠 Category: Overweight")
    else:
        st.error("🔴 Category: Obese")

st.markdown("---")
st.caption("BMI Calculator using Streamlit | Developed by  Harsha")