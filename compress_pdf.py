import PyPDF2


def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        # Iterate over each page in the input PDF
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            page.compress_content_streams()  # Compress the content streams of the page
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)


# Usage example
# Replace with the path of the input PDF file
input_path = '\images\you.jpg'
# Replace with the desired output PDF file path
output_path = '\images\you_2.jpg'

compress_pdf(input_path, output_path)
