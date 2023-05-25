#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load the necessary packages
import cv2


# In[3]:


# Read the Image and convert to grayscale
img = cv2.imread('pyramid1.jpg')
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[4]:


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows


# In[5]:


#Use Global thresholding to segment the image
ret,thresh_img1 = cv2.threshold(img, 120,255,cv2.THRESH_BINARY)
ret,thresh_img2=cv2.threshold(gray,86,255,cv2.THRESH_BINARY_INV)

ret,thresh_img3=cv2.threshold(gray,86,255,cv2.THRESH_TOZERO)

ret,thresh_img4=cv2.threshold(gray,86,255,cv2.THRESH_TOZERO_INV)

ret,thresh_img5=cv2.threshold(gray,100,255,cv2.THRESH_TRUNC)


# In[6]:


# Use Adaptive thresholding to segment the image

thresh_img6=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

thresh_img7=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


# In[7]:


# Use Otsu's method to segment the image 
ret,thresh_img8=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# In[8]:


# Display the results

image = [thresh_img1,thresh_img2,thresh_img3,thresh_img4,thresh_img5,thresh_img6,thresh_img7,thresh_img8]
for i in range(0,8):
    cv2.imshow('threshold_image',image[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows


# In[ ]:




