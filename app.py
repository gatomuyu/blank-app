import streamlit as st

#---Page Setup---
st.sidebar.text("Please Select A Tab")

home_page = st.Page(
    page = "home.py",
    title = "Home Page",
    default = True)


register_page = st.Page(
    page = "register.py",
    title = "Register")

about_page = st.Page(
    page = "about.py",
    title = "Learn More"
)

settings_page = st.Page(
    page = "/settings.py",
    title = "Settings"
)

#---Navigation Pages---
pg = st.navigation(pages = [home_page, register_page, about_page, settings_page])

#---Run Navigation---
pg.run()


#Running Setup
print()
print("You can now view your Streamlit app in your browser.")
print()
print(f"Local Url: http://localhost:8501/")
print(f"Network Url: http://192.168.1.134:8501/")
print()

#streamlit run app.py
