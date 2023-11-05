import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"* We suspect mildewed cherry leaves have clear marks/signs, "
        f"  typically leaf discoloration and markings, that can differentiate them"
        f"  from an uninfected leaf.\n"
        f"* An Image Montage shows that typically an infected leaf has powdery mildew on it.\n "
        f"* Average Image, Variability Image and Difference between Averages"
        f"  were used to differentiate one from the other.\n"
        f"* We believe that these types of features should be sufficient"
        f"  to differentiate a healthy leaf from an infected "
        f"  leaf.\n"
        f"* The ML model will be able to distinguish "
        f"  between a healthy cherry leaf and an infected cherry leaf "
        f"  with at least a 70% accuracy.\n"

    )

    st.success(
        f"* We believe that Cherry leaves infected with "
        f" powdery mildew have exhibit a distinct "
        f" difference in color and appearance than purely green "
        f" healthy cherry leaves, making the differences markedly apparent. \n"

        f"* An Image Montage shows the evident difference "
        f"between both kinds of leaves. Powdery mildew being white and discolored"
        f"and healthy cherry leafs exhibiting their normal green coloring.\n"

        f"* Average Image, Variability Image and Difference "
        f" confirmed ours hypothesis "
        f" showing color difference between healthy and infected leaves "
        f" however; there were no clear identifies via leaf shape.\n"

        f"* ML pipeline performance was evaluated and it differentiates "
        f" a healthy leaf and an infected leaf "
        f" with at least 97% accuracy.\n\n"
    )