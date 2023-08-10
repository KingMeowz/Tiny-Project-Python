from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_jpg_to_pdf(jpg_path, pdf_path):
    image = Image.open(jpg_path)
    pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)

    pdf_canvas.setPageSize((image.width, image.height))
    pdf_canvas.drawImage(jpg_path, 0, 0, image.width, image.height)

    pdf_canvas.save()


# Usage example
jpg_path = 'up/down.jpg'  # Replace with your JPG file path
# Replace with the desired output PDF file path
pdf_path = 'up/down.jpg'

convert_jpg_to_pdf(jpg_path, pdf_path)
