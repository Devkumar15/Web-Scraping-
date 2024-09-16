# -*- coding: utf-8 -*-
"""NLP_mini_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LQTZIJUje3XyT9OnKjsndtlvLT-eXH9y
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver.get('https://www.amazon.com/your-product-link')

# Scroll down and load more reviews
load_more = driver.find_element(By.CLASS_NAME, 'load-more-button-class')
load_more.click()

# Optionally, sleep to wait for loading
time.sleep(2)

# Now use BeautifulSoup to parse the updated HTML
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# import module
import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \ AppleWebKit/537.36 (KHTML, like Gecko) \ Chrome/90.0.4430.212 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text


def html_code(url):

	# pass the url
	# into getdata function
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	# display html code
	return (soup)

url ="https://www.amazon.in/LG-inches-Ultra-Smart-43UR7500PSC/dp/B0C82ZHYQ8"
# url = "https://www.amazon.in/Columbia-Mens-wind-\resistant-Glove/dp/B0772WVHPS/?_encoding=UTF8&pd_rd\_w=d9RS9&pf_rd_p=3d2ae0df-d986-4d1d-8c95-aa25d2ade606&pf\_rd_r=7MP3ZDYBBV88PYJ7KEMJ&pd_rd_r=550bec4d-5268-41d5-\87cb-8af40554a01e&pd_rd_wg=oy8v8&ref_=pd_gw_cr_cartx&th=1"
soup = html_code(url)
print(soup)
url="https://www.amazon.in/LG-inches-Ultra-Smart-43UR7500PSC/product-reviews/B0C82ZHYQ8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
soup = html_code(url)
print(soup)

def cus_data(soup):
	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	cus_list = []

	for item in soup.find_all("span", class_="a-profile-name"):
		data_str = data_str + item.get_text()
		cus_list.append(data_str)
		data_str = ""
	return cus_list


cus_res = cus_data(soup)
print(cus_res)

def extract_reviews_and_ratings(soup):
    reviews_and_ratings = []

    # Find all the review elements
    review_elements = soup.find_all("div", class_="a-section review aok-relative")
    review_text=[]
    rating=[]
    for review_element in review_elements:
        # Extract the review text
        temp = review_element.find("span", class_="review-text").get_text().strip()
        review_text.append(temp)
        # Extract the rating
        rating_element = review_element.find("i", class_="a-icon-star")
        temp2 = rating_element.get_text().strip()  # This assumes that the rating text is directly within the <i> element
        rating.append(temp2)
        # Append the review and rating to the list
        # reviews_and_ratings.append((review_text, rating))
        x=review_text
        y=rating
    return x,y
x,y = extract_reviews_and_ratings(soup)
for i in range (len(x)):
  print(x[i])
  print(y[i])

def cus_rev(soup):
    data_str = ""
    result = []  # Initialize an empty list
    for item in soup.find_all("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
        data_str = data_str + item.get_text()
        result = data_str.split("\n")
    return result

rev_data = cus_rev(soup)
rev_result = []
for i in rev_data:
    if i == "":
        pass
    else:
        rev_result.append(i)
rev_result

import pandas as pd

# initialise data of lists.
data = {'review': rev_result}

# Create DataFrame
df = pd.DataFrame(data)

# Save the output.
df.to_csv('amazon_review.csv')

"""**Attemp1**"""

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

data = pd.read_csv('AmazonReview.csv')
data.head()

data.info()

data.dropna(inplace=True)

#1,2,3->negative(i.e 0)
data.loc[data['Sentiment']<=3,'Sentiment'] = 0

#4,5->positive(i.e 1)
data.loc[data['Sentiment']>3,'Sentiment'] = 1

stp_words=stopwords.words('english')
def clean_review(review):
  cleanreview=" ".join(word for word in review.
					split() if word not in stp_words)
  return cleanreview

data['Review']=data['Review'].apply(clean_review)

data['Sentiment'].value_counts()

consolidated=' '.join(word for word in data['Review'][data['Sentiment']==0].astype(str))
wordCloud=WordCloud(width=1600,height=800,random_state=21,max_font_size=110)
plt.figure(figsize=(15,10))
plt.imshow(wordCloud.generate(consolidated),interpolation='bilinear')
plt.axis('off')
plt.show()

from google.colab import drive
drive.mount('/content/drive')

consolidated=' '.join(word for word in data['Review'][data['Sentiment']==1].astype(str))
wordCloud=WordCloud(width=1600,height=800,random_state=21,max_font_size=110)
plt.figure(figsize=(15,10))
plt.imshow(wordCloud.generate(consolidated),interpolation='bilinear')
plt.axis('off')
plt.show()

cv = TfidfVectorizer(max_features=2500)
X = cv.fit_transform(data['Review'] ).toarray()

from sklearn.model_selection import train_test_split
x_train ,x_test,y_train,y_test=train_test_split(X,data['Sentiment'],test_size=0.25 ,random_state=42)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

#Model fitting
model.fit(x_train,y_train)

#testing the model
pred=model.predict(x_test)

#model accuracy
accuracy=accuracy_score(y_test,pred)
print(accuracy)

from sklearn import metrics
cm = confusion_matrix(y_test,pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = cm,
											display_labels = [False, True])

cm_display.plot()
plt.show()

"""**Attemp2**"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
import warnings #But we need to hide these warnings
warnings.filterwarnings('ignore')
warnings.filterwarnings("ignore",category=UserWarning)
sns.set_style("whitegrid")
# %matplotlib inline
np.random.seed
data = pd.read_csv('Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv', encoding='utf-8', skiprows=[47,826,901,1105,1308,1348,1389,1511,1573,1636,1698,1761,2084])

data.info()

data.hist(bins=50, figsize=(10,8))
plt.show()

sns.countplot(data['reviews.rating'])
plt.xlabel('Rating Count')

sns.countplot(data['reviews.numHelpful'])
plt.xlabel('Rating Count')
sentiment_score = {1: 0,
                   2: 0,
                   3: 0,
                   4: 0,
                   5: 1}
sentiment = {0: 'NEGATIVE',
             1: 'POSITIVE'}

data['sentiment_score'] =data['reviews.rating'].map(sentiment_score)
data['sentiment'] = data['sentiment_score'].map(sentiment_score)

labels = ['POSITIVE', 'NEGATIVE']
colors = ['#189AB4', '#D4F1F4']
plt.pie(data['sentiment_score'].value_counts(), autopct='%0.2f%%',colors=colors)

plt.title('Distribution of sentiment', size=14, y=-0.01)
plt.legend(labels, ncol=2, loc=9)
plt.show()

all_words =pd.Series(' '.join(str(data['reviews.text']).split()))
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
wordcloud = WordCloud(width = 1000, height = 500).generate(' '.join(all_words))

plt.figure(figsize=(15,8))

plt.imshow(wordcloud)
plt.title("Most used words in all reviews", size=16)

plt.axis("off")
plt.show()