from flask import *

app = Flask(__name__)

@app.route('/successpost/<name>')
def successPost(name):
    return 'POST : welcome %s' % name

@app.route('/successget/<name>')
def successGet(name):
    return 'GET : welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('successPost',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('successGet',name = user))

if __name__ == '__main__':
   app.run(debug = True)