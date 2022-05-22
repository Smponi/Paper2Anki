import shutil
from pathlib import Path
from typing import Callable

from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import FileResponse

from AnkiCreator import create_apkg
from Converter import Converter

app = FastAPI()
app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../HTML")


@app.get("/root", response_class=HTMLResponse)
async def display_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/pdf", response_class=FileResponse)
async def upload(
    anki_name: str = Form(...), pdf_file: UploadFile = File(...)
) -> FileResponse:
    path = None
    try:
        # Check if file is correct file type
        if pdf_file.content_type != "application/pdf":
            raise HTTPException(400, detail="Invalid document type")
        with open(f"{pdf_file.filename}", "wb") as buffer:
            shutil.copyfileobj(pdf_file.file, buffer)
        path = convert_file(pdf_file.filename, anki_name)
    finally:
        pdf_file.file.close()
    return FileResponse(Path(path), media_type="apkg", filename=path)


def convert_file(pdf_file, anki_name: str) -> str   :
    converter = Converter(pdf_file, anki_name)
    converter.convert()
    name = create_apkg(anki_name)
    converter.remove_temp()
    return name


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
