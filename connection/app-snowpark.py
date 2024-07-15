import os
from snowflake.snowpark import Session


pars = {
    "account": 'fkayqyl-vma04178',
    "user": 'cneal4',
    "password": os.environ['SNOWSQL_PWD'],
    "database": 'STREAMLIT_DEMO',
    "schema": 'PUBLIC'
}

session = Session.builder.configs(pars).create()

df = session.sql('select * from employees')
rows = df.collect()
# for row in rows:
#     print(row)

dfp = df.to_pandas()
print(dfp)