import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal infection sometimes experienced by cherry"
        f"trees. It is transmitted via airborne spoars"
        f"Controlling powdery mildew often involves a combination of cultural" 
        f"practices, such as pruning to improve air circulation, and fungicide" 
        f"applications. Selecting cherry varieties with resistance to powdery"
        f"mildew can also help prevent infection.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/ericjonesdev/milestone-project-cherry-leaves-mildew-detection.git).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"infected and uninfected cherry leaves visually.\n"
        f"* 2 - The client is interested in telling whether a given leaf"
        f" contains mildew or not. "
        )