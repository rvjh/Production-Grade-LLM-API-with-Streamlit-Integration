import streamlit as st

from AHI_Turbine_Faliure.Home_Turbine_v1 import main_turbine
from Utility_AHI.Home_Underground_Cable import main_underground_cable

# Create a SessionState class for managing session state across dropdowns
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# Initialize session state
session_state = SessionState(ticker1=None, asset_class=None)

# Set the page configuration
st.set_page_config(page_title="Utility Dashboard", page_icon="🧊", layout="wide")

# Sidebar styling
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            padding-top: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Add image and title to the sidebar
st.sidebar.image(r"https://assets.bwbx.io/images/users/iqjWHBFdfxIU/ilRo2DdUbN.k/v0/-1x-1.jpg", width=300)
st.sidebar.markdown("<h1 style='text-align: center;'>Asset Performance Management</h1>", unsafe_allow_html=True)

# Select utility segment and asset class
ticker1_options = ["Generation", "Distribution"]
session_state.ticker1 = st.sidebar.selectbox("Select Utility Segment", ticker1_options)

if session_state.ticker1 == "Generation":
    asset_class_options = ["Steam Turbine","Gas Turbine","Diesel Generation","Combined Cycle Generation"]
elif session_state.ticker1 == "Distribution":
    asset_class_options = ["Underground Cable","Poles","Network Transformer","Power Transformer","Overhead Lines"]
else:
    asset_class_options = []

session_state.asset_class = st.sidebar.selectbox("Select Asset Class", asset_class_options)

# Display main content based on selected asset class
if session_state.asset_class == "Steam Turbine":
    main_turbine()

if session_state.asset_class == "Underground Cable":
    main_underground_cable()

if session_state.asset_class == "Gas Turbine":
    st.subheader("Page under maintenance.")

if session_state.asset_class == "Diesel Generation":
    st.subheader("Page under maintenance.")

if session_state.asset_class == "Combined Cycle Generation":
    st.subheader("Page under maintenance.")

if session_state.asset_class == "Poles":
    st.subheader("Page under maintenance.")

if session_state.asset_class == "Network Transformer":
    st.subheader("Page under maintenance.")

if session_state.asset_class == "Power Transformer":
    st.subheader("Page under maintenance.")

if session_state.asset_class == "Overhead Lines":
    st.subheader("Page under maintenance.")