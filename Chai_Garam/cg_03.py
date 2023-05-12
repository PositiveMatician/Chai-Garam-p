#Following is the code used to make the website work





from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')#TODO find where main.html is and put the file location here


if __name__=='__main__':
    app.run()