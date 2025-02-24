import os
from jinja2 import Template
from weasyprint import HTML
import base64

# Function to encode images to Base64
def encode_image_to_base64(image_path):
    """Converts an image file to a Base64 string."""
    try:
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        return ""

# HTML template with Jinja2 placeholders
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate</title>
    <style>
        @page { size: A4 landscape; margin: 0; }
        body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f5f5f5;
        }
        .certificate {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            color: #000;
            padding: 30px;
        }
        .background {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            z-index: -1;
        }
        h1 { font-family: Arial, sans-serif; font-size: 48px; font-weight: bold; }
        .details { font-size: 24px; font-weight: bold; }
        .usn { font-size: 18px; font-weight: normal; }
        .footer { position: absolute; bottom: 50px; width: 100%; text-align: center; }
        .signature img { max-height: 70px; margin-bottom: -10px; }
        .signature p { font-size: 18px; font-weight: bold; margin: 0; }
    </style>
</head>
<body>
    <div class="certificate">
        <!-- Background Image -->
        <img class="background" src="{{ background_image_path }}" alt="Certificate Background">
        
        <h1>CERTIFICATE OF INTERNSHIP</h1>
        <p class="details">{{ name }} <span class="usn">({{ usn }})</span></p>
        <p>has successfully completed a 10-day training in Python with Database Integration.</p>
        <div class="footer">
            <div class="signature">
                <img src="{{ signature_image_base64 }}" alt="Signature">
                <p>Managing Director</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Function to process HTML files and generate PDFs
def generate_certificates_from_html(input_html_directory, output_directory):
    """Processes HTML files from a directory and generates PDFs."""
    os.makedirs(output_directory, exist_ok=True)

    # Use absolute file path for background image
    background_image_path = os.path.abspath("Certificate_Generator(White)/assests/background.png")
    
    # Encode signature image as Base64 (small image works fine in Base64)
    signature_image_base64 = encode_image_to_base64("Certificate_Generator(White)/assests/sign.png")

    # Loop through HTML files in the input directory
    for filename in os.listdir(input_html_directory):
        if filename.endswith(".html"):
            input_html_path = os.path.join(input_html_directory, filename)

            # Extract name and usn from filename
            try:
                parts = filename.rsplit('_', 1)
                name = parts[0]
                usn = parts[1].replace('.html', '')
            except IndexError:
                print(f"Skipping file {filename} due to incorrect naming format.")
                continue

            # Render HTML from template
            template = Template(html_template)
            rendered_html = template.render(
                name=name,
                usn=usn,
                background_image_path=background_image_path,  # Corrected path
                signature_image_base64=signature_image_base64
            )

            # Output PDF path
            pdf_file_path = os.path.join(output_directory, f"{name}_{usn}.pdf")

            try:
                # Generate PDF from HTML
                HTML(string=rendered_html, base_url=os.getcwd()).write_pdf(pdf_file_path)
                print(f"Generated: {pdf_file_path}")
            except Exception as e:
                print(f"Error generating PDF for {filename}: {e}")

# Main function
if __name__ == "__main__":
    input_html_directory = r"C:\Users\abhin\OneDrive\Documents\SIC\SIC\Certificate_Generator(White)\html_certificates"  # Input directory
    output_directory = r"C:\Users\abhin\OneDrive\Documents\SIC\SIC\Certificate_Generator(White)\pdf_certificates"  # Output directory
    try:
        generate_certificates_from_html(input_html_directory, output_directory)
    except Exception as e:
        print(f"Critical Error: {e}")
