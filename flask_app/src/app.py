from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:123@db/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return 'Person %r' % self.id


db.create_all()


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form['fname'] + " " + request.form['lname']

        person = Person(name=name)

        try:
            db.session.add(person)
            db.session.commit()
            return redirect("/")
        except:
            return redirect("/")
    else:
        return render_template("form.html")


@app.route("/data")
def data():
    persons = Person.query.order_by(Person.id).all()
    return render_template("data.html", persons=persons)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
