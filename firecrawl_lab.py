import requests
import ollama
from fpdf import FPDF

# Configuration
FIRECRAWL_API_KEY = 'fc-1cb30e59374046cab8006393f5fa4b61'
FIRECRAWL_URL = 'https://api.firecrawl.dev/v1/scrape'
MODEL_NAME = 'mistral'

# Data Collection
def collect_data_from_url(url):
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {FIRECRAWL_API_KEY}'
    }
    json_data = {
        'url': url
    }
    response = requests.post(FIRECRAWL_URL, headers=headers, json=json_data)
    response.raise_for_status()
    return response.json().get('text', '')

# Process with LLM
def process_with_llm(content):
    print("\nProcessing content with offline LLM...")
    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{
            'role': 'user',
            'content': (
                "Please summarize and extract key actionable insights "
                "from the following content for a cybersecurity student:\n\n"
                f"{content}"
            )
        }]
    )
    return response['message']['content']

# Generate PDF
def generate_pdf(content, filename="agentic_ai_summary.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content.split('\n'):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)
    print(f"\nPDF report generated: {filename}")

# Main Execution
def main():
    print("=== Agentic AI Lab: Firecrawl + Offline LLM + PDF Generator ===")
    url = input("Enter the URL to collect data from: ")

    try:
        scraped = collect_data_from_url(url)
        if not scraped:
            print("No content retrieved from the URL.")
            return

        summary = process_with_llm(scraped)
        print("\n--- LLM Processed Summary ---")
        print(summary)

        generate_pdf(summary)

    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
