import numpy as np
import matplotlib.pyplot as plt
import snowflake.connector
import pandas as pd
import streamlit as st

st.title("Patient Performance trajectory")

ctx = snowflake.connector.connect(
          user="hannah",
          password="Hannah-312",
          account="dsidune-gob16463",
          warehouse="COMPUTE_WH",
          database="RISKGRAPHTRAINING",
          schema="DBT_WORKING")
cur = ctx.cursor()

#sql = "select * from SUBJECTS"
sql = "select * from subjects where ab is not null or toxicity is not null"
cur.execute(sql)
df = cur.fetch_pandas_all()
cur.close()
ctx.close()
