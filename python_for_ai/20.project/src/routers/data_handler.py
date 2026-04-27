from fastapi import APIRouter, UploadFile, File, Query, HTTPException
import uuid as uuid_pkg
import os

# import the share data store
from src.data_store import data_store

# pdf processing utility
from src.utils.pdf_processor import extract_text_from_pdf

# llm client utility
from src.utils.llm_client import get_llm_response

# temp directory
UPLOAD_DIR = "uploads/temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()


@router.post("/update/{uuid}", status_code=201)
def upload_pdf(uuid: uuid_pkg.UUID, file: UploadFile = File(...)):
    """
    upload pdf file with assosiate uuid
    extract content from file then store content
    if uuid already exist! raise error PUT to Update
    """
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400, detail="Invalid file type! Only pdf files accpted:")

    uuid_str = str(uuid)
    if uuid_str in data_store:
        raise HTTPException(
            status_code=400, detail="uuid already exist!  put to update this file")

    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_{file.filename}")

    try:
        # save upload file temporary
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Extract text using utility function
        extracted_text = extract_text_from_pdf(file_path)
        print("Text:", extracted_text)

        if extracted_text is None:
            raise HTTPException(
                status_code=500, detail="Failed to extract text from pdf")

        # store extracted text
        data_store[uuid_str] = extracted_text
        print("data_store:", data_store)
        return {
            "message": "File Upload and text extracted successfully",
            "uuid": uuid_str
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error occred during file process {str(e)}")
    finally:
        # clean up the tempprary file
        if os.path.exists(file_path):
            os.remove(file_path)


@router.post("/upload/{uuid}")
def update_pdf(uuid: uuid_pkg.UUID,   file: UploadFile = File(...)):
    """
    extract text and adds new text into existing file against UUID,
    check uuid is already exist, or not , if not raise error
    """

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400, detail="Invalid file type! Only pdf files accpted:")

    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(
            status_code=400, detail="uuid not exist!  please first upload documents")

    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_{file.filename}")

    try:
        # save upload file temporary
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # Extract text using utility function
        new_extracted_text = extract_text_from_pdf(file_path)
        print("Text:", new_extracted_text)

        if new_extracted_text is None:
            raise HTTPException(
                status_code=500, detail="Failed to extract new text from pdf")

        # append extracted text into existing content(Add seprator for clarity)
        data_store[uuid_str] += "\n\n" + new_extracted_text
        print("data_store:", data_store)
        return {
            "message": "File append successfully",
            "uuid": uuid_str
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error occred during file process {str(e)}")
    finally:
        # clean up the tempprary file
        if os.path.exists(file_path):
            os.remove(file_path)


@router.get("/query/{uuid}")
def query_from_pdf(uuid: uuid_pkg.UUID, query: str = Query(..., min_length=1)):
    """
    Retrieves the store text for UUID along with query to LLM service.
    Return the placeholder response
    """

    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(
            status_code=404, detail=" UUID {uuid_str} not found")

    stored_text = data_store[uuid_str]

    llm_response = get_llm_response(context=stored_text, query=query)

    return {"uuid": uuid_str, "query": query, "llm_response": llm_response}


@router.delete("/data/{uuid}", status_code=200)
def delete_data(uuid: uuid_pkg.UUID):
    """
    find uuid and delete data from data storage
    """
    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(
            status_code=404, detail="UUID not found:")

    del data_store[uuid_str]
    return {"message": "Data deleted successfully"}
