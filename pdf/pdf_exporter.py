from fpdf import FPDF
from datetime import datetime

def generate_pdf(summary, fig_path, output_path="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Analysis Report", ln=True, align='C')
    pdf.cell(200, 10, txt=str(datetime.now()), ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, summary)
    pdf.image(fig_path, w=180)
    pdf.output(output_path)