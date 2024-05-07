import streamlit as st
import re
import google.generativeai as palm
from sec_api import ExtractorApi  # Import SEC Extractor API
import matplotlib.pyplot as plt
import config

# Function to clean text
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

# Function to split text into smaller chunks
def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Function to summarize text chunks
def summarize_text_chunks(text_chunks, model):
    summaries = []
    for i, chunk in enumerate(text_chunks):
        prompt = "I collected some SEC filing data and want to summarize it. " \
                 "Please summarize and output 10 BULLET POINTS ONLY. Do not use the words 'bullet points' " \
                 "in your answer. Make sure the output is WELL FORMATTED and EASY TO UNDERSTAND. Otherwise, a child will die. The relevant information is below:\n" + chunk
        print("Generating summary for Chunk", i + 1)
        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0,
            max_output_tokens=300,
        )
        summary = completion.result
        summaries.append(summary)  # Append the summary to the list of summaries
    return summaries


# Initialize SEC Extractor API
extractorApi = ExtractorApi("9458b344ac5df97a8178aeb1751e759b5ce49528e35de2b365f7c813ce4dc23c")
palm.configure(api_key=config.API_KEY)
# Streamlit UI
st.title("SEC Filing Summarization App")

# User input for filing URL
filing_url = st.text_input("Enter the SEC filing URL:")

# Dropdown to select section
sections = ['1', '1A', '1B', '6', '7', '7A', '8', '9']
sections_dict = {"1": "Business", "1A": "Risk Factors", "1B" : "Unresolved Staff Comments", "6": "Selected Financial Data", "7": "Management Discussion and Analysis of Financial Condition and Results of Operation", "7A": "Quantitative and Qualitative Disclosures about Market Risk", "8": "Financial Statements and Supplementary Data", "9": "Changes in and Disagreements with Accountants on Accounting and Financial Disclosure"}
selected = st.selectbox("Select the section of the SEC filing to summarize:", sections_dict.items())
selected_pair = selected[0]  # Accessing the first key-value pair
selected_section = selected_pair[0] 
if st.button("Summarize"):
    if filing_url:
        # Extract text from SEC filing using the Extractor API
        section_text = extractorApi.get_section(filing_url, selected_section, 'text')

        # Clean the extracted text
        cleaned_text = clean_text(section_text)

        # Split the text into smaller chunks
        chunk_size = 40000  # Adjust as needed
        text_chunks = split_text(cleaned_text, chunk_size)

        # Load the model
        model = "models/text-bison-001"

        # Summarize each chunk of text
        summaries = summarize_text_chunks(text_chunks, model)

        # Combine summaries into a single text
        # Flatten the list of lists
        combined_summary = " ".join(str(point) for sublist in summaries for point in sublist if point is not None)

      
        # Display the summaries
        st.subheader("Summary")
        for i, summary in enumerate(summaries):
            st.write(summary)
    else:
        st.warning("Please enter the SEC filing URL.")
