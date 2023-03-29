from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import File
import tempfile

app = FastAPI()
last_data = None

@app.get("/")
async def root():
    return {"info": "pdf generating api on /pdf"}

#A route that given a json data from the client returns a pdf file with the data
@app.post("/pdf")
async def pdf(data: dict):

    global last_data
    last_data = data

    from Services.PdfService import PdfService

    pdf = PdfService.get_pdf(data)
    pdf.seek(0)

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf.getvalue())

    return FileResponse(tmp_file.name, media_type="application/pdf", filename="reportoh.pdf")

@app.get("/pdf")
async def pdf():
    global last_data

    if last_data is None:
        return {"error": "no data"}


    from Services.PdfService import PdfService

    pdf = PdfService.get_pdf(last_data)
    pdf.seek(0)

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf.getvalue())

    headers = {
        "Content-Disposition": "inline; filename=output.pdf",
        "Content-Type": "application/pdf",
    }
    return FileResponse(tmp_file.name, media_type="application/pdf", filename="reportoh.pdf", headers=headers)