# Rental real estate market analysis

I have chosen to undertake this project on the rental real estate market in Gdansk due to my keen <br> 
interest in the subject. This is an exciting time to conduct this analysis, as during data collection stage <br>
there was a high degree of fluctuation in rental prices due to the large student population in the city and <br> 
after COVID market release. 


### Technologies: 

- Python:
  - NumPy
  - Pandas
  - Scikit-learn
  - Tensorflow
  - Matplotlib
  - Flask
- SQL
- Tableau
- Excel

## Project Overall:

The objective of this project is to conduct an analysis of the rental real estate market in <br> 
Gdansk, using the Selenium package to collect data from the popular classifieds portal OLX.

In the first stage of the project, I am using Selenium to scrape rental property data in Gdansk <br>
from OLX, such as location, area, price, number of rooms, etc. In the second stage, this data is <br> 
stored and processed using Python packages such as Pandas, Numpy and Scikit-learn to explore and <br> 
analyze the data.

The end goal of this project is to gain insights into the rental real estate market in local market and <br>
create visualizations to better understand the trends and patterns in the data. Through this analysis, <br>
I hope to identify factors that influence rental prices and ultimately provide valuable insights to <br> 
individuals and businesses operating in the rental real estate market in Gdansk.



## Needs of this project and Author: 

* **Data exploration/descriptive statistics**: This project requires exploring and summarizing the rental real estate market data in Gdansk using descriptive statistics. The data exploration will provide an understanding of the characteristics of the data and identify any trends, patterns, or outliers.

* **Data processing/cleaning**: The collected data will require processing and cleaning to ensure the quality and consistency of the data. The data processing will involve data transformation, merging, and aggregation. The data cleaning will involve dealing with missing or erroneous data and outliers.

* **Statistical modeling**: This project requires building a statistical model to identify factors that influence rental prices in Gdansk. The statistical model will help to quantify the relationship between the variables and enable us to make predictions about future rental prices.

* **Writeup/reporting**: The results of the project will be presented in a writeup/reporting format. The writeup will include an overview of the project, data collection and processing methods, statistical modeling approach, results, and conclusions. The reporting will include visualizations such as charts, graphs, and tables to aid in communicating the findings.

* **Feature engineering**: In order to improve the accuracy of the statistical models used in this project, I'll need to engineer new features based on the existing data. This may involve creating new variables, combining existing variables, or transforming existing variables to better capture the relationship between them and the rental prices.

* **Model validation and selection**: To ensure that the statistical model is reliable and accurate, I'll need to validate it using statistical techniques such as cross-validation and hypothesis testing. Additionally, I'll need to select the best performing model based on evaluation metrics such as mean squared error, root mean squared error, and R-squared.

* **Interpretation and communication of results**: Finally, I will need to interpret the results of the analysis and communicate them effectively to a wider audience. This will involve creating visualizations and reports that are clear, concise, and easy to understand, as well as presenting our findings to stakeholders in a way that is engaging and informative.


##  1 Data collection October 22
#### Method: Web Scrapping <br> Tool: Selenium library 

### Metadata
The following metadata were collected for each rental offer:

- building-type: Type of the building, with the following options: <br>
    - 0: Pozostałe 
    - 1: Dom wolnostojący
    - 2: Kamienica
    - 3: Szeregowiec
    - 4: Blok
    - 5: Apartamentowiec
    - 6: Loft
    - 7: Suterena
- furnished: Indicates whether the rental unit is furnished or not, with values of true or false.
- level: Floor number of the rental unit within the building, with a range of 0-10, with 11 indicating that the floor number is greater than 10, and null indicating that no information was available.
- link: URL link to the offer on olx.pl.
- listing_no: Unique identification number for the listing.
- negotiable: Indicates whether the rental price is negotiable or not, with values of true or false.
- private: Indicates whether the owner of the rental unit is a private person or not, with values of true or false.
- publish-date: Date when the offer was published on olx.pl, in the format of "YYYY-MM-DD".
- rent: Rental price for the rental unit.
- rent-extra: Additional costs associated with renting the unit, such as utilities or maintenance fees.
- rent-full: Total rental price (rent + rent-extra).
- rooms: Number of rooms in the rental unit, with values ranging from 1-3, and 4 indicating that the unit has 4 or more rooms.
- surface: Total surface area of the rental unit, in square meters.
- title: Title of the rental offer.
- collection_set: Indicates the date when the rental data was collected, with the following options:
    - 1: sep3
    - 2: sep11
    - 3: sep19
    - 4: sep26
    - 5: oct3
    - 6: oct11
    - 7: oct20
    - 8: oct27
    - 9: nov3.


