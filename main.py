from Converter import Converter
from AnkiCreator import create_apkg
from os import unlink
import shutil
from tempfile import template
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.param_functions import Form
from fastapi.responses import HTMLResponse
from pydantic.fields import Field
from pathlib import Path
from typing import Callable
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from starlette.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="HTML")


@app.get("/root", response_class=HTMLResponse)
async def display_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/pdf")
async def upload(pdf_file: UploadFile = File(...)) -> None:
    try:
        if pdf_file.content_type != "application/pdf":
            raise HTTPException(400, detail="Invalid document type")
        with open(f"{pdf_file.filename}", "wb") as buffer:
            shutil.copyfileobj(pdf_file.file, buffer)
        convert_file(pdf_file.filename)
    finally:
        pdf_file.file.close()


def convert_file(pdf_file):
    converter = Converter(pdf_file, "in1")
    converter.convert()
    create_apkg("in1")
    converter.remove_temp()


def handle_upload_file(
    upload_file: UploadFile, handler: Callable[[Path], None]
) -> None:
    tmp_path = upload(upload_file)
    try:
        # Do something with the saved tempfile
        handler(tmp_path)
    finally:
        # Delete the tempfile
        tmp_path.unlink()

# def handler(
#    pdf: Path
# ):
