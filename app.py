import streamlit as st
import pandas as pd
from databricks import sql

import logging
logging.basicConfig(level=logging.INFO)

st.write("First Streamlit Program ...")

connection = sql.connect(server_hostname = "adb-2984943014560952.12.azuredatabricks.net",
                         http_path = "/sql/1.0/warehouses/ef612f64d5f4c0fc",
                         access_token = "dapic8ec89891f29da71966ec1dc3191af27",
                         _tls_no_verify=True
    )

st.write("Connection created")

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM samples.nyctaxi.trips limit 100")

    results = cursor.fetchall()
    column_names=[desc[0] for desc in cursor.description]
    df = pd.DataFrame(results, columns=column_names)
    st.dataframe(df)