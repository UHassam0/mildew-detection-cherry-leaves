import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal problem that affects cherry trees and "
        f"the cherries they produce.\n"
        f"* The leaves need to be carefully inspected and can take an employee around 30 minutes.\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains +4 thousand images taken from "
        f"the client's crop fields ")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/UHassam0/mildew-detection-cherry-leaves/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a healthy cherry leaf from one with powdery mildew. \n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
    )
