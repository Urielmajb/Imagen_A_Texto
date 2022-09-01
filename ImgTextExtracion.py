from PIL import Image
import pytesseract

imagen = Image.open("descarga.png")
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

texto_extraer = 'extraccion.txt'
f = open(texto_extraer,"a")
text = str(((pytesseract.image_to_string(imagen))))
text = text.replace('-\n', '*')
f.write(text)
f.close()

print("Se logro :D")

