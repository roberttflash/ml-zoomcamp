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
heroku container:login
```

And then create the app from the built image, in this case I set the name as zoomcamp-midterm:
```cmd
heroku create zoomcamp-midterm 
```

Build the image using this command. It also push your built image to Heroku container registry:
```cmd
heroku container:push web -a zoomcamp-midterm
```

Finally, release it to expose it to public using this command:
```cmd
heroku container:release web -a zoomcamp-midterm
```
and the app is ready to be hit.
In this case, the app url is https://zoomcamp-midterm.herokuapp.com/predict


## Usage

You need these all parameters as an input to the model
```python
{'checking_status': "'<0'",
 'duration': 36,
 'credit_history': "'critical/other existing credit'",
 'purpose': 'education',
 'credit_amount': 8065,
 'savings_status': "'<100'",
 'employment': "'1<=X<4'",
 'installment_commitment': 3,
 'personal_status': "'female div/dep/mar'",
 'other_parties': 'none',
 'residence_since': 2,
 'property_magnitude': "'no known property'",
 'age': 25,
 'other_payment_plans': 'none',
 'housing': 'own',
 'existing_credits': 2,
 'job': "'high qualif/self emp/mgmt'",
 'num_dependents': 1,
 'own_telephone': 'yes',
 'foreign_worker': 'yes'}
  ```

And it gives the output as below:
```python
{'bad': True, 'bad_probability': 0.9411764705882353}
```

You can also run test.py in this repo to automatically hit the app.

And below is the list of possible inputs for each parameter:
```python
['age',
 "checking_status='0<=X<200'",
 "checking_status='<0'",
 "checking_status='>=200'",
 "checking_status='no checking'",
 'credit_amount',
 "credit_history='all paid'",
 "credit_history='critical/other existing credit'",
 "credit_history='delayed previously'",
 "credit_history='existing paid'",
 "credit_history='no credits/all paid'",
 'duration',
 "employment='1<=X<4'",
 "employment='4<=X<7'",
 "employment='<1'",
 "employment='>=7'",
 'employment=unemployed',
 'existing_credits',
 'foreign_worker=no',
 'foreign_worker=yes',
 "housing='for free'",
 'housing=own',
 'housing=rent',
 'installment_commitment',
 "job='high qualif/self emp/mgmt'",
 "job='unemp/unskilled non res'",
 "job='unskilled resident'",
 'job=skilled',
 'num_dependents',
 "other_parties='co applicant'",
 'other_parties=guarantor',
 'other_parties=none',
 'other_payment_plans=bank',
 'other_payment_plans=none',
 'other_payment_plans=stores',
 'own_telephone=none',
 'own_telephone=yes',
 "personal_status='female div/dep/mar'",
 "personal_status='male div/sep'",
 "personal_status='male mar/wid'",
 "personal_status='male single'",
 "property_magnitude='life insurance'",
 "property_magnitude='no known property'",
 "property_magnitude='real estate'",
 'property_magnitude=car',
 "purpose='domestic appliance'",
 "purpose='new car'",
 "purpose='used car'",
 'purpose=business',
 'purpose=education',
 'purpose=furniture/equipment',
 'purpose=other',
 'purpose=radio/tv',
 'purpose=repairs',
 'purpose=retraining',
 'residence_since',
 "savings_status='100<=X<500'",
 "savings_status='500<=X<1000'",
 "savings_status='<100'",
 "savings_status='>=1000'",
 "savings_status='no known savings'"]
 ```
