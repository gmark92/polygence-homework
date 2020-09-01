# polygence-homework
Polygence technical assignment

## Description
In this technical assignment I had to reliase a RESTful API of an imaginary spending tracker.  
For achiving this task I used Django and django-restframework.  
For storing the data I used a Postgres database.  
For managing the dependencies and running the webapplication and database I used docker and docker-compose.  

### Running
To run the application you need **docker**, **docker-compose**.

1. In the projects root folder run  
    ```docker-compose up```  
2. Migrate (First run only)  
    a, Enter the running container  
    ```docker exec -it <container_id> bash```  
    You can find the container_id with ```docker ps```  
    b, Run the Django migrations  
    ```python manage.py migrate```  
3. Example endpoint calls  
    Add a new spending (POST)  
    ```http://localhost:8000/api/me/spendings/```  
    JSON in the body  
    ```
    {
        "date" : "2020-09-01T20:11",  
	    "amount" : "3000",  
	    "currency" : "GBP",  
	    "description" : "SOME TEXT2"  
    }
    ``` 
    List all the spendings (GET)  
    ```http://localhost:8000/api/me/spendings/```  
    Order by amount (GET)  
    ```http://localhost:8000/api/me/spendings/?ordering=amount```  
    List all the spendings filtered by the currency (GET)  
    ```http://localhost:8000/api/me/spendings/?currency=HUF```  
    Delete a spending (DEL)  
    ```http://localhost:8000/api/me/spendings/1/```  
    Update a spending (PATCH)  
    ```http://localhost:8000/api/me/spendings/1/```  
    JSON in the body  
    ```
    {  
	    "amount" : "4000"  
    }
    ``` 
    