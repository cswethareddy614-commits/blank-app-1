import streamlit as st
st.title("BMI Calculator")

weight = st.number_input("enter your weight (kg) :", min_value=0.0, format="%2f")
height_d = st.radio("Select your height unit:", ["Centimeters", "Meters", "Feet"])
height = st.number_input(f"enter your height({height_d.lower()}):",
                         min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    try:
        if height_d == 'Centimeters':
            height_m = height / 100
        elif height_d == "Feet":
            height_m = height / 3.28
        else:
            height_m = height

        if height_m <= 0:
            st.error("height must be greater than 0")
        else:
            bmi = weight / (height_m ** 2)
            st.success(f"your BMI is{bmi:.2f}")

            if bmi < 16:
                st.error("you are extremely UnderWeight")
            elif 16 <= bmi < 18.5:
                st.warning("you are UnderWeight")
            elif 18.5 <= bmi < 25:
                st.success("You are Healthy")
            elif 25 <= bmi < 30:
                st.warning("You are OverWeight")
    except:
        st.error("please enter valid numerical values")
        
