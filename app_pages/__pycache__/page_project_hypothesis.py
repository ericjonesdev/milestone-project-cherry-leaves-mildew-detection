import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildewed cherry leaves have clear marks/signs, "
        f"typically leaf discoloration and markings, that can differentiate them"
        f"from an uninfected leaf. \n\n"
        f"* An Image Montage shows that typically an infected leaf has powdery mildew on it. "
        f"Average Image, Variability Image and Difference between Averages"
        f"were used to differentiate one from the other."

    )