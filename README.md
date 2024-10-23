<h1> Simple Vehicle Allocation System using FastAPI and MongoDB. </h1>

## Running the Application
Before starting you have [Python](https://www.python.org/downloads/), [MongoDB](https://www.mongodb.com/docs/manual/installation/), [pip and virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) be installed and MongoDB database server running.

1. Clone the repository

```
git clone "https://github.com/mdashik313/vehicle-allocation-system-FastAPI.git"
```
2. Navigate to the project folder
```
cd vehicle-allocation-system-FastAPI
```
3. Create virtual environment
```
python3 -m venv .venv
```
4. Activate virtual environment

For Windows(shell):
```
source venv/Scripts/activate
```
For Linux:
```
. .venv/bin/activate
```
5. Install project dependencies
```
pip install -r requirements.txt
```
6. Run the application
```
uvicorn main:app --reload
```
The message "Database configured and application running successfull" will appear if everything is right.

## Deployment
### MongoDB Atlas
I will use <mark> MongoDB Atlas </mark>, a cloud database service for MongoDB to host the database. </br>
Steps to setup MongoDB Atlas in the project:
1. Register for Atlas account, deploy a free tier cluster, set up a user, and an IP address.
2. Grab the database connection URL from the cluster.
3. In the src/database.py file in porject directory set MONGO_DETAILS = "connection_URL"
4. Restart Uvicorn server and test each route from the interactive documentation at http://localhost:8000/docs

### Heroku
For deploying the application, I will use <mark> Heroku </mark> as the hosting platform.
Steps to setup Heroku in the project:
1. Sign up for a Heroku account and install the Heroku CLI.
2. Add a file named Procfile to project's root directory and paste the following line
```
web: uvicorn app.server.app:app --host 0.0.0.0 --port=$PORT
```
3. Initialize a git repository in project root if not initialized yet
```
git init
git add .
git commit -m "Initialization"
```
4. Create a new app on Heroku:
```
heroku create
```
5. Push code to Heroku and check an instance of the application is running
```
git push heroku master
heroku ps:scale web=1
```
6. Run on broweser
```
heroku open
```

## Maintainance
To maintain the project effectively, I will use Git and GitHub for version control, ensuring a clear history of changes, with feature branches and pull requests for collaboration and review. Testing will be prioritized through unit and integration tests with tools like pytest to maintain high code quality. For database performance, regular backups and index optimization will be implemented. The application will be containerized with Docker. Additionally, clear code documentation, a detailed README, and Swagger-based API docs will ensure easy understanding and extension of the project.
