""" Boilerplate Theme Stuff """

# imports
import streamlit as st
from PIL import Image
from assets.plotly_theme import px_template, MODEBAR_CONFIG

# Common Plotly Settings to run throughout app
PLOTLY_KWARGS = dict(use_container_width=True, theme=None, config=MODEBAR_CONFIG)


def streamlit_boilerplate(
        page_title: str = "APP TITLE",
        hide_decoration_bar: bool = False,):
    """ Boilerplate Streamlit Setup Code

    Streamlit seems to be great for rapid prototyping, but it's a pain in the
    backside for themes and needing repetitive boilerplate stuff.
    This function runs several things:
        - sets page config: wide layout, with chosen favicon.ico
        - changes default plotly template for all plots in an app
        - option to remove god ugly streamlit 90's red decoration bar
        - run a CSS stylesheet saved as stylesheet.css

    References:
        - https://discuss.streamlit.io/t/delete-red-bar-at-the-top-of-the-app/9658

    """

    # streamlit page config must always be the first line of code run
    st.set_page_config(
        page_title=page_title,
        page_icon=Image.open('assets/favicon.ico'),
        layout="wide",
    )

    # load bespoke plotly theme & set as default
    px_template(as_default=True)

    # CSS to remove annoying header bar in Streamlit (the shit red / orange one)
    # Also remove access to the Streamlit menu, so only set to True in deployed App
    if hide_decoration_bar:
        hide_decoration_bar_style = '''<style> header {visibility: hidden;} </style> '''
        st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    # Run CSS stylesheet for main hackery
    with open("assets/stylesheet.css") as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)
