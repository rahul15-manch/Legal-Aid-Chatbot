# pages/legal_lawyers.py
import streamlit as st
from database_integration.database import get_lawyers_by_specialization

def show_lawyers_page():
    st.title("👨‍⚖️ Find Lawyers by Specialization")

    specialization = st.text_input("Enter Specialization (e.g. Criminal, Civil, Corporate):")

    if st.button("Search"):
        if specialization.strip():
            lawyers = get_lawyers_by_specialization(specialization)
            if lawyers:
                st.success(f"✅ Found {len(lawyers)} lawyer(s) specializing in {specialization}")
                for lawyer in lawyers:
                    st.write(f"**{lawyer[1]}** — {lawyer[2]} (Contact: {lawyer[3]})")
            else:
                st.warning("⚠️ No lawyers found for this specialization.")
        else:
            st.error("Please enter a specialization.")
