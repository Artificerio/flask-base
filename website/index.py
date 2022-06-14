from flask import Blueprint, render_template
import psycopg2
import psycopg2.extras

#create Blueprint
index = Blueprint('index', __name__)

conn = psycopg2.connect(dbname='test', user='postgres',
                        password='0305', host='localhost')
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute('SELECT * FROM pet WHERE age >= 5')
data = cursor.fetchall()

@index.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html", name='Artem', data=data)