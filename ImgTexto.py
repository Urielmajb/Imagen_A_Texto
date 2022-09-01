from PIL import Image
import pytesseract

imagen = Image.open("descarga.png")
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

texto = pytesseract.image_to_string(imagen)
print(texto)