import streamlit as st
import os
import utils
import validators
import constants as ct
import openai

# Streamlit App
st.title("Cover Letter Generator 📄✨")

# Upload PDF file
pdf_path = None
uploaded_file = st.file_uploader("Upload your CV as PDF file", type=["pdf"])
if uploaded_file:
    pdf_path = os.path.join("streamlit/uploads", uploaded_file.name)
    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.getvalue())
    st.success(f"File uploaded successfully! 🎉")

# Input list of URLs
company_url = st.text_input("Input the URL of the company you want to apply", value="")
if not validators.url(company_url) and company_url != "":
    st.error(f"{company_url} is not valid a URL.")

# Get job description
job_information = st.text_area("Job Description", "")

# Optional text input
candidate_instructions = st.text_area(
    "Specific instruction for ChatGPT (e.g, say this..., avoid this..., etc)",
    "")

# Personal data
your_name = st.text_input("Input your name")
your_city = st.text_input("Input your city")
your_country = st.text_input("Input your country")
email = st.text_input("Input your email")

# Secret input for OpenAI token
openai_token = st.text_input("Enter your OpenAI Token", type="password")
openai.api_key = openai_token

# Execute button
if st.button("Execute"):
    if not uploaded_file:
        st.warning("Please upload a PDF file first.")
    if not validators.url(company_url):
        st.warning("Please enter a valid URL.")
    else:
        # Get curriculum vitalie
        curriculum_vitalie = utils.pdf_to_text(pdf_path)

        # Generate cover letter text
        cover_letter_text = utils.generate_cover_letter_text(
            company_url=company_url,
            curriculum_vitalie=curriculum_vitalie,
            candidate_instructions=candidate_instructions,
            job_information=job_information
        )

        # Save cover letter text to temporary file
        utils.generate_cover_letter_doc(
            your_name=your_name,
            your_city=your_city,
            your_country=your_country,
            your_email=email,
            cover_letter_text=cover_letter_text,
            file_path=ct.RESULTS_PATH)

        # Download button
        st.success("Cover letter generated successfully! 🚀")

        # Download button
        file_content = utils.download_file(ct.RESULTS_PATH)
        st.download_button(
            label="Click to download",
            data=file_content,
            file_name="cover_letters.docx",
            key="download_button")

# Feedback section
#st.title("Feedback 💬")
#feedback = st.text_area("Share your feedback or suggestions", "")

#if feedback:
#    st.success("Thank you for your feedback! 😊")

# Note: Run the app using the following command in the terminal
# streamlit run cover_letter_generator.py
