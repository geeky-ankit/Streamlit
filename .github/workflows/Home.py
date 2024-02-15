import streamlit as st
import pandas as pd
from databricks import sql


connection = sql.connect(server_hostname = "adb-2984943014560952.12.azuredatabricks.net",
                    http_path = "/sql/1.0/warehouses/ef612f64d5f4c0fc",
                    access_token = "dapiea4d9dd052d445530b0efc13b24f6dbf")

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM select * from samples.nyctaxi.trips limit 100")

    results = cursor.fetchall()
    column_names=[desc[0] for desc in cursor.description]
    df = pd.DataFrame(results, columns=column_names)
    st.dataframe(df)
