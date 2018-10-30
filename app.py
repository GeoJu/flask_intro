from flask import Flask, render_template
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

@app.route("/html_file")
def html_file():
    return render_template("file.html")



@app.route("/hello_p/<string:name>")
def hello_str(name):
    return render_template("hello.html", people_name = name)


@app.route("/cube/<int:num>")
def cube(num):
    result = num ** 3
    return render_template('cube.html', result = result, num = num)