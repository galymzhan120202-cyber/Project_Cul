import os
import sys
from pptx import Presentation
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def convert_pptx_to_pdf(pptx_path, pdf_path):
    # Load the presentation
    prs = Presentation(pptx_path)

    # Create a PDF canvas
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Loop through each slide in the pptx
    for slide_number, slide in enumerate(prs.slides):
        # Set page size
        c.setPageSize((width, height))
        # Add a new page
        c.drawString(100, height - 100, f'Slide {slide_number + 1}')  # Add slide number
        # Here, we would need an actual implementation to draw slide content
        # For now, we just note which slides exist
        c.showPage()  # Finish the page

    c.save()


if __name__ == '__main__':
    pptx_file = 'Mahmud_al_Kashgari_Presentation.pptx'
    pdf_file = os.path.splitext(pptx_file)[0] + '.pdf'
    convert_pptx_to_pdf(pptx_file, pdf_file)
    print(f'Converted {pptx_file} to {pdf_file}')