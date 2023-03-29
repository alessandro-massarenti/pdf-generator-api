from io import BytesIO
from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


class PdfService:

    @staticmethod
    def get_pdf(nome):
        today_date = datetime.today()
        context = {'sender': nome["name"], 'receiver': "Gian", 'oggetti': [{"qt": 23}], 'today_date': today_date}
        #use the template folder to load the html
        template_loader = FileSystemLoader('./templates/')
        template_env = Environment(loader=template_loader)
        template = template_env.get_template('child.html')
        html = template.render(context)
        # create a pdfoutput_text
        output = BytesIO()
        pisa_status = pisa.CreatePDF(src=html, dest=output)
        # if error then show some funny view
        if pisa_status.err:
            print("error")
            return
        return output
