from flask import Flask, render_template, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
db = SQLAlchemy()

update_cmd = """UPDATE for_web.user_db SET shopping_cart = '{\"liked_pid\": [\"5566\", \"7788\", \"69\"]}' WHERE (pid = '1');"""


select_table = {
    'club': '''SELECT * FROM for_web.club_info''',
    'product': '''SELECT * FROM for_web.product_list''',
    'user': '''SELECT * FROM for_web.user_db'''
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:bruh@127.0.0.1:3306/for_web"

db.init_app(app)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/read_all/<string:table_name>', methods=['GET']) # 
def read_all(table_name):
    print(str(select_table[table_name]+''';'''))
    cur = db.engine.execute(select_table[table_name]+''';''')
    rv = cur.fetchall()
    temp = ""
    for item in rv:
        temp = temp+str(item)+"\r\n"
    print(temp)
    return temp


@app.route('/read/<string:table_name>/<string:ID>', methods=['GET'])
def read(table_name, ID):
    print(str(select_table[table_name]+''' WHERE id='''+ID+''';'''))
    cur = db.engine.execute(
        select_table[table_name]+''' WHERE pid='''+ID+''';''')
    rv = cur.fetchall()
    temp = ""
    for item in rv:
        temp = temp+str(item)+"\r\n"
    print(temp)
    return temp


if __name__ == '__main__':
    app.run(debug=True, port=3000)
