# CherryPicker-backend

## This repository contains the Scrapers for Event Venue Rental Websites. Scrapers will be run by AWS Lambda and cloudwatch which will then transfer data to MongoDB atlas.

## Libraries used:

- Requests
- BeautifulSoup

## How to start development:

### (1) Install Pip

### (2) Install PipEnv as package manager

- Recommended to use PipEnv to manage python packages. PipEnv is just like NPM. It helps you to download the dependencies required for the python project. See more in this [link:](https://medium.com/@krishnaregmi/pipenv-vs-virtualenv-vs-conda-environment-3dde3f6869ed)
- To use pipenv, you need to install pip.
- Next, you create a new environment by using the command `pip install pipenv` This will look for a pipenv file, if it doesn’t exist, it will create a new environment and activate it.
- If an error occur, try `pip install pipenv==2018.11.26`
- To activate it `pipenv shell`
- To install a new package do `pipenv install <packageName>` so that pipenv will add the package to the pipenv file called Pipfile

### (2.1) Subsequent runs after the above configuration

- Activate pipenv by using the command `pipenv shell`

### (3) Use the Requirements.txt

- To download all the required dependencies, simply run `pipenv install -r requirements.txt`
- Whenever you download a new library, add it to requirements.txt by doing `pip freeze > requirements.txt`

### (4) Connecting to MongoDB Atlas

- Please obtain .env file from @ooihuiying

### (5) Triggering Scrapers manually

- (Without connecting to database-MongoAtlas) Please make sure that you are on the same directory level as Scrapers, Data, Connect-Database folders before running the command `python Scrapers/<SCRAPERNAME>.py`
- (Saving data to database-MongoAtlas) Run `bash run.sh`

## Scrapers created

- TagVenue
- Venuerific
- VenuExplorer
- Huone

## Helpful links to get started on scraping and pipenv

- https://github.com/pypa/pipenv/issues/4296
- https://medium.com/@krishnaregmi/pipenv-vs-virtualenv-vs-conda-environment-3dde3f6869ed
- https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184
- https://medium.com/@DrGabrielHarris/python-how-create-requirements-txt-using-pipenv-2c22bbb533af
- https://pypi.org/project/python-dotenv/
- https://medium.com/@ooiyueying/serverless-python-web-scraping-on-schedule-using-ec2-lambda-ssm-and-cloudwatch-on-aws-and-197d30331261
