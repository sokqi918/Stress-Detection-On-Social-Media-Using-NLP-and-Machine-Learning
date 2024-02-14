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

# Feature Extraction Techniques
Logistic Regression with TF-IDF are outperforming among all models in term of accuracy, which achieved at 76.23%. Naive Bayes is well performed in BoW and TF-IDF as well, achieved F1-Score of 79.76% and 78.42% respectively. 

*Traditional Machine Learning Models*  

**1. BoW** 
| Models | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 73.77    | 77.52     | 73.80  | 75.61    |
| LR     | 75.70    | **78.69**     | 76.68  | 77.67    |
| NB     | **76.06**    | 74.65     | **85.62**  | **79.76**    |
| DT     | 62.15    | 68.56     | 57.83  | 62.74    |
| RF     | 73.24    | 73.61     | 80.19  | 76.76    |

![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Pictures/BoW.png)

**2. TF-IDF** 
| Models | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 75.70    | **79.26**     | 75.72  | 77.45    |
| LR     | **76.23**    | 78.90     | 77.64  | 78.26    |
| NB     | 75.00    | 74.78     | **82.43**  | **78.42**    |
| DT     | 61.80    | 74.49     | 46.65  | 57.37    |
| RF     | 74.47    | 75.61     | 79.23  | 77.38    |

![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Pictures/TFIDF.png)

**3. Word2Vec**
| Models | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 57.92    | 59.59     | 67.21  | 63.17    |
| LR     | 65.67    | 67.86     | 68.52  | 68.19    |
| NB     | 58.10    | 59.77     | 67.21  | 63.27    |
| DT     | 53.70    | 57.09     | 55.41  | 56.24    |
| RF     | 62.68    | 64.86     | 66.56  | 65.70    |

![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Pictures/Word2vec.png)

*Deep Learning Models*

| Feature_Extraction | Models | Accuracy | Precision | Recall | F1-Score |
|--------------------|--------|----------|-----------|--------|----------|
| GloVe              | LSTM   | 73.66    | 79.87     | 66.84  | 72.78    |
| GloVe              | CNN    | 73.52    | 71.93     | 81.55  | 76.44    |

![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Pictures/glove.png)

# Deployment
We used Streamlit to create a simple Website, you can find the coding in [here](https://github.com/sokqi918/Stress-Detection-On-Social-Media/tree/main/Deployment).
