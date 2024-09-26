from flask import Flask 
app=Flask(__name__)
@app.route("/")
def fun():
    return ("this is hello")
@app.route("/admin")
def admin_page():
    return ("admin page")
app.run()