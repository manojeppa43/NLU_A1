# Sports vs Politics Text Classification 
## Natural Language Understanding – Assignment 01 
### Problem Statement 
The goal of this project is to build a machine learning classifier that reads a 
news text document and classifies it as either: 
1. Sports
2. Politics

I have used Bag of words feature representation and built three classifiers using the following techniques:
1. Multinomial Naive Bayes
2. Logistic Regression
3. Linear Support Vector Machine
### Requirements / Installation section
Make sure you have python and pip installed and then install the required libraries using the following command:
> **pip install pandas scikit-learn fsspec huggingface_hub**

### Repo Structure
1. **preprocessing.ipynb**: Contains code regarding to pre processing of data obtained from (https://huggingface.co/datasets/okite97/news-data)
2. **cleaned_data.csv**: Contains our required data after pre-processing
3. **multinomial_naive_bayes.ipynb**: Contains code related to classifier built using multinomial naive bayes method.
4. **logistic_regression.ipynb**: Contains code related to classifier built using logistic regression method.
5. **svm.ipynb**: Contains code related to classifier built using linear SVM method.
6. **B22AI018_prob4.pdf**: Contains dataset description and detailed analysis of performance of models built using these three methods.
