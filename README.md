## GEEKFESTIA-2021

This repository contains a Data Analysis on a weather dataset created using Jypter Notebook.
The weather dataset contains the following columns:- **year, month, day, hour, PM2.5(Particulate matter), temperature, pressure, rain, wind_direction, wind_speed.**


#### Exploratory Data Analysis is an approach to analyze data, to summarize the main characteristics of data, and better understand the data set. It also allows us to quickly interpret the data and adjust different variables to see their effect. The three main steps to get a perfect EDA are :-
* Extracting/Downloading the data from an authorized source.
* Cleaning and processing the data 
* Performing data visualization on the cleaned data set.

#### We are going to analyze the Weather data set. <p>
Our main aim is to perform data cleaning, data normalizing, testing the hypothesis, and deriving appropriate insights.

#### 1. Importing the necessary libraries :<p>
   This project is done using the following libraries :-
   * Pandas
   * Numpy
   <!--- * Matplotlib
   * Scikit-Learn --->
   
#### 2. Reading the dataset : <p>
        pd.read_csv('train.csv')

#### 3. Cleaning and Processing the Dataset : <p>
   We first convert all the numeric data from object data-type to float/int data-type, then we remove all the null values so that we can perform our analysis in the later stage. As we're given the date and time spread across four different columns, we tried to simplify them into a single column using this code <p>
          ` df['Date'] = pd.to_datetime(df.day.astype(str) + "-" + df.month.astype(str) + "-" + df.year.astype(str) + " " + df.hour.astype(str) + ":00:00")` <p>
          ` df.drop(columns=['year', 'month', 'day', 'hour'], inplace = True)`
  
  

