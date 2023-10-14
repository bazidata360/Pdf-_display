import streamlit as st
import base64

# Create a session state to track login status
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

# Check if the user is already logged in
if st.session_state.login_status:
    st.title("Welcome to the Secure Area")
    st.write("You are logged in!")
    def main():

    # Create a selectbox to allow the user to select a page
        page = st.sidebar.selectbox("Select a page:", ["Home", "Link", "Contact"])

    # Conditionally render content based on the selected page
        if page == "Home":
            display_home_page()
        elif page == "Link":
            display_Link_page()
        elif page == "Contact":
            display_contact_page()

    def display_home_page():
        st.header("Home Page")
        st.write("Welcome to the Home Page!")

    def display_Link_page():
        st.header("Past Link")
        st.write("This is the About Page.")

    def display_contact_page():
        st.header("Contact Page")
        st.write("You can reach us at contact@example.com.")
    
    def display_home_page():
        st.title("PDF Viewer")

    # Upload a PDF file
        pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        if pdf_file is not None:
            # Display the PDF using an iframe
            pdf_bytes = pdf_file.read()
            st.write("PDF Preview:")
            st.write(pdf_file)
            st.write(f"File size: {len(pdf_bytes)} bytes")

        # Create a URL for the PDF file
            pdf_url = get_pdf_url(pdf_bytes)

        # Embed the PDF viewer using an iframe
            pdf_display = f'<embed src="data:application/pdf;base64,{pdf_url}" width="700" height="1000" type="application/pdf">'
            st.markdown(pdf_display, unsafe_allow_html=True)

    def get_pdf_url(pdf_bytes):
    # You can use a library or service to store the PDF temporarily and get a URL.
    # For demonstration purposes, we'll use a simple approach to encode the PDF as base64.
    
        pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
        return f"data:application/pdf;base64,{pdf_base64}"


    def display_Link_page():
        st.title("Large PDF Viewer")

    # Take input as a link (URL) from the user
        user_link = st.text_input("Enter a URL", "https://www.example.com")

    # Display the entered link as a clickable link
        if user_link:
            st.markdown(f"[{user_link}]({user_link})")
    # Embed the PDF viewer using an iframe
            st.write("PDF Viewer:")
            st.write(f'<embed src="{user_link}" width="100%" height="600"></embed>', unsafe_allow_html=True)
    if __name__ == '__main__':
        main()

    # Add your functions and content for the secure area here
    # For example, you can add buttons to trigger various actions.
   
else:
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        # Check login credentials (you can replace this with your logic)
        if email == "your_email" and password == "your_password":
            st.session_state.login_status = True
        else:
            st.write("Login failed. Please try again.")

# Optionally, you can add a "Sign Up" link or other content here.
