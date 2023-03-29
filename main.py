from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import File
import tempfile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

#A route that given a json data from the client returns a pdf file with the data
@app.post("/pdf")
async def pdf(data: dict):

    from Services.PdfService import PdfService

    pdf = PdfService.get_pdf(data)
    pdf.seek(0)

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf.getvalue())

    return FileResponse(tmp_file.name, media_type="application/pdf", filename="reportoh.pdf")
