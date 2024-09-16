# Amazon Product Review Analysis using Web Scraping and NLP

## Overview
This project focuses on scraping Amazon product reviews, extracting and processing customer feedback, and applying Natural Language Processing (NLP) techniques to analyze the sentiment of these reviews. The process involves:

Scraping reviews from Amazon using Selenium and BeautifulSoup.
Cleaning and processing the data.
Performing sentiment analysis using NLP techniques.
Visualizing the key insights using Matplotlib and WordCloud.
Training a machine learning model for sentiment classification.

## Features

### Web Scraping with Selenium & BeautifulSoup:
Utilizes Selenium to navigate dynamic Amazon web pages and BeautifulSoup for parsing HTML.
Extracts customer names, reviews, and ratings from Amazon product pages.

### Sentiment Analysis:
Data cleaning and preprocessing using NLTK.
Sentiment classification based on customer reviews (1-3 stars = Negative, 4-5 stars = Positive).
Uses TfidfVectorizer to convert text data into numerical form.

### Data Visualization:
Generates word clouds of the most frequent terms in positive and negative reviews.
Visualizes the distribution of customer sentiments.

### Machine Learning:
Logistic regression model to classify customer reviews into positive or negative sentiment.
Performance evaluation using accuracy scores and confusion matrices.

## Installation
### Prerequisites

#### Python 3.x
### Install the required libraries using the following:
#### pip install -r requirements.txt
### Required Libraries

Selenium: For web scraping dynamic content.
BeautifulSoup: For parsing the HTML content.
requests: To fetch webpage content.
nltk: For text preprocessing.
matplotlib: For visualization.
wordcloud: For generating word clouds.
pandas: For data manipulation and analysis.
scikit-learn: For machine learning models.

### Setting up Selenium
To use Selenium for scraping, you will need the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome):

Download the Chrome WebDriver.
Replace the /path/to/chromedriver in the code with the actual path to your ChromeDriver executable.

## How to Run the Project

Scraping Reviews:
Update the product URL in the code to the Amazon product page of your choice.
Run the scraping section to gather reviews, ratings, and customer names.
Save the scraped data into a CSV file (amazon_review.csv).

Data Cleaning and Preprocessing:
Preprocess the reviews by removing stopwords and performing other text cleaning steps.

Sentiment Analysis:
Use TfidfVectorizer to convert reviews into numerical form.
Classify the sentiment (positive or negative) based on star ratings.

Model Training:
Train a logistic regression model on the preprocessed review data.
Test the model’s accuracy on a separate test set.

Visualization:
Generate word clouds to visualize frequently used words in positive and negative reviews.
Plot graphs showing sentiment distribution and confusion matrices for model evaluation.

## Ouput Example:

![image](https://github.com/user-attachments/assets/5894c28d-700c-4c6a-8fb3-097ac96b076a)

![image](https://github.com/user-attachments/assets/d5917eba-14fd-4cc9-b99e-f78a596dbabd)

![image](https://github.com/user-attachments/assets/d88831e1-d824-4d92-8ac7-1b731e7ec1f1)


## Future Enhancements
Advanced NLP: Explore deeper NLP techniques, such as using transformers (BERT, GPT) for more accurate sentiment analysis.
Data Expansion: Scrape more product categories and increase the dataset for better model generalization.
Additional Features: Include more features such as review length, number of helpful votes, etc., to enhance sentiment predictions.
