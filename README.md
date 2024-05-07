# SEC Filing Summarization App

This Streamlit web application allows users to summarize sections of SEC filings using AI-powered text summarization. Users can input the URL of the SEC filing and select the section they want to summarize. The application then extracts the text from the specified section, cleans it, and generates a concise summary using Google's PaLM API.

# [Demo](https://youtu.be/pEuKsEnY1Fo)

# Tech Stack

1. **Streamlit:** Chosen for its ease of use in building interactive web applications with Python, providing a straightforward user interface for accessing the summarization functionality.

2. **Google GenerativeAI (PaLM API):** Utilized for text summarization due to its advanced natural language processing capabilities, allowing for the generation of concise summaries from lengthy SEC filings. Google's PaLM (Pattern-Exploiting Language Model) API is chosen for text summarization due to its advanced capabilities in understanding the context and structure of text. PaLM excels in summarizing lengthy documents like SEC filings by extracting the most relevant information while preserving context, leading to more accurate and coherent summaries.

3. **SEC API:** Used for accessing SEC filings programmatically, enabling users to input the URL of the filing they want to summarize directly into the application.


# What is an SEC filing?

The SEC filing is a financial statement or other formal document submitted to the U.S. Securities and Exchange Commission. Public companies, certain insiders, and broker-dealers are required to make regular SEC filings.

# What is a 10-K?

- A 10-K is a comprehensive report filed annually by public companies about their financial performance.
- The report is required by the U.S. Securities and Exchange Commission (SEC) and is far more detailed than the annual report.
- Information in the 10-K includes corporate history, financial statements, earnings per share, and any other relevant data.
- The 10-K is a useful tool for investors to make important decisions about their investments.

This application can summarize the following sections of a 10K filing:

1. **Business (Item 1):** Investors and analysts are interested in understanding the nature of the company's business operations, including its products or services, markets served, competition, and key strategies. This section provides insights into the company's core activities and the factors influencing its performance.

1A. **Risk Factors (Item 1A):** Users want to identify and assess the risks that could impact the company's financial condition and results of operations. Understanding these risks helps investors make informed decisions about the company's prospects and potential vulnerabilities.

1B. **Unresolved Staff Comments (Item 1B):** This section discloses any ongoing discussions or inquiries from regulatory authorities regarding the company's filings. Users, particularly investors and analysts, are interested in knowing if there are any unresolved issues that could affect the accuracy or completeness of the financial disclosures.

6. **Selected Financial Data (Item 6):** Investors and analysts use this section to review key financial metrics and performance indicators over multiple years. It provides a summarized view of the company's financial history, enabling users to assess trends and evaluate financial stability.

7. **Management Discussion and Analysis of Financial Condition and Results of Operation (Item 7):** This section offers management's perspective on the company's financial performance, discussing key drivers, challenges, opportunities, and future outlook. Users rely on this narrative to gain insights beyond the numbers and understand the underlying factors shaping the company's financial results.

7A. **Quantitative and Qualitative Disclosures about Market Risk (Item 7A):** Investors and analysts are interested in understanding the company's exposure to various market risks, such as interest rate risk, currency risk, commodity price risk, etc. This section provides details on how the company manages these risks and their potential impact on financial performance.

8. **Financial Statements and Supplementary Data (Item 8):** This is perhaps the most critical section for users as it presents the company's audited financial statements, including the balance sheet, income statement, cash flow statement, and notes to the financial statements. Users analyze these statements to assess the company's financial health, profitability, liquidity, and solvency.

9. **Changes in and Disagreements with Accountants on Accounting and Financial Disclosure (Item 9):** Users are interested in any past disagreements or changes in accounting practices between the company and its auditors. This section provides transparency regarding accounting issues and any potential impact on financial reporting integrity.

## Features

- Summarize selected sections of SEC filings into bullet points.
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


## Dependencies

- Streamlit
- Google GenerativeAI
- SEC API
- Matplotlib


## Contributors

- [Vidhyakshaya Kannan](vidhyakshaya.k-26@scds.saiuniversity.edu.in)

## License

This project is licensed under the [MIT License](LICENSE).
