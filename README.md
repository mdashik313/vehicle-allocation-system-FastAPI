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

I will use MongoDB Atlas, a cloud database service for MongoDB to host the database. </br>
Steps to setup MongoDB Atlas in the project:
1. Register for Atlas account, deploy a free tier cluster, set up a user, and an IP address.
2. 
For deploying the application, I will use <mark> Heroku </mark> as the hosting platform and <mark> MongoDB Atlas </mark> for the database service.

Heroku provides a seamless and scalable environment for deploying applications with built-in support for integration and easy scaling.

MongoDB Atlas, a cloud database service, offers global distribution, ensuring high availability and scalability along with its monitoring and automated backups features.


##
