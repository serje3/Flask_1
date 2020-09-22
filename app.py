import json

from flask import Flask, render_template, url_for,request, redirect
from Encryption import Main

application = Flask(__name__)
with open('keys.json') as f:
   a=json.load(f)
global posts
with open('posts.json') as f:
   posts=json.load(f)
def addPost(text,user):
    posts[text] = user
@application.route("/home")
@application.route("/")
def index():
    postsAll=None
    if posts is not None:
      postsAll=list(posts.items())
      postsAll.reverse()
    return render_template('index.html', posts=postsAll)


@application.route("/encrypt")
def encryptPage():
   return render_template("encrypt.html")


@application.route("/decrypt")
def decryptPage():
   return render_template("decrypt.html")


@application.route("/check", methods=['POST'])
def encryptDone():
   if len(str(request.form['message']))!=0:
      d=Main.enc(request.form['message'].replace('ё','е'))
      a[d[0]]=str(d[1])
      word=str(d[0])
      with open('keys.json', 'w') as f:
         json.dump(a, f)
      return render_template('encryptDone.html',word=word)
   else:
      return encryptPage()

@application.route("/decheck", methods=['POST'])
def decryptDone():
   if len(request.form['word'])==0:
      return decryptPage()
   elif request.form['word'] in a:
      d=Main.dec(request.form['word'],a[request.form['word']])
      return render_template('decryptDone.html',word=d)
   else:
      if str(request.form['word']).isdigit():
         return render_template('decryptFailed.html', word='Такого слова не существует')
      else:
         return render_template('decryptFailed.html', word='Указан неверный код. На вход принимаются только цифры')
@application.route("/add")
def add():
   return render_template('add.html')
@application.route('/added', methods=['POST'])
def added():
   text = str(request.form['text'])
   user = str(request.form['user'])
   if (len(text)!= 0) and (len(user) != 0):
      addPost(text,user)
   with open('posts.json','w') as f:
      json.dump(posts,f)
   return redirect(url_for('index'))

@application.route('/delete/<string:text>')
def delete(text):
   del posts[text.replace('%20',' ')]
   return redirect(url_for('index'))
if __name__ == "__main__":
   application.run(debug=True)

# d = {}
# with open("файл.txt") as file:
#     for line in file:
#         key, *value = line.split()
#         d[key] = value