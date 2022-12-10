import cv2


img_filter = cv2.imread("filter.jpg")
img_medyan = cv2.imread("median.jpg")
img_bilateral = cv2.imread("bilateral.jpg")

ksize = (5, 5)
blur = cv2.blur(img_filter, ksize)
blur_g = cv2.GaussianBlur(img_filter, ksize, cv2.BORDER_DEFAULT)

median_blur = cv2.medianBlur(img_medyan, 5)
bilateral_blur = cv2.bilateralFilter(img_bilateral, 9, 95, 95)

cv2.imshow("original", img_filter)
cv2.imshow("blur", blur)
cv2.imshow("blurG", blur_g)

cv2.waitKey(0)
cv2.destroyAllWindows()