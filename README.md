# InverseImage
Project testing interpretability of "inverse images"
The concept came from the idea of inverse matrices
Considering a picture of a certain pixel resolution like 400x400 would usually be 400x400x3 for each color channel, 
grayscaling the images gives a matrix with integer entries thus if the image is square and invertible you could potentially compute an "inverse image"
This unfortunately resulted in nothing interpretable. I then decided to try to find an inverse A-B picture, Given a picture A and B what is the image that transforms one into the other? So solving AX=B gives X=(A')B. This also gave nothing interpretable. 
