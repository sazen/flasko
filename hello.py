from flask import Flask, render_template

#Create Falsk instance (object)
app=Flask(__name__)

#Create a route decorator (route is URL enter page like index.thml or start_here.html)
@app.route('/') # in function route from app instace, add route parameter (for index.html is just '/' for start_here is '/start here')

def index():
    stuff='<strong>Bolded staff</strong>'
    first_name='Jojo'#define a variable
    pizza=['gog','ee','ff',55]#string variable
    return render_template('index.html',
    first=first_name,
    boldstaff=stuff,
    pizza=pizza
    ) 

#URL is localhost:5000/user/John
@app.route('/user/<name>')#<name> takes parameter name from browser
def user(name):
#https://www.youtube.com/watch?v=0Qxtt4veJIc
#    return'<h1>Hello {}</h1>'.format(name)

#https://www.youtube.com/watch?v=4yaG-jFfePc
    return render_template('user.html',user_name=name) 

# Invalid URL
@app.errorhandler(404)
def page_error(e):
    return render_template('404.html'),404

# Internal server error
@app.errorhandler(500)
def page_error(e):
    return render_template('500.html'),500

