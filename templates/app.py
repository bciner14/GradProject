from  flask import  Flask,render_template,request,jsonify
import psycopg2


app=Flask(__name__,template_folder='templates')


database_name = "checklist"
user_name = "postgres"
password = "hstnfrnctn2"
host_ip = "localhost"
host_port = "5434"

baglanti = psycopg2.connect(database=database_name, user=user_name, password=password, host=host_ip, port=host_port)

baglanti.autocommit = True

cursor = baglanti.cursor()


"""""@app.route("/")
def anasayfa():
    cursor.execute('select *from students;' )
    return "<h1>anasayfamıza hoşgeldiniz</h1>"


@app.route("/kaydol")
def kaydol():
    return "<h1>Kullanıcı adı:<br>Şifre:</h1>"

@app.errorhandler(404)
def error(hata):
    return render_template("404.html")


if __name__== "__main__":
    app.debug=True
    app.run()    """
@app.route('/', methods=['GET'])
def get():
    response = {
        'message': 'Hi, there!'
    }
    return jsonify(response)



# Endpoint ekleme
@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {'name': 'ali', 'age': 25},
        {'name': 'Veli', 'age': 23},
        {'name': 'ayse', 'age': 30},
    ]
    return jsonify(users)


# Yeni veri ekleme
@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    # user verilerinin veritabanina kaydedilmesi
    response = {
        'message': 'User created successfully!',
        'user': user
    }
    return jsonify(response)

# Veri guncelleme
@app.route('/users/<string:name>', methods=['PUT'])
def update_user(name):
    user = request.json
    # name ile eslesen kullanicinin guncellenmesi
    response = {
        'message': f'{name} updated successfully!',
        'user': user
    }
    return jsonify(response)

# Veri Silme:
    @app.route('/users/<string:name>', methods=['DELETE'])
    def delete_user(name):
    # name ile eslesen kullanicinin silinmesi
     response = {
        'message': f'{name} deleted successfully!'
    }
    return jsonify(response)

# Bunlarin disinda veritabanı baglantilari, kimlik dogrulama, yetkilendirme ve hata yonetimi gibi
# ozellikleri de ekleyebilirsiniz.
if __name__ == '__main__':
    app.run(debug=True)

#
# Bunlarin disinda veritabanı baglantilari, kimlik dogrulama, yetkilendirme ve hata yonetimi gibi
# ozellikleri de ekleyebilirsiniz.
"""@app.route("/")
def index():

 return render_template("studentlogin.html")"""

"""@app.route("/toplam",methods =["GET","POST"])
def toplam():
  if request.method == "POST":
      number1=request.form.get("number1")
      number2 = request.form.get("number2")
      return render_template("number.html",total=number1+number2)
  else:
    return render_template("number.html")"""

"""app.route("/Login")
def login():
    return "Kullanıcı adı:"


app.route("/Logout")
def logout():
    return "Çıkış yap:"
if __name__== "__main__":
    app.run(debug = True)"""
    