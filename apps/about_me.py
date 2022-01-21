import base64

import streamlit as st
from PIL import Image

def app():
    #st.title('About me')
    #st.write("Know More about me.")
    col1, col2 = st.columns(2)

    original = Image.open('ME.jpeg')
    #col1.header("This is me")
    resizedImg = original.resize((220, 220), Image.ANTIALIAS)
    col1.image(resizedImg, use_column_width=True)


    col2.header(":book: Summary\n "
                "\nReliable and hardworking Management Information systems graduate."
                "\n  Skilled in recording, interpreting, and analyzing data. "
                "\n Offering accurate problem-solving and innovative solution synthesis."
                "\n Seeking to advance into my career, while adhering to high-level of quality and productivity.")

    if st.checkbox("Show CV"):
        def show_pdf(file_path):
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

        st.write(show_pdf("MyCV.pdf"))


    if st.checkbox("Show Grade"):
        def show_pdf(file_path):
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

        st.write(show_pdf("Bachelor MIS.pdf"))

    if st.checkbox("Show Certificate"):
        def show_pdf(file_path):
            with open(file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

        st.write(show_pdf("MISK DAPI Certificate of Completion EN.pdf"))






