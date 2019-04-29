from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
app = Flask(__name__)

app.config.update(

    SECRET_KEY = '050408',
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:050408@localhost:5432/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False

)

db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/new/')
def greet(greeting = "Hello!"):
    queryValue = request.args.get('greeting', greeting)
    return '<h1> the greeting is : {0} </h1>'.format(queryValue)

@app.route('/user')
@app.route('/user/<name>')
def show_name(name = "Mina"):
    return '<h1> hello there ! {} </h1>'.format(name)

# Strings
@app.route('/text/<string:name>')
def work_with_string(name):
    return '<h1> here is string: {}</h1>'.format(name)

#Integer
@app.route('/int/<int:number>')
def workInteger(number):
    return '<h1> Here is number ' + str(number) + '</h1>'

#float
@app.route('/float/<float:number>')
def workFloat(number):
    return '<h1> here is float ' + str(number) + '</h1>'
@app.route('/temp')
def using_templates():
    return render_template('hello.html')

##Jinja templates

@app.route('/watch')
def watch_movies():
    movies_list = [

        'Hing Hong',
        'Last',
        'Go',
        'Never'
        ]

    return render_template('movies.html',

                           movies = movies_list,

                           name = "Guka"

                           )

@app.route('/movies')
def length_movies():
    movies_dict = {

        "King Arth": 2.23,
        "Prince Persia": 1.1,
        "Jnam": 3.3,
        "Youtube": 4.2

    }
    return  render_template('table.html',

                            movies = movies_dict,

                            name = "Bare"
                            )

@app.route('/filter')
def filter():
    movies_dict = {

        "King Arth": 2.23,
        "Prince Persia": 1.1,
        "Jnam": 3.3,
        "Youtube": 4.2

    }
    return  render_template('filter.html',

                            movies = movies_dict,

                            name = None,

                            film = "Thor"
                            )

@app.route('/macros')
def macros():
    movies_dict = {

        "King Arth": 2.23,
        "Prince Persia": 1.1,
        "Jnam": 3.3,
        "Youtube": 4.2

    }
    return  render_template('using_macros.html',

                            movies = movies_dict
                            )


class Publication(db.Model):

    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key = True)

    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name ):
        self.name = name

    def __repr__(self):
        return ', name is {}'.format(self.name)


class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(500), nullable = False, index = True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique = True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default = datetime.utcnow())
    ##Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages,  pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

if __name__ == '__main__':
    db.create_all()
    app.run();

