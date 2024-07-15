import os
import snowflake.connector

PASSWORD = os.getenv('SNOWSQL_PWD')
# WAREHOUSE = os.getenv('WAREHOUSE')

conn = snowflake.connector.connect(
    account='fkayqyl-vma04178',
    user='cneal4',
    password=PASSWORD,
    database='streamlit_demo',
    WAREHOUSE = 'STREAMLITWAREHOUSE'
)

cur = conn.cursor()
cur.execute ('select * from streamlit_demo.public.employees')
# for row in cur:
#     print(row)

df = cur. fetch_pandas_all()
print(df)