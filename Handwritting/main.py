import pywhatkit as kit
import pytesseract
import cv2
txt = '''Hey zain '''

kit.text_to_handwriting(txt, save_to='demo.png')
img = cv2.imread("demo.png")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# try:
#     sendwhatmsg.sendwhatmsg("+abc",
#                           "nashta nh hai",
#                           14, 11
#                           )
#     print("Successfully Sent!")

# except:
#     print("An Unexpected Error!")
