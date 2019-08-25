# Intro

This is a simple poll web app that allows users to create and share polls.

## Installation & Running
1. Have Python3 installed
1. Have virtualenv installed
1. Clone this repo - `git clone git@github.com:thejoshcrawford/pipl-assignment.git`
1. `cd pipl-assignment`
1. Install the virtual environment - `virtualenv -p python3 .`
1. `souce bin/activate`
1. Install Django - `pip install Django`
1. Install Django Rest Framework - `pip install djangorestframework`
1. Create your database - `cd src`
1. `python manage.py migrate`
1. Run your web server - `python manage.py runserver`
1. Load the app in a browser by opening http://127.0.0.1:8000/

## Requirements:
- No authentication
- Each user can create as many polls as they wish (/create)
- Each poll can have an unlimited number of answers
- Every poll has a unique URL, which can be sent to anyone (/poll/ID)
- Every user can answer once on each poll
- On each poll we need to save:
-- Votes per option.
-- User agent, IP addresses and additional information from where each vote was
made.

## Sites used for help
- https://www.youtube.com/watch?v=F5mRW0jo-U4\
- https://medium.com/quick-code/crud-app-using-vue-js-and-django-516edf4e4217   
- https://www.django-rest-framework.org/
- https://stackoverflow.com/        
- https://github.com/codingforentrepreneurs/Try-Django/blob/master/.gitignore

## Login
super user - josh
password - password
*Yes this should never be saved in a production repo*

## Design Decisions
- PUT and DELETE is disabled on polls to prevent other individuals from changing a poll (no authentication) 

## Future Improvements or Considerations
- Change table names and urls to be plural instead of singular polls vs poll
- Add authentication
- Not of the best practice for making the Vue router work with the Django router
- Show the latest polls on the first page the polls on the first
- Form validation should be added
- Use complete ES2015 and create a build step for backwards compatibility
- Separate Vue code and templates
- Create proper Vue components and data share
- Disable debug mode
- I don't show error when a user tries to vote twice, to limit feedback for users trying to hack the page
- Sort poll after voting