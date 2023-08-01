import streamlit as st
import pandas as pd

# Snowflake connection stuff
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL
import snowflake.connector as connector


@st.experimental_singleton
def snowflake_connect():
    """ Connection to Snowflake via Snowflake-Connector-Python"""
    return connector.connect(**st.secrets.snowflake_ms_lab_temp_check, client_session_keep_alive=True)


@st.experimental_singleton
def snowflake_sql_engine():
    """ Connection via the SQL Alchemy Engine Method """
    return create_engine(URL(**st.secrets.snowflake_ms_lab_temp_check))
