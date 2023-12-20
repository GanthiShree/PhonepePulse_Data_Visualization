![image](https://github.com/swathinagarajan1996/PhonepePulse_Data_Visualization/assets/127007232/fab1700a-8e35-4334-9bb3-aea43080bc1e)

***Data Visualization and Exploration
A User-Friendly Tool Using Streamlit and Plotly***

The Phonepe pulse Github repository contains a large amount of data related to
various metrics and statistics. The goal is to extract this data and process it to obtain
insights and information that can be visualized in a user-friendly manner.

**Libraries/Modules needed required**
1. Plotly - (To plot and visualize the data)
2. Pandas - (To Create a DataFrame with the scraped data)
3. MySQL server- (To store and retrieve the data)
4. Streamlit - (To Create Graphical user Interface)
5. json - (To load the json files)
6. git.repo.base - (To clone the GitHub repository
7. PIL - The Python Imaging Library, used for opening, manipulating, and saving many different image file formats.

## Problem Statement
  The Phonepe Pulse Github repository houses a wealth of data, and our challenge is to make it accessible and comprehensible. Our solution involves cloning the repository, transforming the data, storing it in a MySQL database, and building a dynamic geo visualization dashboard using Streamlit and Plotly.

## Approach

### Data Extraction:

1. Clone the Github repository using scripting to fetch data from the Phonepe Pulse repository.
2. Store the data in a suitable format such as CSV or JSON.

### Data Transformation:

1. Use Python and Pandas to manipulate and pre-process the data.
2. Handle cleaning, missing values, and transform the data into a suitable format for analysis and visualization.

### Database Insertion:

1. Utilize "mysql-connector-python" to connect to a MySQL database.
2. Insert the transformed data into the database using SQL commands.

### Dashboard Creation:

1. Use Streamlit and Plotly to create an interactive and visually appealing dashboard.
2. Implement Plotly's built-in geo map functions to display data on a map.
3. Incorporate multiple dropdown options for users to select different facts and figures.

### Data Retrieval:

1. Use "mysql-connector-python" to connect to the MySQL database.
2. Fetch the data into a Pandas dataframe to dynamically update the dashboard.

### Deployment:

1. Ensure the solution is secure, efficient, and user-friendly.
2. Thoroughly test the solution and deploy the dashboard publicly for user accessibility.

## Results
  The project delivers a live geo visualization dashboard that provides insights from the Phonepe Pulse Github repository. With at least 10 dropdown options, users can select different facts and figures. The data is stored in a MySQL database for efficient retrieval, and the dashboard dynamically updates to reflect the latest data. Accessible from a web browser, the dashboard offers valuable insights for data analysis and decision-making.

## Learning Outcomes

### Data Extraction and Processing:

- Use Github cloning to extract data and pre-process it with Python and Pandas.

### Database Management:

- Employ a relational database (MySQL) for efficient data storage and retrieval.

### Visualization and Dashboard Creation:

- Create interactive dashboards with Streamlit and Plotly for data visualization.

### Geo Visualization:

- Utilize Plotly's geo map functions to display data on a map.

### Dynamic Updating:

- Develop a dashboard that dynamically updates based on the latest data in a database.

### Project Development and Deployment:

- Learn comprehensive solution development, from data extraction to dashboard deployment.
- Test and deploy the solution to ensure security, efficiency, and user-friendliness.

## Dataset

Dataset Link: [Data Link](https://github.com/PhonePe/pulse#readme)

## Inspired From: [PhonePe Pulse](https://www.phonepe.com/pulse/explore/transaction/2022/4/)

## Contribution Guidelines

Contributions to this project are highly encouraged. If you come across any challenges or have ideas for enhancements, we invite you to submit a pull request. Your input is valuable to us, and we appreciate your contributions.
