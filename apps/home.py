import streamlit as st

def app():


    st.title(":office: Home")
    st.write("Hello, I hope that you're having a great day.\n"
             "My Name is Faris Niyazi and I have built this web page for you to know more about me and what I can do."
             "I consider Myself a Data Analyst freelancer and I am ready to work on a projects.\n"
             "Also, I am ready to be a full-Time employee as a Data analytics ")



    st.header(":mailbox: Get In Touch With Me!")

    contact_form = """
    <form action="https://formsubmit.co/fares.h.niyazi@hotmail.COM" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")