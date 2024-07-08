# Sentiment-Analyzer-Movie Review Analyzer
Sentiment-Analyzer-Web_Application using Flask

The web application performs Sentiment analysis of the review of the movie given by the user as input and gives the output as positive or negative based on the sentiment of the input.

# Data Collection
Publicly available data - IMDB Movie review dataset is considered for this project. The data contains 50k real time reviews of a movie. The table contains two columns - text and sentiment. 'text' contains the movie review and 'sentiment' consists of 'positive' or 'negative'

# Data Cleaning (Text pre-processing)
The dataset needs to be cleaned befotre it is used for model training. Following operations are performed on the dataset by using various libraries of Python like numpy, pandas,etc.
1. Removal of HTML tags
2. Removal of stopwords (and, or, is, etc.)
3. Removal of punctuations and special charecters
4. Stemming - writing the word in it's basic form.
5. Converting all in lower case
Once, text pre-processing is done, we have clean data to pass into the algorithm.
Vectorization is performed using BOW(Bag Of Words) on 'sentiment' column i.e, converting textual data into numerical values so that it is understandable to algorithm. 1 --> positive and 2 --> negative

# Model Training
10k reviews are extracted from the cleaned dataset from previous step and is used for Sentiment analyzer model training further.The dataset is divided into 2 parts - 8k dataset as Train ( for Training the model) and 2k datasets as Test ( to test the model).
Python libraries like nltk - Natural Language Tool Kit and sci-kit learn libraries are used to train the model.
Algorithm used it NAIVE-BAYE'S ALGORITHM (Probabilistic Approach). The model is trained under 3 different classifiers of Naived Baye's algorithm such as GaussianNB, MultinomialNB, and BernoulliNB. Next, accuracy of the model is calculated for all 3 classifications. It is found that BernoulliNB model is more accurate with the accuracy percentage of 85.82%.

# Deployment
The web application is deployed using Flask (Python framework), front end of the web page is designed using HTML and CSS.

# Hosting the web application on AWS Cloud
The Flask application which is on local host is hosted publicly on AWS Cloud using AWS EC2 instance.

# Data Visualization
The data entered by the user is visualized under various parameters visualization graphs and useful insights are drawn from the same using Excel as Data Visualization platform.

# Future Enhancement
Perform real time data visualization of reviews entered by user, show the results on the deployed page and draw overall conclusion regarding public review on the movie which can be used by movie makers and users. 





