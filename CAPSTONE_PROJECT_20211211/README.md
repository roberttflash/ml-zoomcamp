# Objective
For this capstone project, I want to create the model to predict whether the blood donators donated their blood on March 2007.
The dataset used for training was taken from https://www.openml.org/d/1464 and I use two different methods for this as comparison, 
using decision trees and XGBoost. After tuned the parameters for both methods, XGBoost came up with the highest auc score. 
Therefore I decided to use it as the main model for this project.
For the last couple of days, I didn't have time to explore and learn even more about machine learning and its concepts, 
so I am so certain that there are so many flaws on my analysis and methods. Please give me some feedbacks regarding this project and hopefully 
I could improve my knowledge and make a better model next time. Thank you very much for all of you who evaluate my project.

### Attribute description   
1. recency - months since last donation 
2. frequency - total number of donation 
3. total_donated - total blood donated in c.c. 
4. months_since_beginning - months since first donation
5. class: a binary variable representing whether he/she donated blood in March 2007 (1 stand for donating blood; 0 stands for not donating blood).

## How to Install Dependencies Using pipenv
Make sure you have pipenv installed on your local machine. If not, you can install it first using this command:
```cmd
pip install pipenv
```
After that, install the dependencies required for this model to work using this command:
```cmd
pipenv install numpy pandas scikit-learn==0.24.1 flask xgboost==1.5.0 gunicorn
```
It automatically created Pipfile and Pipfile.lock. Wait until it finish installing the dependencies.

Next, run the virtual environment using ```pipenv shell ``` and type this command to run the app using gunicorn:
```cmd
gunicorn --bind 0.0.0.0:9698 pred:app
```
Now you can hit the app using this command:
```python
donator = {"recency": 1,
  "frequency": 16,
  "total_donated": 4000,
  "months_since_beginning": 35}
 
import requests
url = 'http://localhost:9698/predict'
response = requests.post(url, json=donator)
result = response.json()
result
```
If success, the app will return this response:
```cmd
{'donating_probability': 0.8267529010772705, 'is_donating': True}
```


## How to Deploy in localhost
For running the image locally, make sure you edit the entrypoint to this one:
```Dockerfile
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:<port>", "score:app"]
```

And then build the image using this code below in the root folder:
```cmd
docker build -t <image_name>:<version> .
```

Then run the docker using this command:
```cmd
docker run -it --rm -p <host_port>:<container_port> zoomcamp-capstone:latest
```

## How to Deploy to Heroku
I followed the awesome tutorial created by **nindate** on this github page. You should check it out: https://github.com/nindate/ml-zoomcamp-exercises/blob/main/how-to-use-heroku.md

First of all, make sure you have an account to deploy your image to the Heroku docker registry. You can sign up here: https://signup.heroku.com/

Edit the ENTRYPOINT of Dockerfile to this one as this:
```Dockerfile
ENTRYPOINT ["gunicorn", "score:app"]
```

After that, install heroku CLI by follow the instructions on this page: https://devcenter.heroku.com/articles/heroku-cli
Or if you are on the macOS environment, you can install it by running this command on your terminal:
```cmd
brew tap heroku/brew && brew install heroku
```

Now, login to heroku CLI by running this command below:
``` cmd
heroku login
```
A browser window will pop up to the login page. Login using your account and confirm the authorization process and go back to the terminal to continue the next step.

Login to Heroku container:
```cmd
heroku container:login
```

And then create the app from the built image, in this case I set the name as zoomcamp-capstone-tg. Make sure no one on the heroku server has taken the name before. Otherwise it will gives the error that the name has been taken:
```cmd
heroku create zoomcamp-capstone-tg 
```

Build the image using this command. It also push your built image to Heroku container registry:
```cmd
heroku container:push web -a zoomcamp-capstone-tg
```

Finally, release it to expose it to public using this command:
```cmd
heroku container:release web -a zoomcamp-capstone-tg
```
and the app is ready to be hit.
In this case, the app url is https://zoomcamp-capstone-tg.herokuapp.com/predict


## Usage

You need these all parameters as an input to the model. You can change the value, but make sure the data type is number:
```python
{"recency": 1,
  "frequency": 16,
  "total_donated": 4000,
  "months_since_beginning": 35
}
  ```

And it gives the output as below:
```python
{'donating_probability': 0.8267529010772705, 'is_donating': True}
```
