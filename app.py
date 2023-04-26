from flask import Flask,render_template
import pickle
import os
df = pickle.load(open('movie_list.pkl','rb'))

app = Flask(__name__)
'''picFolder = os.path.join( 'static','pics')
app.config['UPLOAD_FOLDER'] = picFolder'''
@app. route ("/")
def index():
    '''pic1 =os.path. join (app.config [ 'UPLOAD_FOLDER'], 'image1.jpg')
    return render_template("index.html", user_image = 'pic1',
                           mname = list(df['title'].values))'''
    return render_template("index.html",
                           movie_name=list(df['title'].values))
'''
@app.route('/')
def index():
    return render_template('index.html')
'''
if __name__== '__main__':
    app.run(debug=True)