# Stress-Detection-On-Social-Media
This repository contains the coding using python from data preprocessing until deployment 

 IPython Notebook can be found here: [Link](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Coding/New_P1_Stress_detection%20(2).ipynb)

# Objectives
1. To explore the effective feature extraction techniques that can improve stress detection models.
2. To build stress detection model by applying machine learning techniques to accurately detect stress on social media.
3. To evaluate the selected machine learning models performance using suitable evaluation metrics.

# Methodology
In this project, we are using SEMMA to create our methodology. 
Dataset Link: [Kaggle](https://www.kaggle.com/datasets/kreeshrajani/human-stress-prediction)
![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Pictures/methodology.jpg)

# BoW
| Models | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 73.77    | 77.52     | 73.80  | 75.61    |
| LR     | 75.70    | 78.69     | 76.68  | 77.67    |
| NB     | 76.06    | 74.65     | 85.62  | 79.76    |
| DT     | 62.15    | 68.56     | 57.83  | 62.74    |
| RF     | 73.24    | 73.61     | 80.19  | 76.76    |

# TF-IDF 
| Models | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 75.70    | 79.26     | 75.72  | 77.45    |
| LR     | 76.23    | 78.90     | 77.64  | 78.26    |
| NB     | 75.00    | 74.78     | 82.43  | 78.42    |
| DT     | 61.80    | 74.49     | 46.65  | 57.37    |
| RF     | 74.47    | 75.61     | 79.23  | 77.38    |

# Word2vec
| Models | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 57.92    | 59.59     | 67.21  | 63.17    |
| LR     | 65.67    | 67.86     | 68.52  | 68.19    |
| NB     | 58.10    | 59.77     | 67.21  | 63.27    |
| DT     | 53.70    | 57.09     | 55.41  | 56.24    |
| RF     | 62.68    | 64.86     | 66.56  | 65.70    |

