# Workable ETL Job

Python script and dag to deploy job with k8s airflow operator

First python script and job I ever wrote, even before I started learning Python. Used the basic knowledge I had in C to adapt different scripts from the web to my use case.

In order to use the data from talent acquisition process from Workable Platform, we had to retrieve it through Workable API and load it into BigQuery where it was then transformed with SQL. 
So first we make a query in our tables to find out what was the most up-to-date data and we only extract data created or updated after that. 