## 2) Data Cleaning & Database Creation - October 22
The next step in the project is to clean and process the data collected from olx.pl, and create a database to store the cleaned data.

### Data Cleaning
Data cleaning involves identifying and handling missing values, removing duplicates, dealing with outliers, and correcting inconsistencies in the data. In this project, the collected rental offer data may have incomplete or inconsistent information, such as missing values for the number of rooms or area, or conflicting information about the location or property type. These issues need to be addressed before the data can be analyzed.

- Handling Missing Values - check for missing values in each column and decide on the appropriate action to handle them. For example, if the percentage of missing values in a column is low, I may remove the rows with missing values. If the percentage is high, I may impute the missing values using appropriate methods such as mean, median, or mode.
- Removing Duplicates - check for duplicate rows in the data and remove them if necessary.
- Handling Outliers - identify outliers in the data and decide on the appropriate action to handle them. For example, I may remove the rows with extreme values or replace them with the nearest non-outlying value.
- Correcting Inconsistencies - identify inconsistencies in the data, such as conflicting information about the location or property type, and correct them manually or programmatically.

### Database Creation
Once the data has been cleaned, it needs to be stored in a database for further analysis. For this project, I will use MySQL as the database management system to create a database to store the cleaned data.

To create the database, I will follow the following steps:
- Designing the Schema - design a schema that specifies the structure of the tables and the relationships between them. The schema will take into account the types of data collected from olx.pl and the analytical goals of the project.
- Creating the Tables: Using the schema - create the tables in the database using SQL statements. I will also define constraints and indexes on the tables to ensure data integrity and improve query performance.
- Importing the Cleaned Data - import the cleaned data into the corresponding tables in the database using Python and the MySQL connector library.
- Verifying the Data - perform basic checks to verify that the data has been imported correctly into the database tables.


## 3) Analysis Stage 1 - November 22
### Method: Removing duplicate and outliers, getting to know the data and pre-analysis of rental opportunities.
<br> Tools: Python (pandas, numpy) 

The "Removing Duplicate and Outliers, Getting to Know the Data" stage of data pre-processing is crucial to ensuring 
the accuracy and reliability of the data used in further analysis. The goal of this stage is to remove any duplicate
data points and outlier data points, and to explore the dataset to gain insights into its characteristics. Additionally,
in pre-analysis stage i identified periods of time in witch a rental could have occurred but did not.

The tools used in this stage include Python, specifically the libraries Pandas and Numpy. Pandas is a data manipulation 
library that provides easy-to-use data structures and data analysis tools, while Numpy is a library for numerical 
computing in Python.

Steps:
1) Load the dataset into a Pandas DataFrame using the appropriate function depending on the format of your data.
2) Check the shape of the dataset using the shape attribute of the DataFrame.
3) Check for duplicates using the duplicated method of the DataFrame, and remove duplicate rows using the drop_duplicates
method.
4) Check for outliers in each column of the dataset using statistical methods from Numpy or Pandas.
5) Remove outliers by filtering the DataFrame based on a threshold value for each column.
6) Identify any gaps in the rental periods where a rental should have occurred but did not, and mark these periods 
as possible rental opportunities.
7) Explore the dataset further to gain insights into its characteristics, such as the distribution of values in 
each column and the relationships between columns.

<i> Conclusion:
Removing duplicate and outlier data points and exploring the dataset can help to ensure the accuracy and reliability 
of the data used in further analysis. Additionally, identifying possible rental opportunities can provide valuable 
insights for a business. This stage of data pre-processing is critical to the success of any data analysis project, 
and Python libraries such as Pandas and Numpy are powerful tools that can simplify the process.</i>


## 4) Analysis Stage 2 - April to May 23
### in progress... 
#### Method: Random Forest Algorithm. 

Description: <br>

## 5) Visualization & Conclusion May 23
### in progress 
#### Method: Removing duplicate <br> Tool: Selenium library 

Description: <br>



# Results of project

1. This project will be finalized with report of my [findings - NO FINDINGS YET](https://google.com)

2. Raw Data is being kept [here - NO RAW DATA YET](https://google.com) within this repo.
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)


## Contact
* [Github](https://github.com/Mateusz-Matejko)
* [LinkedIn](https://www.linkedin.com/mateusz7matejko)
* Feel free to contact me with any questions of any analysis ideas!
