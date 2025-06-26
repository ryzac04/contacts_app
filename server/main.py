# Step 3 - API 

from flask import request, jsonify
from config import app, db
from models import Contact

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    # Convert each Contact object in the contacts list to a JSON-serializable dictionary using its to_json() method 
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

# If running main.py, app.run(debug=True) will execute but if we import the file, app.run(debug=True) will not execute
if __name__ == "__main__":
    # instantiate models in our database - only does this if not already created 
    with app.app_context():
        db.create_all()

    app.run(debug=True)