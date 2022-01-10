import base64

import streamlit as st
from PIL import Image

def app():
    st.header("Here is littel taste of what I can do")
    st.write("I am trying to build up my skills and knowledge to improve my experience in Data Science and Data Analysis. Besides,\n"
              "I developed a strong proficiency in Microsoft Excel, Python, Power Bi, and My SQL.")

    with st.expander("Have a look at my Power BI and Excel"):
        st.write("""
            As you can see this pdf file contains the dashboard that I have built.\n 
            In Power Bi and Excel Sheet, I have done it after cleaning the data using Excel Sheet.
        """)
        if st.checkbox("Show"):
            def show_pdf(file_path):
                with open(file_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
                    st.markdown(pdf_display, unsafe_allow_html=True)
            st.write(show_pdf("powe bi_excel_merged.pdf"))

    with st.expander("A bout My SQL"):
        st.write("""
            Still can't figure out how I could show you my skills but you can always ask.:smile:
        """)

    with st.expander("A bout My Python"):
        st.write("""
            I have build this wep app by using Py Charm. Also, I am able to use jupyter notebook which is my favorites to build up my analysis.\n
             this is my example.
        """)


