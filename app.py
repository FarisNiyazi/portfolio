import streamlit as st
from multiapp import MultiApp
from apps import home, about_me, work # import your app modules here

app = MultiApp()

st.markdown("""
# Faris's Portfolio
""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("About me", about_me.app)
app.add_app("My Work", work.app)


# The main app
app.run()