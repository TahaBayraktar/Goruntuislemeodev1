from turtle import shape
import cv2
import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros

foto=cv2.imread("../deneme.jpeg", 0)
hist=zeros(256)
print(foto.shape)
[w,h]=foto.shape
for v in range(0,h):
    for u in range(0,w):
        i=foto[u,v]
        hist[i]+=1
plt.plot(hist)
plt.show()
