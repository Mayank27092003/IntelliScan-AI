IntelliScan AI: Project README
Summary

IntelliScan AI is a Streamlit web application that uses a Keras Convolutional Neural Net- work (CNN) to classify medical conditions like Covid-19 and Pneumonia from X-ray images. Built with Python, the tool achieves approximately 93% accuracy, offering a fast and reliable method for preliminary medical image analysis.

Description

IntelliScan AI is a project developed to explore the practical applications of artificial intel- ligence in the medical field. It serves as a powerful demonstration of how deep learning can be harnessed to create accessible and efficient tools for diagnostic assistance. The core mis- sion is to provide rapid, AI-driven analysis of X-ray images, making complex technology more understandable and useful.

Technology Stack
The project leverages a modern stack for machine learning and web deployment:
•	Backend: Python
•	Machine Learning: Keras (TensorFlow)
•	Web Framework: Streamlit

Model Architecture
The core of the application is an 8-layer CNN designed to identify complex patterns in radio- logical images. It processes an input X-ray and passes it through specialized layers to make a final classification.

Model Summary Table

Layer (type)	Output Shape	Param #
conv2d (Conv2D)	(None, 222, 222, 32)	896
max pooling2d
(None, 111, 111, 32)	0
conv2d 1 (Conv2D)
(None, 109, 109, 64)	18496
max pooling2d 1
(None, 54, 54, 64)	0
conv2d 2 (Conv2D)
(None, 52, 52, 128)	73856
max pooling2d 2
(None, 26, 26, 128)	0
flatten (Flatten)	(None, 86528)	0
dense (Dense)	(None, 128)	11075712
 
The model’s Convolutional and Pooling layers act as feature extractors, identifying key visual markers. The final Dense layer acts as the decision-maker, analyzing these features to classify the image.
