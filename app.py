from flaskemr import app, db
#from waitress import serve

if __name__ == "__main__":
    app.run(debug=True)
#    with app.app_context():
#        db.create_all()
#    serve(app, host="0.0.0.0", port=5000)
