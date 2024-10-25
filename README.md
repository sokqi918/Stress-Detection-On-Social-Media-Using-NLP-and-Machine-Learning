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

# Data Collection & Data Understanding
The dataset was collected from Kaggle, which consist of 7 features with 2838 rows. Before we start to do data cleansing, we would like to understand our dataset. Figure 2 showed the meaning for each column. Since we want to identify if the content is stressful or not, the column of “label” is our target variable in this case. 1488 users are identified as stress, while 1350 users are identified as non-stress. The target variable is quite balanced.

![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media-Using-NLP-and-Machine-Learning/blob/main/Pictures/data%20description.jpg)

# Data Cleaning
Data cleaning and preprocessing are essential steps in the data preparation process for NLP tasks because noisy data will affect the performance of models. Before we preprocess the data, we will need to check if there is any duplicated or missing data in our dataset. Besides that, text will be pre-processed by using NLP techniques such as stop words removal, punctuation, and perform tokenization and word normalization. The following are some methods for text data:

**i.	Stop words removal**
Stop word removal is a Natural Language Processing (NLP) technique where common words like “the”, “are”, “is” and “and” are removed from the text data to reduce noise and focus on meaningful words. By removing stop words, the focus shifts to more informative and contextually relevant words in the text.

**ii.	Lemmatization**
Lemmatization is an essential NLP technique designed to simplify words to their base or root form. Its objective is to standardize words to their common base, aiding in the reduction of inflected forms and facilitating analysis. Unlike stemming, lemmatization typically transforms words to their root form, preserving the meaningful and interpretable meaning of the words. This distinction from stemming is significant, as lemmatization ensures that words maintain their semantic integrity, avoiding potential confusion that may arise from the more aggressive nature of stemming.

**iii.	Tokenization**
Tokenization involves breaking down the text into tokens, which are individual words. During this step, the text is segmented based on both whitespace and punctuation. For instance, the phrase "It is a good day!" will be broken up into the phrases "it," "is," "a," "good", "day," and "!"

**iv.	Punctuation marks removal**
The elimination of punctuation marks, including periods, commas, question marks, quote marks, colons, semicolons, and other symbols, is accomplished using NLP approaches.

*World Cloud After Data Preprocessing*
![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media-Using-NLP-and-Machine-Learning/blob/main/Pictures/World%20Cloud%20After%20Data%20Preprocessing.jpg)

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
**4. GloVe**  
| Feature_Extraction | Models | Accuracy | Precision | Recall | F1-Score |
|--------------------|--------|----------|-----------|--------|----------|
| GloVe              | LSTM   | 73.66    | 79.87     | 66.84  | 72.78    |
| GloVe              | CNN    | 73.52    | 71.93     | 81.55  | 76.44    |

![Updated Image](https://github.com/sokqi918/Stress-Detection-On-Social-Media/blob/main/Pictures/glove.png)

# Deployment
We used Streamlit to create a simple Website, you can find the coding in [here](https://github.com/sokqi918/Stress-Detection-On-Social-Media/tree/main/Deployment).
