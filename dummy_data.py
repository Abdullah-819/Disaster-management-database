from app import app
from models import db, Disaster, Victim, FoodItem, HealthItem

with app.app_context():

    # ---------- Clear existing data ----------
    Victim.query.delete()
    FoodItem.query.delete()
    HealthItem.query.delete()
    Disaster.query.delete()
    db.session.commit()

    # ---------- Disasters ----------
    disasters = [
        Disaster(name="Flood Lahore", disaster_type="Flood", date="2024-08-10", location="Lahore"),
        Disaster(name="Earthquake Quetta", disaster_type="Earthquake", date="2024-07-02", location="Quetta"),
        Disaster(name="Cyclone Karachi", disaster_type="Cyclone", date="2024-06-15", location="Karachi"),
        Disaster(name="Heatwave Multan", disaster_type="Heatwave", date="2024-05-20", location="Multan"),
        Disaster(name="Drought Sukkur", disaster_type="Drought", date="2024-04-30", location="Sukkur")
    ]
    db.session.add_all(disasters)
    db.session.commit()

    # ---------- Victims ----------
    victims = [
        Victim(name="Ali Khan", age=32, disaster_id=disasters[0].id),
        Victim(name="Sara Ahmed", age=27, disaster_id=disasters[0].id),
        Victim(name="Ahmed Raza", age=45, disaster_id=disasters[1].id),
        Victim(name="Hina Iqbal", age=30, disaster_id=disasters[2].id),
        Victim(name="Bilal Sheikh", age=38, disaster_id=disasters[3].id),
        Victim(name="Zara Malik", age=21, disaster_id=disasters[4].id),
        Victim(name="Usman Tariq", age=50, disaster_id=disasters[1].id),
        Victim(name="Ayesha Noor", age=25, disaster_id=disasters[2].id)
    ]
    db.session.add_all(victims)
    db.session.commit()

    # ---------- Food Items ----------
    food_items = [
        FoodItem(name="Rice Bags (5kg)", quantity=250, disaster_id=disasters[0].id),
        FoodItem(name="Water Bottles (1L)", quantity=600, disaster_id=disasters[0].id),
        FoodItem(name="Canned Beans", quantity=350, disaster_id=disasters[1].id),
        FoodItem(name="Bread Loaves", quantity=450, disaster_id=disasters[2].id),
        FoodItem(name="Milk Packets (1L)", quantity=180, disaster_id=disasters[3].id),
        FoodItem(name="Sugar (2kg bags)", quantity=120, disaster_id=disasters[4].id),
        FoodItem(name="Biscuits", quantity=200, disaster_id=disasters[1].id),
        FoodItem(name="Pasta Packs", quantity=150, disaster_id=disasters[2].id)
    ]
    db.session.add_all(food_items)
    db.session.commit()

    # ---------- Health Items ----------
    health_items = [
        HealthItem(name="First Aid Kits", quantity=60, disaster_id=disasters[0].id),
        HealthItem(name="Medicine Packs", quantity=90, disaster_id=disasters[1].id),
        HealthItem(name="Sanitizers (500ml)", quantity=75, disaster_id=disasters[2].id),
        HealthItem(name="Face Masks", quantity=120, disaster_id=disasters[3].id),
        HealthItem(name="Painkillers (tablets)", quantity=80, disaster_id=disasters[4].id),
        HealthItem(name="Bandages", quantity=50, disaster_id=disasters[0].id),
        HealthItem(name="Vitamin Supplements", quantity=40, disaster_id=disasters[1].id)
    ]
    db.session.add_all(health_items)
    db.session.commit()

    print("✅ Dummy data inserted successfully!")
