#import the relevant libraries 
from bottle import route, run

#when you visit the website's homepage...
@route('/')
def homepage():
    #display the words "Hello user"
    html = """
    <html>
    <head>
      <title>"Homepage"</title>
      <style>
        h1   {color:blue}
        p    {color:green;
            border:1px solid black;
            padding:10px;
            }
          body {
            color: blue;
            text-decoration: underline;
            font-size: 42px;
            background-color:lightgray;
          }
      </style>
    </head>
    <body>
        <h1>Welcome!</h1>
        <p>This is your homepage</p>
        <br/>
        <h2>This form does nothing</h2>
        <form action="/" method="get">
        <input type="text" name="task" value="10" size="20" maxlength="100">
        <select name="On or Off?">
        <option>On</option>
        <option>Off</option>
        </select>
        <br/>
        <input type="submit" name="save" value="save">
        </form>
    </body>
    </html>"""
    return html

#this is where we run the server and tell it where to listen\
#'0.0.0.0' means listens to all incoming signals on port 8080
run(host='0.0.0.0', port=8080, reloader=True)
