import fitz
import os

pdf_path = "report.pdf"
doc = fitz.open(pdf_path)

os.makedirs("figures", exist_ok=True)
os.makedirs("figures_raw", exist_ok=True)

# 1. Export page 6 of the report PDF as an image and save it to figures/topology-block.png
page = doc.load_page(5) # 0-indexed, so page 6 is index 5
pix = page.get_pixmap(dpi=300)
pix.save("figures/topology-block.png")

# 2. Extract embedded images
for i in range(len(doc)):
    for img in doc.get_page_images(i):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.n - pix.alpha > 3:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.save(f"figures_raw/img_{i}_{xref}.png")
        pix = None

print("Images extracted successfully.")
