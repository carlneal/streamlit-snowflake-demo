use schema streamlit_demo.public;

create or replace stage streamlit_stage;

put file://C:\Users\Work\Documents\phData\streamlit\streamlit-snowflake-demo\first-streamlit-app\app.py @streamlit_stage
    overwrite=true auto_compress=false;

create or replace streamlit first_streamlit_app
    root_location = '@streamlit_demo.public.streamlit_stage'
    main_file = '/app.py'
    query_warehouse = 'STREAMLITWAREHOUSE';
show streamlits;