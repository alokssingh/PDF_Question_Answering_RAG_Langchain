# 🚀 Semi-Structured RAG with Langchain

This project processes **semi-structured documents** and performs **question answering** using **Retrieval-Augmented Generation (RAG)** techniques with the **Langchain** library. 📄🤖

---
## 🔧 RAG Pipeline
![a](https://github.com/alokssingh/PDF_Question_Answering_RAG_Langchain/blob/main/REG_flow.png)

---
## 🔧 Installation

### 1️⃣ Install Required Packages
```sh
pip install langchain unstructured[all-docs] pydantic lxml langchainhub
```

### 2️⃣ Install Additional Dependencies
#### 📌 Ensure `tesseract` and `poppler` are installed:
```sh
# For macOS
brew install tesseract poppler
```

### 3️⃣ Install Dependencies from `requirements.txt`
```sh
pip install -r requirements.txt
```

---

## ⚙️ Command Line Arguments
You can customize the script execution with the following options:

| Argument | Description | Default Value |
|----------|-------------|----------------|
| `--filename` | Path to the PDF file to process | `attention.pdf` |
| `--path` | Directory containing the PDF file | `./data/` |

Example Usage:
```sh
python main.py --filename my_document.pdf --path ./documents/
```

---

## 🎯 Usage

### 🚀 Running the Main Script
The **`main.py`** script manages the entire pipeline from reading PDF files to answering user queries.

Run the script using:
```sh
python main.py --filename <path_to_pdf_file> --path <directory_containing_pdf_file>
```

🔹 **Make sure to set up your OpenAI API key** in your environment or in the script if you plan to use OpenAI services.

---

## 🤝 Contributing
We welcome contributions! 💡 If you want to make major changes, please **open an issue** first to discuss it.

To contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Your Message"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **[MIT License](https://choosealicense.com/licenses/mit/)**.

🚀 **Happy Coding!** 🚀
