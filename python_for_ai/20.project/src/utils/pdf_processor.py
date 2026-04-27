from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract content from pdf file using PyPdf
    Args: 
    pdf_paths: Path to the pdf file
    The extracted text as a single string
    """

    try:
        reader = PdfReader(pdf_path)
        full_text = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)
        return "\n".join(full_text)
    except FileNotFoundError:
        print("Error : file not found at {pdf_path} ")
        return ""
    except Exception as e:
        print(f"An error occured while extracting file {e}")
