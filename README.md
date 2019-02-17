### [This README is under construction.]


* I am in the process of converting my presentation for this project from slideshow into a proper README format.

* Thanks for your patience!



# Automated Photograph Culling

### Abstract

This is my capstone project for Flatiron School.  I built two image classification models using convolutional neural networks, achieving accuracy scores of 91.5% and 88.5%. The models were combined into an application, currently in beta version.

----

### Motivation

I am not a photographer, nor am I passionate about photography. But my current roommate is a passionate photographer who runs her own business. When she gets home from shoots, she has between 1000 to 2000 photos which she has to sort though manually. For my latest project I wanted to attempt to use deep learning techniques and python to build something that could save her time during the culling process.


#### Question?

* Can I use deep learning to classify photos based on specific features?

#### Goals:

* Identify photos that are blurry and not blurry
* Identify photos that do and don't contain people blinking
* Identify photos that are duplicate/similar  
* Build a platform that automatically sorts photos for photographers to save time during the culling process

----
### Datasets

I curated my own custom datasets through combining several other datasets as well as scraping and cropping images.

* For the blurry model, I combined the [CERTH  image blur dataset](https://mklab.iti.gr/results/certh-image-blur-dataset/) and the [Portland State University, Blur image Dataset](https://riemenschneider.hayko.at/vision/dataset/task.php?did=382). I made this decision because I wanted the "blurry label" to be a more accurate representation of photographs that are good vs. bad. After combining the two sources, the dataset contains both artificially blurry and naturally blurry photos.

* For the blinking model, I started out with the [Closed Eyes In The Wild (CEW)](http://parnec.nuaa.edu.cn/xtan/data/ClosedEyeDatabases.html) dataset. Then, I manually went through and deleted photos which were incorrectly labeled or were of significantly poor quality. Lastly, using several Google image searches, I scraped and cropped roughly 500 images of both blinking and non-blinking eyes to make sure my dataset was large enough.


#### Preprocessing

The preprocessing steps for the blurry model were far less intense than the blinking model.

For the blurry model,

For the blinking model, 


---

### Models



---

### Next steps

* Identify duplicate/similar photos
* Further develop the application
