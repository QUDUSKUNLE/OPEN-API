### OPEN API
This application allows users to signup, signin, post, edit and delete articles

### The Approach
- A user model is created which inherits from the django AbstractBaseUser to store a user's info and its authorization keys
- An endpoints to login a user which will return a token. The token is used to verify a user when requests are made
- An endpoint for users to getting and retriving articles

### Technologies used
The functionality of this app depends on the following technologies.

- Django
- Django REST Framework
- Sqlite3

### Usage
- Visit `localhost:8080/admin` on your browser to log in to the admin.
- Visit `localhost:8000/api/v1/users/` to sign up
- Visit the endpoints `localhost:8080/api/v1/login/` on postman or the browser and supplied your username(which is your email) and password.
- Grab the token and pass it as Authorization Token header while you access the endpoints `localhost:8080/api/v1/articles/`
- The GET method will retrieve articles
- The POST method will post, retrieve and edit `articles`


### Author
`Qudus Yekeen`

### License & Copyright
MIT © Qudus Yekeen