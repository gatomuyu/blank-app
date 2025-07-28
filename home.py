import streamlit as st
from PIL import Image

image2 = Image.open("Welcome.jpg")

new_img2 = image2.resize((700, 500))

st.set_page_config(page_title = "Home Page",
                   page_icon = "📄")

st.title("**Welcome**!")
st.header("""**Welcome To Loud Code :)**""")
st.write("""**This is A Web Were You Can Apply For A Pythonic Working Project, In Which you Can Customize To Your Full Liking,
         This Is A Really Great Place To Go With If You Are Very Advanced With Python, Enjoy Your Stay :)**""")

st.image(new_img2)

st.write("**To Register An Account, Please Click On This Link (http://192.168.1.134:8501/register)**")
