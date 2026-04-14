import streamlit as st

from forms.contact import contact_form

import os

# Get the directory the current script is in
current_dir = os.path.dirname(__file__)
logo_path = os.path.join(current_dir, "assets", "jun.ico")


# --- PAGE SETUP ---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/dash_boards.py",
    title="Dashboards",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chat_bot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# --- SHARED ON ALL PAGES ---          
st.logo("assets/Jun2.png")
#st.logo(logo_path)
#st.logo("https://github.com/jspear01/streamlit_app/blob/main/assets/Jun.ico")
st.sidebar.text("© 2026 Jun Song") 
# --- RUN NAVIGATION ---               │
pg.run()  





