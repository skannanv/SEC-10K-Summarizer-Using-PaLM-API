# SEC Filing Summarization App

This Streamlit web application allows users to summarize sections of SEC filings using AI-powered text summarization. Users can input the URL of the SEC filing and select the section they want to summarize. The application then extracts the text from the specified section, cleans it, and generates a concise summary using Google's PaLM API.

## Features

- Summarize sections of SEC filings into bullet points.
- Perform sentiment analysis on the summarized text.
- User-friendly interface with input fields and dropdown menus.

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required Python packages listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app with the following command:
   ```
   streamlit run app.py
   ```
4. Access the app in your web browser at the provided URL (typically `http://localhost:8501`).

## Usage

1. Enter the URL of the SEC filing in the text input field.
2. Select the section of the SEC filing you want to summarize from the dropdown menu.
3. Click the "Summarize" button to generate the summary.
4. View the summarized text and sentiment analysis.

## Dependencies

- Streamlit
- Google GenerativeAI
- SEC API
- WordCloud
- Matplotlib
- TextBlob

## Contributors

- [Vidhyakshaya Kannan] - [vidhyakshaya.k-26@scds.saiuniversity.edu.in]

## License

This project is licensed under the [MIT License](LICENSE).
