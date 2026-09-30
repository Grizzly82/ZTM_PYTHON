import PyPDF2
import sys

input_pdf_path = sys.argv[1:]  # Get the input PDF path from command line arguments

def pdf_watermark(input_pdf_path, watermark_path, output_pdf_path):
    try:
        # Open the input PDF and watermark PDF
        with open(input_pdf_path, 'rb') as input_pdf_file, open(watermark_path, 'rb') as watermark_file:
            input_pdf = PyPDF2.PdfReader(input_pdf_file)
            watermark_pdf = PyPDF2.PdfReader(watermark_file)
            watermark_page = watermark_pdf.pages[0]

            # Create a PdfWriter object for the output PDF
            pdf_writer = PyPDF2.PdfWriter()

            # Loop through each page of the input PDF
            for page in input_pdf.pages:
                # Merge the watermark with the current page
                page.merge_page(watermark_page)
                pdf_writer.add_page(page)

            # Write the output PDF to a file
            with open(output_pdf_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)

        print(f"Watermarked PDF saved to: {output_pdf_path}")

    except FileNotFoundError:
        print("Error: The input PDF or watermark file was not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")