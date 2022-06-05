from distutils.log import debug
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
   return "Hello Mayank Gupta"
#app.add_url_rule('/', 'hello', hello_world)


#using parameters in the URL and getting the corresponding values into variables enclosed in <>
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

#using parameters in the URL with types defined in <>
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

# Normal & canonical URLs, URL routes defined ending with '/' can provide output with or without '/' in the end, 
# but the routes defined ending without '/' can't work if '/' added additionally
@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

# to redirect to different URL or to different Function, redirect() is used, and to find the corresponding method, url_for is used, as the redirect needs URL

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)