import streamlit as st

# Get proxy configuration
HOST = "brd.superproxy.io:22225" #st.secrets.proxy_configuration.HOST
USERNAME = "brd-customer-hl_93b5fa1a-zone-data_center" #st.secrets.proxy_configuration.USERNAME
PASSWORD = "ask3gh8zga95" #st.secrets.proxy_configuration.PASSWORD
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; rv:84.0) Gecko/20100101 Firefox/84.0"  #st.secrets.proxy_configuration.USER_AGENT
PROXY = f'http://{USERNAME}:{PASSWORD}@{PASSWORD}'
PROXIES = {"http": HOST}
REQUEST_TIMEOUT = 10
RESULTS_PATH = "./streamlit/uploads/cover_letter.docx"

delimiter = "###"
system_message = f"""
    You will be provided with the information of a curriculum
    vitalie of a candidate, the information of the company 
    where the candidate wants to apply for a job and a text of
    instructions of the candidate and the information of the job the 
    candidate wants to apply for. Your task is to generate a
    cover letter for this candidate and company, explaining why 
    the candidate wants to work in this company and what tools he
    or she brings to the table. Also mention how the candidate experience
    can specifically be useful for the job he/she is applying for.
    The cover letter must use a formal
    language but don't use fancy words. \
    The user curriculum vitalie, information of the company and \ 
    the instruction of the candidate will be delimited with \
    {delimiter} characters \
    Output a cover letter"""