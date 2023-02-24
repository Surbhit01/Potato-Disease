# POTATO DISEASE

## PROBLEM STATEMENT

Detecting if the leaf of a potato plant is healthy or is suffering from early or late blight. 
Project reference link - [Codebasics](https://www.youtube.com/watch?v=dGtDTjYs3xc&list=PLeo1K3hjS3utJFNGyBpIvjWgSDY0eOE8S)

## DATASET

The dataset contains 3 different classes of images - healthy leaves, early blight infected and late blight infected leaves. There are total 2152 images. Early and late blight contain 1000 images each and 100 images for late blight. <br> <br>
**SAMPLES**

![1f9870b3-899e-46fb-98c9-cfc2ce92895b___RS_HL 1816](https://user-images.githubusercontent.com/24591039/221207547-7708f47d-7924-45bb-a58e-8cff6c007089.JPG)

[Image Above] Healthy Leaf

![0d2e2971-f1c9-4278-b35c-91dd8a22a64d___RS_Early B 7581](https://user-images.githubusercontent.com/24591039/221208069-36c24769-c220-4b6a-9ac2-fd1872f2ea7c.JPG)

[Image Above] Early Blight Infected Leaf

![1a674846-9d13-4a7f-ba03-8931c5dd3d2c___RS_LB 2768](https://user-images.githubusercontent.com/24591039/221209138-1b8cf3b7-5055-4045-a516-43150aeff290.JPG)

[Image Above] Late Blight Infected Leaf



## APPROACH

All images were resized to 256x256 and scaled 0-1 pixel values. Data augmented was performed on these images (flipping and rotation). Model for prediction was built using CNN architecture. The classification service was hosted locally using flask.

![model](https://user-images.githubusercontent.com/24591039/221213666-7f70673a-0471-4fe5-b876-3ee84fbbf519.png)

[Image above] Model Architecture


![DiseasePred](https://user-images.githubusercontent.com/24591039/221214414-62f36ba7-c110-430a-966b-aab1bf6c32e0.png)

[image Above] Homepage
