#import the relevant libraries 
from bottle import route, run

#when you visit the website's homepage...
@route('/')
def homepage():
    #display the words "Hello user"
    return "Hello User!"

#when you visit the website URL +/name/jimmy...
@route('/name/<username>')
def namepage(username):
    #display the words "Hello " plus the name they typed in the URL i.e. jimmy
    return "Hello "+str(username)+"!"

#this is where we run the server and tell it where to listen\
#'0.0.0.0' means listens to all incoming signals on port 8080
run(host='0.0.0.0', port=8080, reloader=True)
