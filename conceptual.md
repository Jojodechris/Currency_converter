
Answer the following questions below:

- What are important differences between Python and JavaScript?
Javascript can be used both for front end and back end development. Python is only used in back end development.
Python's syntax are less complex and easier to read.
The debugging process in python is implemented using the terminal. In javascript it is implemented using console.log and javascript console.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

- What is a unit test?
Unit test is a flask test that tests  each single function of our code 

- What is an integration test?
An integration test is a test that help to check whether the elements of the code works well together.

- What is the role of web application framework, like Flask?
it helps us to handle the the structure and the routes of our application. 


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?
we can do it using the request object 

- How do you collect data from the body of the request using Flask?
we can use request.get_json or request.form

- What is a cookie and what kinds of things are they commonly used for?
it is a file that stores users' informtion related to a website.

- What is the session object in Flask?
a session object in flask is the place where we can store user's data which can be useful for maintaining user state or tracking user activity.

- What does Flask's `jsonify()` do?
Flask 'jsonify' helps us to turn python structure into a  JSON format.