# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     # example.py
#     import ddddocr
#
#     ocr = ddddocr.DdddOcr()
#
#     image = open("F:\\Code\\Project\\Program\\Engage2024\\ddddocr\\image\\5.png", "rb").read()
#     result = ocr.classification(image)
#     print(result)
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

import ddddocr
import cv2

det = ddddocr.DdddOcr(det=True)

with open(r"D:\Project\Engage2024\DDDDOCR\image\TargetDetection_image\5.png", 'rb') as f:
    image = f.read()

bboxes = det.detection(image)
print(bboxes)

im = cv2.imread(r"D:\Project\Engage2024\DDDDOCR\image\TargetDetection_image\5.png")

for bbox in bboxes:
    x1, y1, x2, y2 = bbox
    im = cv2.rectangle(im, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)

cv2.imwrite(r"D:\Project\Engage2024\DDDDOCR\image\TargetDetection_image\5_result.png", im)
