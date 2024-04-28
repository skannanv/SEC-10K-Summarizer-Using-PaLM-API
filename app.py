import streamlit as st
import re
import google.generativeai as palm
from sec_api import ExtractorApi  # Import SEC Extractor API
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from textblob import TextBlob
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
                 "Please summarize and output 3 BULLET POINTS ONLY. Do not use the words 'bullet points' " \
                 "in your answer. Make sure the output is WELL FORMATTED and EASY TO UNDERSTAND. Otherwise, a child will die. If there is no relevant or important information, output an empty string. The relevant information is below:\n" + chunk
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

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

# Initialize SEC Extractor API
extractorApi = ExtractorApi("c905a34a80b5a9ff1420f43193a4af1d202ab63b69060918470fd486669461d0")
palm.configure(api_key=config.API_KEY)
# Streamlit UI
st.title("SEC Filing Summarization App")

# User input for filing URL
filing_url = st.text_input("Enter the SEC filing URL:")

# Dropdown to select section
sections = ['1', '1A', '7', '7A', '8', '9']
selected_section = st.selectbox("Select the section of the SEC filing to summarize:", sections)

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
        combined_summary = " ".join(point for sublist in summaries for point in sublist if point is not None)

        # Perform sentiment analysis
        sentiment = analyze_sentiment(combined_summary)
        st.subheader("Sentiment Analysis")
        st.write(f"Overall Sentiment: {sentiment.polarity}")
        
        # Display the summaries
        st.subheader("Summary")
        for i, summary in enumerate(summaries):
            st.write(summary)
    else:
        st.warning("Please enter the SEC filing URL.")
