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