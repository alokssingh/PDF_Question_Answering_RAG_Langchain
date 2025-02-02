# Semi-Structured RAG Langchain

This project is designed to process semi-structured documents and perform question answering using the Retrieval-Augmented Generation (RAG) techniques with the Langchain library.

## Installation

1. #### Install the necessary packages 
   ! pip install langchain unstructured[all-docs] pydantic lxml langchainhub

#### Additionally, ensure you have tesseract and poppler installed
   ! brew install tesseract poppler

#### Alternatively, Install the required dependencies listed in the requirements.txt file
   ! pip install -r requirements.txt

3. #### Command Line Arguments

   When running the scripts, you can specify command line arguments to customize the behavior:

   - `--filename`: Path to the PDF file to be processed. Default is `attention.pdf`.
   - `--path`: Path to the directory containing the PDF file. Default is `./data/`.

## Usage

#### Main Script

The `main.py` script orchestrates the entire process, from reading PDF files to generating answers to user questions.

#### Running the Main Script

To run the main script, use the following command:

```bash
python main.py --filename <path_to_pdf_file> --path <directory_containing_pdf_file>
```
### Note

Make sure to set up your OpenAI API key in your environment or directly in the script if you plan to use OpenAI services.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
# PDF_Question_Answering_RAG_Langchain
