# example.py
import ddddocr

ocr = ddddocr.DdddOcr()

image = open(r"D:\Project\Engage2024\DDDDOCR\image\BasicOCR_image\5.png", "rb").read()
result = ocr.classification(image)
print(result)