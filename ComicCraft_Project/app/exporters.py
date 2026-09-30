import os
from fpdf import FPDF

EXPORT_DIR = "static/exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def save_pdf(layout):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    for panel in layout:
        pdf.add_page()
        pdf.set_font("Arial", "B", 18)
        pdf.cell(0, 12, f"Panel {panel['panel_number']}: {panel['title']}", ln=True)

        image_path = panel["image"].lstrip("/")
        if os.path.exists(image_path):
            pdf.image(image_path, x=15, y=30, w=180)

        pdf.set_y(140)
        pdf.set_font("Arial", "I", 11)
        pdf.multi_cell(0, 7, panel["scene_description"])

        pdf.ln(4)
        pdf.set_font("Arial", size=11)
        # Replace uncommon Unicode characters for basic FPDF fonts.
        text = panel["text"].encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 7, text)

    filename = os.path.join(EXPORT_DIR, "comiccraft_comic.pdf")
    pdf.output(filename)
    return "/" + filename.replace("\\", "/")
