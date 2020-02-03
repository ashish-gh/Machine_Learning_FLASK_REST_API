# Machine Learning Model with FLASK REST API

![Alt text](https://hackernoon.com/drafts/7967432wy.png)

## Boston housing price prediction
The dataset used in this project comes from the UCI Machine Learning Repository. This data was collected in 1978 and each of the 506 entries represents aggregate information about 14 features of homes from various suburbs located in Boston.

The features can be summarized as follows:

* CRIM: This is the per capita crime rate by town
* ZN: This is the proportion of residential land zoned for lots larger than 25,000 sq.ft.
* INDUS: This is the proportion of non-retail business acres per town.
* CHAS: This is the Charles River dummy variable (this is equal to 1 if tract bounds river; 0 otherwise)
* NOX: This is the nitric oxides concentration (parts per 10 million)
* RM: This is the average number of rooms per dwelling
* AGE: This is the proportion of owner-occupied units built prior to 1940
* DIS: This is the weighted distances to five Boston employment centers
* RAD: This is the index of accessibility to radial highways
* TAX: This is the full-value property-tax rate per $10,000
* PTRATIO: This is the pupil-teacher ratio by town
* B: This is calculated as 1000(Bk — 0.63)², where Bk is the proportion of people of African American descent by town
* LSTAT: This is the percentage lower status of the population
* MEDV: This is the median value of owner-occupied homes in $1000s

# Outline
* [Blogpost](#blogpost)
* [Pre-requisites](#pre-requisites)
* [How to run](#how-to-run)



## BlogPost
For detailed overview, here is the accompanying blog titled: **[Machine Learning Model with FLASK REST API](https://hackernoon.com/machine-learning-w22g322x)**


## Pre-requisites
*  Flask
*  Postman
*  Libraries and Packages


[Flask Installation](https://flask.palletsprojects.com/en/1.1.x/installation/) provides a practical guide for installation of Flask.

For platform-specific instructions, read [here](https://pypi.org/project/Flask/)

[Postman Installation](https://www.getpostman.com/downloads/) provides a practical guide for installation of Postman.



### Installing required packages
After NLTK has been downloaded, install required packages
```
pip install -r requirements.txt
```

## How to run
You can either run Jupyter notebook to go through every process and develop model or use developed model and run application through terminal.

* Jupyter Notebook [![Binder](https://mybinder.org/badge_logo.svg)](https://hackernoon.com/machine-learning-w22g322x)

You can run the [Boston_house_price_prediction.ipynb] (https://github.com/ashish-gh/boston_housing_price/blob/master/Boston_house_price_prediction.ipynb) which also includes step by step instructions.

* Through Terminal
```
python app.py
```

