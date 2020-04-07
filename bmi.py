import streamlit as st
import pandas as pd
import numpy as np

st.title('BMI CALCULATOR')

from PIL import Image
img= Image.open("./bmi.jpg")
st.image(img)

st.info("What is BMI?")
st.success("Body mass index (BMI) is a value derived from the mass (weight) and height of a person. BMI provides a simple numeric measure of a person's thickness or thinness, allowing health professionals to discuss weight problems more objectively with their patients.")

if st.checkbox("Click here to know more about BMI"):
	st.text("The BMI is generally used as a means of correlation between groups related by general ")
	st.text("mass and can serve as a vague means of estimating adiposity.The duality of the BMI is ")
	st.text("that, while it is easy to use as a general calculation, it is limited as to how accurate")
	st.text("and pertinent the data obtained from it can be. Generally, the index is suitable for")
	st.text("recognizing trends within sedentary or overweight individuals because there is a smaller")
	st.text("margin of error.The BMI has been used by the WHO as the standard for recording obesity")
	st.text("statistics since the early 1980s.")

st.header("Here you can checkout your BMI and know how you can work out on it...")
name=st.text_input("Enter your name")
gender=st.radio("What is your gender",("Male","Female"))
selection=st.selectbox("Select your age group",["10-17","18-34","35-44","45-54","55-64","65-74","75-79"])
height=st.slider("Your height(in metres)",0.55,2.72)
weight=st.slider("Your weight(in kilograms)",5,120)
bmi=weight/(height*height)
if bmi==0.11:
        st.text("      ")
if st.button("Submit"):
	result=("Hi "+str(name)+" your bmi is "+ str(bmi))
	st.text(result)
	
if bmi < 14:
	st.warning("You are soo thin!!")
	if st.checkbox("Click here to know important tips to gain weight."):
		st.info("1.) Eat more calories than your body burns.")
		st.info("2.) Increase your fibre intake.")
		st.info("3.) Eat Energy-Dense Foods and Use Sauces, Spices and Condiments.")
		st.info("4.) Eat plenty of proteins.")
else:
        if bmi > 35 :
                st.warning("You are soo obese!!!")
                if st.checkbox("Click here to know your eating habits."):
                        st.info("1.) Include fruits and veggies on regular basis.")
                        st.info("2.) Eat a whole source of protein with each meal – meat, chicken, fish, eggs, etc.")
                        st.info("3.) Make weight gainer shakes by mixing oats, milk, banana, peanut butter and whey protein in your blender.")
                        st.info("4.) Do free weight, compounds like Squats and Deadlifts instead. They trigger more strength and muscle gains to gain weight.")
        else :
                st.success("You have an acceptable bmi")
                if st.checkbox("Click here to know how to maintain a good bmi."):
                        st.info("1.) Try to make physical activity a regular part of your day, just like brushing your teeth.")
                        st.info("2.) Stay hydrated and eat balanced diet.")
                        st.info("3.) Avoid random snacking.")

if bmi>35:
	if (gender=="Female"):
		img1=Image.open("./fat_woman.jpg")
		st.image(img1,width=200)
	else:	
		img2=Image.open("./fat_man.jpg")
		st.image(img2,width=200)
else :
        if bmi<16:
                if (gender=="Female"):
                        img3=Image.open("./thin_woman.jpg")
                        st.image(img3,width=200)
                else:	
                        img4=Image.open("./thin_man.jpg")
                        st.image(img4,width=200)
        else:
                if (gender=="Male"):
                        img5=Image.open("./healthy_boy.jpg")
                        st.image(img5,width=200)
                else :
                        img6=Image.open("./healthy_woman.jpg")
                        st.image(img6,width=200)
                
