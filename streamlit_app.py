import streamlit as st
from PIL import Image
import smtplib

st.title("Welcome To Python Job Application")

image1 = Image.open("Python_Image.jpg")

new_img1 = image1.resize((500, 300))

st.image(new_img1, caption = "Thumbnail")

st.set_page_config(page_title = "Python Job Application",
                   page_icon = "📄")


#Setup
st.header("You Will Need To Answer Some Questions To See If you Are Good Enough For A Python Job"
          "📄")

st.text_input("**Enter Your First Name**")
st.text_input("**Enter Your Last Name**")
st.date_input("**Enter The Day You Want To Start**")
gmail = st.text_input("**Gmail**")
apppass = st.text_input("**Please Enter Your App-Password**")
st.selectbox("**Select The Path You Want For The Job**", ["*Leave Blank*", "Software Engineer", "Python Data structure",
                                                          "Web Development", "Project Organizer"])

st.selectbox("**Select The Currency You Want To Be Paid With**", ["(USD)", "(EUR)", "(CNY)", "(AUD)", "(CAD)", "Other..."])
st.text_input("**If Its Another Currency, Please Put The Currency (Global) You Wish To Be Paid With**")
st.number_input("Select The Salary Amount You Expect Yearly")
st.radio("Employment Desired", ["Full-Time", "Part-Time", "Seasonal"])
felony = st.radio("**Have You Ever Been Convicted Of A Felony**", ["No", "Yes"])
reason_of_felony = st.text_input("**If Yes, Please Explain Why**")

#Education Questions
st.title("Education Questions")
st.header("**High School**")
st.text_input("**City**")
st.text_input("**State**")
st.radio("**Graduated?**", ["Yes", "No"])
st.radio("Diploma?", ["Yes", "No"])

st.header("**Collage**")
st.text_input("**City?**")
st.text_input("**State?**")
st.radio("**Graduate?**", ["Yes", "No"])
st.radio("**Degree?**", ["Yes", "No"])

#Pythonic Questions
st.title("Python Questions")
st.selectbox("**What Level Of Python Would You Consider Yourself?**", ["Expert", "Master", "Intermediate"])
st.radio("**Do You Usually Organize Your Python Code?**", ["Yes", "No"])
st.selectbox("Which Version Of Python Do You Use?", ["v3.14", "v3.13", "v3.12", "v3.11", "v3.10", "v3.9", "v3.8", "Other..."])
st.radio("Do You Know The Important Stuff In Python Such As Functions, Dataclasses?", ["Yes", "No"])

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#Functions
def submit():
    if felony == "No":
        sender = "brightchineseedu@gmail.com"
        receiver = gmail
        password = "f g i v v v c m w y w t n m n b"
        subject = "Python email test"
        body = "Hello!, If You Are Reading This, This is Working Successfully!"

        #Header
        message = f"""From: Loud Code
        To:{receiver}
        Subject: {subject}\n
        {body}
        """

        try:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
            st.write("Successfully Submitted")

        except Exception:
            st.write("Something Went Wrong...")

    else:
        try:
            sender = gmail
            receiver = "brightchineseedu@gmail.com"
            password = apppass
            subject = "Python Felony Question"
            body = f"Felony Question: {reason_of_felony}"

            # Header
            message = f"""From: Loud Code
            To:{receiver}
            Subject: {subject}\n
            {body}
            """

            try:
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
                st.write("Successfully Submitted")

            except Exception:
                st.write("Something Went Wrong...")

        except Exception:
            st.write("Something Went Wrong...")

#Finishing Touches
if st.button("Submit"):
    submit()

#streamlit run app.py
