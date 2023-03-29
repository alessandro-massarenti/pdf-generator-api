from io import BytesIO
from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


class PdfService:

    @staticmethod
    def get_pdf(user_data):
        today_date = datetime.today()

        oggetti = [
            {"product": "mela", "qt": 2, "price": 2.5, "total": 5},
            {"product": "Coca Cola", "qt": 10, "price": 2, "total": 20},
            {"product": "Pasta", "qt": 1, "price": 1.5, "total": 1.5},
            {"product": "Fantasia", "qt": 3, "price": 1.5, "total": 4.5},
        ]

        context = {'sender': user_data["name"],'receiver': "Gian", 'items': user_data["items"], 'today_date': today_date}
        #use the template folder to load the html
        template_loader = FileSystemLoader('./templates/')
        template_env = Environment(loader=template_loader)
        template = template_env.get_template('child.html')
        html = template.render(context)
        # create a pdfoutput_text
        output = BytesIO()
        pisa_status = pisa.CreatePDF(src=html, dest=output, encoding='utf-8')
        # if error then show some funny view
        if pisa_status.err:
            print("error")
            return
        return output
