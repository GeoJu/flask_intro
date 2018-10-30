from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/welcome")
def welcome():
    return "welcome flask!!"

@app.route("/html_tag")
def html_tag():
    return "<h1>니 하오!!!</h1>"
    
@app.route("/html_line")
def html_line():
    return """
    <h1>여러줄이 간다!!!</h1>
    <ul>
        <li>python</li>
        <li>flask</li>
        <li>good</li>
    </ul>    
    """    
    
    