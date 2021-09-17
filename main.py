import shutil
from fastapi import FastAPI,File,UploadFile, HTTPException 
from fastapi.responses import HTMLResponse
from pydantic.fields import Field

app = FastAPI()


@app.post("/pdf")
async def root(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf"]:
        raise HTTPException(400, detail="Invalid document type")
    with open(f'{file.filename}',"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}
