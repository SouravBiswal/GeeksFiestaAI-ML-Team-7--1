## GEEKFESTIA-2021

#### This repository contains a Data Analysis on a weather dataset created using Jupyter Notebook.
#### The weather dataset contains the following columns:- **year, month, day, hour, PM2.5(Particulate matter), temperature, pressure, rain, wind_direction, wind_speed.**  <p>
  <em> Pariculate matter :- PM stands for particulate matter (also called particle pollution): the term for a mixture of solid particles and liquid droplets found in the                             air. Some particles, such as dust, dirt, soot, or smoke, are large or dark enough to be seen with the naked eye. <p>
   Temperature :- Temperature is a degree of hotness or coldness the can be measured using a thermometer. <p>
   Pressure:- Atmospheric or air pressure is the force per unit of area exerted on the Earth’s surface by the weight of the air above the surface. <p>
   Rain :- The condensed moisture of the atmosphere falling visibly in separate drops. <p>
   Wind direction :- Wind direction is defined as the direction the wind is coming from. If you stand so that the wind is blowing directly into your face, the direction                      you are facing names the wind.For general purposes, the wind direction is reported to eight compass points: N, NE, E, SE, S, SW, W, NW. <p>
   Wind speed :- In meteorology, wind speed, or wind flow speed, is a fundamental atmospheric quantity caused by air moving from high to low pressure, usually due to                      changes in temperature. <p> </em>
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
   * Scikit-Learn 
   <!--- * Matplotlib --->
   
#### 2. Reading the dataset : <p>
        pd.read_csv('train.csv')

#### 3. Cleaning and Processing the Dataset : <p>
   We first convert all the numeric data from object data-type to float/int data-type, then we remove all the null values so that we can perform our analysis in the later stage. As we're given the date and time spread across four different columns, we tried to simplify them into a single column using this code. <p>
      
           df['Date'] = pd.to_datetime(df.day.astype(str) + "-" + df.month.astype(str) + "-" + df.year.astype(str) + " " + df.hour.astype(str) + ":00:00") <p>
           df.drop(columns=['year', 'month', 'day', 'hour'], inplace = True)
             
 Also we found some anomalies and corrected them after analysing the neighbours of such cells manually (we've put a comment on those lines so the reader can identify them easily).
After performing the cleaning, we've exported the given dataset to a fresh dataset as Clean_Data.csv so that we can perform our analysis productively.             
          
  
  

