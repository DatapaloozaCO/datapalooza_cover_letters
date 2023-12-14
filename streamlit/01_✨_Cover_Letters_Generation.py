import streamlit as st
import os
import utils
import validators
import constants as ct
import openai

# Streamlit App
st.set_page_config(page_title="Cover Letter Generator", page_icon = "https://cdn-icons-png.flaticon.com/512/4470/4470631.png")
st.title("Cover Letter Generator 📄✨")
st.markdown("This tool designed to streamline and simplify the process of creating compelling cover letters for job applications. This software typically prompts users to input relevant information, such as their personal details, skills, and experiences to automatically generate a well-structured and tailored cover letter. ")
# Upload PDF file
pdf_path = None
uploaded_file = st.file_uploader("Upload your Curriculum Vitae as PDF file", type=["pdf"])
if uploaded_file:
    pdf_path = os.path.join("streamlit/uploads", uploaded_file.name)
    with open(pdf_path, "wb") as file:
        file.write(uploaded_file.getvalue())
    st.success(f"File uploaded successfully! 🎉")

# Input list of URLs
company_url = st.text_input("Input the URL of the company website you want to apply (for example, the 'About' section)", value="")
if not validators.url(company_url) and company_url != "":
    st.error(f"{company_url} is not valid a URL.")

# Get job description
job_information = st.text_area("Job Description (including the job title and requirements)", "")

# Optional text input
candidate_instructions = st.text_area(
    "Specific instructions for ChatGPT (e.g, mention that..., don't emphatized on..., etc)",
    "")

# Personal data
your_name = st.text_input("Input your name")
your_city = st.text_input("Input your city")
your_country = st.text_input("Input your country")
email = st.text_input("Input your email")

# Secret input for OpenAI token

openai_token = st.text_input("Enter your OpenAI Token", type="password")
openai.api_key = openai_token

# Use st.bet a_expander for newer versions of Streamlit
with st.expander("ℹ️ How to get my Open AI Token?", expanded=False):
    st.markdown("""
        Sign Up and Log In 🚀

        1. Go to the OpenAI website and sign up for an account if you don't have one already.
        2. Log in to your OpenAI account.

        Navigate to the API Section 🗺️

        - Once logged in, navigate to the API section of the OpenAI website. This is where you can find information about using the API and obtain your API key.

        Read and Understand the Documentation 📚

        - Familiarize yourself with the documentation provided by OpenAI. This documentation will guide you on how to make requests, structure your API calls, and handle responses.

        Generate API Key 🔑

        - Look for a section in the OpenAI dashboard that allows you to generate API keys. This might be under your account settings or a specific API section.

        Copy the API Key 📋

        - Once you've generated the API key, copy it. This key is crucial for authenticating your requests to the OpenAI API.
        """
    )


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
            job_information=job_information, 
            candidate_name=your_name
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

        # Delete cover letter from local system.
        os.remove(ct.RESULTS_PATH)

# Feedback section
#st.title("Feedback 💬")
#feedback = st.text_area("Share your feedback or suggestions", "")

#if feedback:
#    st.success("Thank you for your feedback! 😊")

# Note: Run the app using the following command in the terminal
# streamlit run cover_letter_generator.py
