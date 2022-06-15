from unicodedata import name
from flask import Blueprint, render_template, request, flash, redirect, send_file, url_for, request,send_file,Response
from io import BytesIO

from werkzeug.utils import secure_filename
from .models import Img
from . import db
import psycopg2
import psycopg2.extras
import os

#create Blueprint
click = Blueprint('click', __name__)

#postgres query test
conn = psycopg2.connect(dbname='test', user='postgres',
                        password='0305', host='localhost')
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor.execute('SELECT * FROM pet WHERE age >= 5')

#data
data = cursor.fetchall()

#get all table column names
cursor.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'pet' ")
heads = cursor.fetchall()

headings = ('id', 'name', 'age', 'owner_id')


@click.route('/click', methods=['GET', 'POST'])
def index_click():
    if request.method == 'POST':
        password = request.form.get('pswd')
        print(password)
    return render_template('click.html', data=data, headings=heads)

@click.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['pic']
        upload = Img(filename=file.filename, data=file.read(), mimetype=file.mimetype)
        db.session.add(upload)
        db.session.commit()
        #file.save(secure_filename(file.filename))
        file.save(os.path.join('website/images/', secure_filename(file.filename)))
    return f'Image has been uploaded! To download it go to /download/{upload.id}'

@click.route('/download/<upload_id>')
def download(upload_id):
    upload = Img.query.filter_by(id=upload_id).first()
    print(upload)
    return send_file(BytesIO(upload.data), attachment_filename=upload.filename, as_attachment=True)
















