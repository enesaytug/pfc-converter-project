import fitz
import os
import glob

os.makedirs("figures", exist_ok=True)
pdfs = glob.glob("*.pdf")
for pdf in pdfs:
    if pdf == "report.pdf": continue
    doc = fitz.open(pdf)
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=300)
    out_name = "figures/" + pdf.replace(".pdf", ".png").replace(" ", "_")
    pix.save(out_name)
    print(f"Converted {pdf} to {out_name}")
