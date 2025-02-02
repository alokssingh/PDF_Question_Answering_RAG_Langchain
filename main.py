import logging
import warnings
import argparse
from pdf_processor import PDFProcessor
from text_processing import count_tables_text, categorize_by_type
from summarization import summarize_chains
from generation import generation
from embedding import embeddings
import yaml


def main():
    """
    Main function to orchestrate the entire process.
    """
    # Load configuration from config.yaml
    with open('config.yaml', 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

    # Access the API key from the configuration
    api_key = config.get("api_key")
    if api_key is None:
        print("Error: API key not found in config.yaml.")
        return

    # Configure logging
    logging.basicConfig(filename='processing.log', level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Suppress specific type of warning
    warnings.filterwarnings("ignore", message="Some weights of the model checkpoint.*")

    logger.info("Script started")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--filename', type=str, default="manual.pdf", help='Path to the PDF file')
    parser.add_argument('--path', type=str, default='./data/',
                        help='Path to the directory containing the PDF file')
    args = parser.parse_args()
    filename = args.filename
    path = args.path
    logger.info(f"Reading PDF file: {filename}")

    print(f"Reading PDF file: {filename}")

    # Input question
    question = input("Enter your question: ")

    # Process PDF
    processor = PDFProcessor(path)
    raw_pdf_elements = processor.read_pdf(filename)
    logger.info("PDF processing completed")

    # Count tables and text elements
    category_counts = count_tables_text(raw_pdf_elements)
    logger.info(f"Number of tables: {category_counts.get('Table', 0)}")
    logger.info(f"Number of text elements: {category_counts.get('Text', 0)}")

    # Categorize PDF elements
    table_elements, text_elements = categorize_by_type(raw_pdf_elements)
    logger.info("PDF elements categorized")

    # Summarize tables and text
    tables, table_summaries, texts, text_summaries = summarize_chains(table_elements, text_elements, api_key)
    logger.info("Summarization completed")

    # Generate embeddings
    retriever = embeddings(text_summaries, table_summaries, texts, tables, api_key)
    logger.info("Embeddings generated")

    # Generate response
    output = generation(retriever, question, api_key)
    logger.info("Response generated")

    print("Answer is ", output)


if __name__ == '__main__':
    main()


