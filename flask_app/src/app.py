from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dbuser:123@db/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(10), nullable=False)
    lname = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return 'Person %r' % self.id


db.create_all()


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']

        person = Person(fname=fname, lname=lname)

        db.session.add(person)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("form.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
