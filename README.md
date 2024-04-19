# Amharic Character Recognition with U-Net 📜🔍

This repository is dedicated to the Bachelor thesis project focusing on Amharic character recognition using the U-Net architecture. Amharic, an ancient Semitic language used in Ethiopia, possesses a unique character system, 'Fidel Gebeta'. This project aims to explore state-of-the-art neural network models to improve the accuracy of Amharic character recognition, an area that has seen less development compared to other non-Latin languages.

## Project Summary 📝

The U-Net architecture has shown promising results in various image recognition tasks, which inspired its application to Amharic characters. By comparing a sequential CNN model and the U-Net model, the study demonstrates the superior performance of U-Net, achieving an accuracy of 93.37%. This accuracy is obtained by utilizing a U-Net model with two-layer depth as a feature extractor along with multi-task learning classifiers that pinpoint the row and column of characters in 'Fidel Gebeta'.

## Datasets 📊

The project utilizes three datasets:
- Amharic character dataset (Source: Belay B., Habtegebrial T., Liwicki M., et al., 2019)
- The MNIST dataset of handwritten digits
- The Kaggle A-Z handwritten alphabet dataset

These datasets are employed in various combinations as required for specific model training and evaluation tasks.

## Repository Structure 🗂️

- `-amh-alpha`: Contains training scripts and saved models for Amharic character recognition, including sequential CNN, single depth U-Net, two-layer depth U-Net, and Factored CNN models.
- `-eng-alpha`: Similar to `amh-alpha` but for the English alphabet, specifically using the Kaggle A-Z handwritten character dataset.
- `-eng-alphanum`: Contains scripts and models for recognition of a mixed dataset comprising the Kaggle A-Z handwritten characters and MNIST digit dataset.

## Thesis Paper 📄

For more detailed insights into the research, methodologies, and results, you can access the full thesis paper here: [Link to Thesis Paper](#).

## Gallery 🖼️

![Amharic Character Recognition Results](path-to-your-image.jpg)

Replace `path-to-your-image.jpg` with the actual path to your image in the repository when you're ready to display it.

## Acknowledgments 🙏

Special thanks to Belay B., Habtegebrial T., Liwicki M., et al., for their 2019 paper "Factored Convolutional Neural Network for Amharic Character Image Recognition" that provided the dataset enabling this research.

## Reference 📖

- Belay B., Habtegebrial T., Liwicki M., et al. (2019). Factored Convolutional Neural Network for Amharic Character Image Recognition; proceedings of the 2019 IEEE International Conference on Image Processing (ICIP), Sept. 22-25, 2019.
