import ddddocr

det = ddddocr.DdddOcr(det=False, ocr=False)

with open(r'D:\Project\Engage2024\DDDDOCR\image\SliderDetection\1_target.png', 'rb') as f:
    target_bytes = f.read()

with open(r'D:\Project\Engage2024\DDDDOCR\image\SliderDetection\1_background.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes)

print(res)