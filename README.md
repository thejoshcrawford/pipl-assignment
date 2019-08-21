# pipl-assignment

# resources used 
* https://www.youtube.com/watch?v=F5mRW0jo-U4\
* https://medium.com/quick-code/crud-app-using-vue-js-and-django-516edf4e4217           


# borrowed .gitignore here https://github.com/codingforentrepreneurs/Try-Django/blob/master/.gitignore

super user / password - pipl / pipl.super.user
# yes this should never be saved in a git commit, this is just a temp project

#design decisions
* PUT and DELETE is disabled on polls to prevent other individuals from changing a poll (no authentication) 

#future improvements
1. Change table names and urls to be plural instead of singular polls vs poll
2. Add authentication

not sure how to best make the vue router work with the django router
show the latest polls on the first page the polls on the first
form validation should be added
did not use ES2015 for compatibility 
separate vue code and templates
create vue components