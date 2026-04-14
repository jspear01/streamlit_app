import streamlit as st
import re
import requests

# Get Formspree endpoint from st.secrets
# Format should be: https://formspree.io/f/your_form_id
FORMSPREE_ENDPOINT = st.secrets.get("FORMSPREE_ENDPOINT")

def is_valid_email(email):
    # Basic regex for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def send_message(name, sender_email, message):
    if not FORMSPREE_ENDPOINT:
        return False, "Formspree endpoint is not configured in secrets.toml."

    # Formspree configuration
    data = {
        "name": name,
        "email": sender_email,
        "message": message
    }

    try:
        response = requests.post(FORMSPREE_ENDPOINT, json=data)
        if response.status_code == 200:
            return True, None
        else:
            return False, f"Formspree error: {response.text}"
    except Exception as e:
        return False, str(e)

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Please enter your name.", icon="❗")
                st.stop()
            
            if not email:
                st.error("Please enter your email address.", icon="❗")
                st.stop()

            if not is_valid_email(email):
                st.error("Please enter a valid email address.", icon="❗")
                st.stop()
            
            if not message:
                st.error("Please enter your message.", icon="💬")
                st.stop()
            
            # Send message using Formspree
            success, error_msg = send_message(name, email, message)

            if success:
                st.success("Your message has been sent successfully!", icon="✅")
            else:
                st.error(f"Error: {error_msg}", icon="😱")
