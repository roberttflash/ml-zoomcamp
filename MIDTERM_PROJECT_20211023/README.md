# Objective
I want to create a model that can predict the bad probability of on several parameters described below. 
The dataset used for training was taken from https://www.openml.org/d/31 and I use two different methods for this as comparison, 
using unsupervised (autosklearn) and supervised (decision trees). Because of interpretability consideration, 
I decided to choose the decision trees as the final model. 
This is my first time to create the machine learning from end to end besides previous homeworks and lessons, 
so I am certain that there are so many flaws on my analysis and methods. Need input from this. Thank you.

### Attribute description   
1. checking_status: Status of existing checking account, in Deutsche Mark.  
2. duration: Duration in months  
3. credit_history: Credit history (credits taken, paid back duly, delays, critical accounts)  
4. purpose: Purpose of the credit (car, television,...)  
5. credit_amount: Credit amount  
6. savings_status: Status of savings account/bonds, in Deutsche Mark.  
7. employment: Present employment, in number of years.  
8. installment_commitment: Installment rate in percentage of disposable income  
9. personal_status: Personal status (married, single,...) and sex  
10. other_parties: Other debtors / guarantors  
11. residence_since: Present residence since X years  
12. property_magnitude: Property (e.g. real estate)  
13. age: Age in years  
14. other_payment_plans: Other installment plans (banks, stores)  
15. housing: Housing (rent, own,...)  
16. existing_credits: Number of existing credits at this bank  
17. job: Job  
18. num_dependents: Number of people being liable to provide maintenance for  
19. own_telephone: Telephone (yes,no)  
20. foreign_worker: Foreign worker (yes,no)

## Usage in localhost
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
docker run -it --rm -p <host_port>:<container_port> zoomcamp-midterm:latest
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

