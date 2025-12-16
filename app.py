from flask import Flask, render_template, request, redirect
from models import db, Disaster, Victim, FoodItem, HealthItem

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------- HOME ----------
@app.route('/')
def index():
    return render_template('index.html')


# ---------- CREATE ----------
@app.route('/add_disaster', methods=['GET', 'POST'])
def add_disaster():
    if request.method == 'POST':
        disaster = Disaster(
            name=request.form['name'],
            disaster_type=request.form['type'],
            date=request.form['date'],
            location=request.form['location']
        )
        db.session.add(disaster)
        db.session.commit()
        return redirect('/view_disasters')
    return render_template('add_disaster.html')


@app.route('/add_victim', methods=['GET', 'POST'])
def add_victim():
    disasters = Disaster.query.all()
    if request.method == 'POST':
        victim = Victim(
            name=request.form['name'],
            age=request.form['age'],
            disaster_id=request.form['disaster_id']
        )
        db.session.add(victim)
        db.session.commit()
        return redirect('/view_disasters')
    return render_template('add_victim.html', disasters=disasters)


@app.route('/add_food_item', methods=['GET', 'POST'])
def add_food_item():
    disasters = Disaster.query.all()
    if request.method == 'POST':
        food = FoodItem(
            name=request.form['name'],
            quantity=request.form['quantity'],
            disaster_id=request.form['disaster_id']
        )
        db.session.add(food)
        db.session.commit()
        return redirect('/view_food_items')
    return render_template('add_food_item.html', disasters=disasters)


@app.route('/add_health_item', methods=['GET', 'POST'])
def add_health_item():
    disasters = Disaster.query.all()
    if request.method == 'POST':
        health = HealthItem(
            name=request.form['name'],
            quantity=request.form['quantity'],
            disaster_id=request.form['disaster_id']
        )
        db.session.add(health)
        db.session.commit()
        return redirect('/view_health_items')
    return render_template('add_health_item.html', disasters=disasters)


# ---------- READ ----------
@app.route('/view_disasters')
def view_disasters():
    disasters = Disaster.query.all()
    return render_template('view_disasters.html', disasters=disasters)


@app.route('/view_tables')
def view_tables():
    return render_template(
        'view_tables.html',
        disasters=Disaster.query.all(),
        victims=Victim.query.all(),
        food_items=FoodItem.query.all(),
        health_items=HealthItem.query.all()
    )



@app.route('/view_food_items')
def view_food_items():
    disasters = Disaster.query.all()
    totals = [sum([fi.quantity for fi in d.food_items]) for d in disasters]
    return render_template('view_food_items.html', disasters=disasters, totals=totals)


@app.route('/view_health_items')
def view_health_items():
    disasters = Disaster.query.all()
    return render_template('view_health_items.html', disasters=disasters)


# ---------- UPDATE ----------
@app.route('/edit_disaster/<int:id>', methods=['GET', 'POST'])
def edit_disaster(id):
    disaster = Disaster.query.get_or_404(id)
    if request.method == 'POST':
        disaster.name = request.form['name']
        disaster.disaster_type = request.form['type']
        disaster.date = request.form['date']
        disaster.location = request.form['location']
        db.session.commit()
        return redirect('/view_disasters')
    return render_template('edit_disaster.html', disaster=disaster)


# ---------- DELETE ----------
@app.route('/delete_disaster/<int:id>')
def delete_disaster(id):
    disaster = Disaster.query.get_or_404(id)
    db.session.delete(disaster)
    db.session.commit()
    return redirect('/view_disasters')


@app.route('/clear_database')
def clear_database():
    Victim.query.delete()
    FoodItem.query.delete()
    HealthItem.query.delete()
    Disaster.query.delete()
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
