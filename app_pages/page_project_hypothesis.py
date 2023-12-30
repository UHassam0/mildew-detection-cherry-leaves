import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect leaves with mildew have clear marks/signs, "
        f" that can differentiate them from a healthy leaf. \n\n"
        f"* An Image Montage shows that typically an affected leafe has white marks. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
