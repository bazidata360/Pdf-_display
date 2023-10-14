import streamlit as st
import base64

# Create a session state to track login status
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

# Check if the user is already logged in
if st.session_state.login_status:
    st.title("Welcome to the Secure Area")
    def main():

    # Create a selectbox to allow the user to select a page
        page = st.sidebar.selectbox("Select a page:", ["NYSE_HSBC_2021", "LSE_BARC_2022", "NYSE_RBS_2020"])

    # Conditionally render content based on the selected page
        if page == "NYSE_HSBC_2021":
            display_NYSE_HSBC_2021()
        elif page == "LSE_BARC_2022":
            display_LSE_BARC_2022()
        elif page == "NYSE_RBS_2020":
            display_NYSE_RBS_2020()

    def display_NYSE_HSBC_2021():
        st.header("NYSE_HSBC_2021")
        st.write("Welcome to the Home Page!")

    def display_LSE_BARC_2022():
        st.header("LSE_BARC_2022")
        st.write("This is the About Page.")

    def display_NYSE_RBS_2020():
        st.header("NYSE_RBS_2020")
        st.write(".")
    
    def display_NYSE_HSBC_2021():
        st.title("NYSE_HSBC_2021")
        user_link = "https://www.annualreports.com/HostedData/AnnualReportArchive/h/NYSE_HSBC_2021.pdf"  # Replace with the URL of your PDF
        if user_link:
            st.markdown(f"[{user_link}]({user_link})")
    # Embed the PDF viewer using an iframe
            st.write("PDF Viewer:")
            st.write(f'<embed src="{user_link}" width="100%" height="600"></embed>', unsafe_allow_html=True)
            
    def display_LSE_BARC_2022():
        st.title("LSE_BARC_2022")
        user_link = "https://www.annualreports.com/HostedData/AnnualReports/PDF/LSE_BARC_2022.pdf"  # Replace with the URL of your PDF

        if user_link:
            st.markdown(f"[{user_link}]({user_link})")
    # Embed the PDF viewer using an iframe
            st.write("PDF Viewer:")
            st.write(f'<embed src="{user_link}" width="100%" height="600"></embed>', unsafe_allow_html=True)

    def display_NYSE_RBS_2020():
        st.title("NYSE_RBS_2020")
        user_link = "https://www.annualreports.com/HostedData/AnnualReportArchive/r/NYSE_RBS_2020.pdf"  # Replace with the URL of your PDF

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


