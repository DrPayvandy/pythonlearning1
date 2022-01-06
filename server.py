import os
import csv
from flask import send_from_directory,redirect
from flask import Flask,render_template,redirect,url_for,request
app = Flask(__name__)
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                           'favicon.ico',mimetype='image/vnd.microsoft.icon')
@app.route('/')
def My_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write2csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
def write2file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
       data=request.form.to_dict()
       write2file(data)
       write2csv(data)
       print(data)
       return redirect('/tanks.html')
    else:
       return "something wen't wrong try again! "


# @app.route('/works.html')
# def works():
#     return render_template('works.html')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
# @app.route('/home.html')
# def home():
#     return render_template('index.html')
