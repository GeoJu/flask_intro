from flask import Flask, render_template, request
import random
import requests
from bs4 import BeautifulSoup as bssss
import csv
import datetime


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
    
@app.route("/who")
def who():

    return render_template('who.html')

@app.route("/who_is")
def who_is():

    li = ['컴퓨터','나무', '신', '칠판', '선생님','돌맹이','가수','번개']
    
    user_name = request.args.get('name')
    user_hobby = request.args.get('hobby')
    
    url1 = 'https://www.google.co.kr/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiWtf-4ua3eAhVLO7wKHd5XDuYQ_AUIDigB&biw=1444&bih=740&dpr=1.13'.format(user_name)
    url2 = 'https://www.google.co.kr/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiWtf-4ua3eAhVLO7wKHd5XDuYQ_AUIDigB&biw=1444&bih=740&dpr=1.13'.format(user_hobby)
    
    req = requests.get(url1).text
    req1 = requests.get(url2).text
    
    name_img = bs(req, 'lxml')
    hobby_img = bs(req1, 'lxml')
    
    a = name_img.findAll('img')[3]['src']
    b = hobby_img.findAll('img')[3]['src']
    
    wh = random.choice(li)
    you = '{}님 당신의 전생은 취미가 {}인 {}입니다'.format(user_name,user_hobby,wh)

    
    
    return render_template('img.html', you = you, a = a, b = b)

@app.route("/summoner")
def summoner():
    url = 'http://www.op.gg/summoner/userName='
    return render_template('summoner.html')

@app.route("/opgg")
def opgg():
    name = request.args.get('sum')
    url = 'http://www.op.gg/summoner/userName='
    html = requests.get(url+name).text
    
    soup = bssss(html, 'html.parser')
    win = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    lose = soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    #print(win)
    
    if len(win) == 0:
        win = '0승'
    else:
        win = win[0].text
    if len(lose) == 0:
        lose = '0패'
    else: 
        lose = lose[0].text
    # f = open("list.text", "a+")
    # data = "소환사의 이름은 {} {}/{}입니다".format(name, win, lose)
    # f.write(data)
    # f.close()
    f = open('list.csv','a+', encoding = 'utf-8', newline='')
    csvfile = csv.writer(f)
    data = [name, win, lose, datetime.datetime.now()]
    csvfile.writerow(data)
    
    return render_template("opgg.html", name = name, win = win, lose = lose)


@app.route('/log')
def log():
    f = open('list.csv', 'r', encoding = 'utf-8')
    logs = csv.reader(f)
    return render_template('log.html', logs = logs)


    