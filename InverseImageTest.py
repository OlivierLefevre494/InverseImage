import cv2
import numpy as np

image = cv2.imread("images/test-1.png")
imagend = cv2.imread("images/test-2.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_imagend = cv2.cvtColor(imagend, cv2.COLOR_BGR2GRAY)

cropped = gray_image[0:4000, 0:4000]
croppedend = gray_imagend[0:4000, 0:4000]


#inversepicture = np.linalg.inv(cropped)
inversepicture = np.negative(cropped)
end = np.add(inversepicture, croppedend)


cv2.imshow("Cropped Image", inversepicture)
cv2.imshow("POOPOO MAN", end)

cv2.waitKey(0)

cv2.destroyAllWindows()
print(inversepicture)