import streamlit as st

st.set_page_config(page_title="🚀 Datapalooza ", page_icon = "https://chainbreaker.riskii.co/assets/img/logo/chain-white.png")

st.header("🚀 Datapalooza: The driven force behind Cover Letters Generation Project")

st.markdown("Discover [🚀 Datapalooza](https://datapalooza.co). 🚀 💡 Empowering businesses with data expertise, we unlock opportunities and drive success. Partner with Datapalooza to harness data's potential for transformative insights. 🤝💪")

st.header("💡 How business use web data to succeed")

st.markdown("""
    - Price and Product Monitoring 💰🔍
    - Know your customer (KYC) 🕵️‍♀️👤
    - Job Monitoring 🧑‍💻🔍
    - Real Estate Opportunities 🏢🔍
    - Financial Data for Investment Decisions 💼📈
    - Identification of Cybersecurity Threads 🛡️🔍
""")

st.header("🥸 Our Services")

st.markdown("""
    - Web Data Extraction 📊
    - Data Cleansing 🧹
    - Data Integration and Consolidation 🧩
    - Data Quality Assurance 🔍
    - Data Enrichment 🌟
    - Data Transformation and Standardization 🔄
    - Data Analytics and Insights 🔬
    - Data Visualization and Reporting 📈
    - Data Security and Compliance 🔐
""")

st.header("🤝 Meet Datapalooza Team")
col1, col2 = st.columns(2)
with col1: 
    st.markdown("### [:unicorn_face: Cristhian Pardo](https://www.linkedin.com/in/cristhian-pardo/)")
    st.write("Computer scientist and mathematician, passionate about AI, number theory, and using data to tackle society's challenges with new technologies.")
with col2: 
    st.markdown("### [:frog: Juan Esteban Cepeda](https://www.linkedin.com/in/juan-e-cepeda-gestion/)")
    st.write("Computer scientist and business admin with 5 years experience in ML, software engineering, and data analysis.")

st.header("🔗 Links")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### [🔵 Linkedin](https://www.linkedin.com/company/datapalooza/)")
    # st.image('images/octocat.png', width=150)
    st.write("Get to know our data services and products. Contact us today!")

with col2:
    st.markdown("### [:incoming_envelope: Email](mailto:info@datapalooza.co)")
    # st.image('images/kaggle.png', width=125)
    st.write("Do you have questions or a special inquery? Write us to **esteban.cepeda@datapalooza.co**")

st.markdown("### ➡️ Visit our Website: [🚀 Datapalooza](https://datapalooza.co)")
st.markdown("### ➡️ Visit Chain Breaker 🔗 Website: [here](https://chainbreaker.datapalooza.co/)")
