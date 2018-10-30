from flask import Flask, render_template, request
import random
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
    

@app.route("/lunch")
def  lunch():
    
    list = ['양자강', '짜장면', '김밥', '20층']
    
    c = random.choice(list)
    return render_template('lunch.html', c = c)
    
    
@app.route('/lunch/img_lunch')
def img_lunch():
    
    list = ['짜장면', '김밥', '탕수육', '김치볶음밥']
    dic = {'짜장면' : 'https://img1.daumcdn.net/thumb/R720x0/?fname=http://t1.daumcdn.net/liveboard/dinnerqueen/36e82ce28022482a8eb3b0811b99e974.jpg',
           '김밥' :   'https://post-phinf.pstatic.net/MjAxNzA3MjZfMTQ5/MDAxNTAxMDQ2ODk0NzMw.z29Xe0pLr3ecUe8pF8N3BYOmiI57YGyHAzo6u1sxhxcg.Mh3AbSmwaAAMMhZgOMY31amoqzowz_3OOk0-oQWNnYkg.JPEG/1935589795_5pny9aCF_ECB998ECA688EAB980EBB0A5.jpg?type=w1200',
           '탕수육' : 'https://www.maangchi.com/wp-content/uploads/2008/12/sweet_sour-pork-150x150.gif',
           '김치볶음밥' : 'http://img.ezmember.co.kr/cache/board/2011/08/06/b47aa3d5c379ada8beb8889db4615952.jpg'
           }

    ch = random.choice(list)
    img = dic[ch]
    return render_template('lunch.html', li = ch, img = img)
    
@app.route("/lotto")
def lotto():
    list = range(1,46)
    luck = random.sample(list, 6)
    return render_template('lotto.html', luck = sorted(luck))


@app.route("/naver")
def naver():
    return render_template('naver.html')

@app.route("/google")
def google():
    return render_template('google.html')    


@app.route("/hello_man")
def hello_man():
    return render_template('hello_man.html')    
    
    
@app.route("/hi")
def hi():
    user_name = request.args.get('name')
    return render_template('hi.html', user_name = user_name)    
    
    



    