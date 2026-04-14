import streamlit as st

from forms.contact import contact_form

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
st.logo("assets/jun.ico")             
st.sidebar.text("© 2026 Jun Song") 
# --- RUN NAVIGATION ---               │
pg.run()  





