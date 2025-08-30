# streamlit_app.py
import streamlit as st
from streamlit_option_menu import option_menu

# Add pages folder to path
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "pages"))

# Import modules
import home
import legal_chatbot
import legal_affidavit
import legal_rti
import legal_dispute   

# Page config
st.set_page_config(page_title="Legal Aid Advisor", layout="wide", initial_sidebar_state="auto")

# ---------- Top Navigation ----------
selected = option_menu(
    menu_title=None,  # no title
    options=["Home", "Chatbot", "Affidavit Generator", "RTI & Customer Dispute"],
    icons=["house", "robot", "file-text", "file-earmark-text"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# ---------- Display pages ----------
if selected == "Home":
    home.show_home()
elif selected == "Chatbot":
    legal_chatbot.show_chatbot()
elif selected == "Affidavit Generator":
    legal_affidavit.show_affidavit_page()
elif selected == "RTI & Customer Dispute":
    tab = st.radio("Choose Document Type:", ["RTI Application", "Customer Dispute"])
    if tab == "RTI Application":
        legal_rti.show_rti_page()
    else:
        legal_dispute.show_dispute_page()

