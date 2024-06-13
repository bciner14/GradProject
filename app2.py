from  flask import  Flask,render_template,request,jsonify,redirect,url_for,flash,session
import psycopg2
import os
import sqlalchemy
import datetime
import array as arr





database_name = "checklist"
user_name = "postgres"
password = "hstnfrnctn24"
host_ip = "localhost"
host_port = "5434"

baglanti = psycopg2.connect(database=database_name, user=user_name, password=password, host=host_ip, port=host_port)

baglanti.autocommit = True

cursor = baglanti.cursor()

app: Flask=Flask(__name__,template_folder='templates')
app.config["SESSION_PERMANENT"]=True
app.config["SECRET_KEY"]="hstnfrnctn"
app.config["SESSION_TYPE"]="sqlalchemy"





database_name = "checklist"
user_name = "postgres"
password = "hstnfrnctn2"
host_ip = "localhost"
host_port = "5434"

baglanti = psycopg2.connect(database=database_name, user=user_name, password=password, host=host_ip, port=host_port)

baglanti.autocommit = True

cursor = baglanti.cursor()


@app.route("/",methods=['GET'])
def login():




    return render_template("login.html")


@app.route("/", methods=['POST'])
def loginpost():

    studlogin=request.form.get("studentlogin")
    profnurselogin=request.form.get("profnurselogin")
    adminlogin=request.form.get("adminlogin")

    if request.form.get('studentlogin'):
        return redirect("studentlogin")
    elif request.form.get('profnurselogin'):
        return redirect("profnurselogin")
    elif request.form.get('adminlogin'):
        return redirect("adminlogin")




    return render_template("login.html",)

@app.route("/studentlogin",methods=['GET'])
def studentlogin():




    return render_template("studentlogin.html")


@app.route("/studentlogin", methods=['POST'])
def studentloginpost():

    numara=request.form.get("numara")
    password=request.form.get("password")

    form_data={numara,password}
    durum=False
    ÖğrenciNumarasıylaAra = f"SELECT id,password,rol FROM users "
    cursor.execute(ÖğrenciNumarasıylaAra)
    users = cursor.fetchall()
    for studnum,studpassword,role in users:
        if studnum == numara and studpassword == password and role==False:
            durum=True
            break
        else:
            print(f'{studnum},{studpassword}')
            durum=False

    if durum ==True and numara != None and numara!='':
       session['num']=numara

       return redirect("home")

    else:
         flash('HATA:Giriş Başarısız')




    return render_template("studentlogin.html",form_data=form_data)


@app.route("/profnurselogin",methods=['GET'])
def profnurselogin():




    return render_template("profnurselogin.html")


@app.route("/profnurselogin", methods=['POST'])
def profnurseloginpost():

    numara=request.form.get("numara")
    password=request.form.get("password")
    rol=None

    form_data={numara,password}
    durum=False
    ÖğrenciNumarasıylaAra = f"SELECT id,password,rol FROM users "
    cursor.execute(ÖğrenciNumarasıylaAra)
    users = cursor.fetchall()
    for studnum,studpassword,role in users:
        if (studnum == numara) and (studpassword == password) and (role == True):
            durum=True
            rol=role
            break
        else:
            print(f'{studnum},{studpassword},{rol}')
            durum=False

    if durum ==True and numara != None and numara!='':
       return redirect("profnursehome")

    else:
         flash('HATA:Giriş Başarısız')




    return render_template("profnurselogin.html",form_data=form_data)



@app.route("/adminlogin",methods=['GET'])
def adminlogin():




    return render_template("adminlogin.html")


@app.route("/adminlogin", methods=['POST'])
def adminloginpost():

    numara=request.form.get("numara")
    password=request.form.get("password")

    form_data={numara,password}
    durum=False
    ÖğrenciNumarasıylaAra = f"SELECT id,password,rol FROM users "
    cursor.execute(ÖğrenciNumarasıylaAra)
    users = cursor.fetchall()
    for studnum,studpassword,role in users:
        if studnum == numara and studpassword == password and role==True:
            durum=True
            break
        else:
            print(f'{studnum},{studpassword}')
            durum=False

    if durum ==True and numara != None and numara!='':
       return redirect("adminhome")

    else:
         flash('HATA:Giriş Başarısız')




    return render_template("adminlogin.html",form_data=form_data)



@app.route("/logoutbutonu",methods=['GET','POST'])
def logoutbutonu():





     return render_template("studentlogin.html")



@app.route("/create_user", methods=['GET'])
def create_user_get():






    return render_template("register.html")


@app.route("/create_user", methods=['POST'])
def create_user_post():



      id = request.form.get("id")
      ad = request.form.get('name')
      soyad = request.form.get('surname')
      password = request.form.get('password')
      Rol = request.form.get('rol')

      form_data={id,ad,soyad,password,Rol}
      rol=True
      print(f"Rol{Rol}")


      if  (Rol == (0 or '0')) :
        print("öğrenci")
        rol = False




      cursor.execute(f"INSERT INTO users(id,name,surname,password,rol) values ('{id}','{ad}','{soyad}','{password}',{rol})")
      flash(f"{id} numaralı kullanıcı oluşturuldu")
      if rol==False:
            yenikarne = f"""
            CREATE TABLE IF NOT EXISTS {ad}{soyad}{id}Checklist (
               Özellik TEXT PRIMARY KEY,

               KB1 TEXT,
               ÖEG1 TEXT,
               HG1 TEXT,
               imzatarih1 TEXT,
               KB2 TEXT,
               ÖEG2 TEXT,
               HG2 TEXT,
               imzatarih2 TEXT,
               KB3 TEXT,
               ÖEG3 TEXT,
               HG3 TEXT,
               imzatarih3 TEXT,
               KB4 TEXT,
               ÖEG4 TEXT,
               HG4 TEXT,
               imzatarih4 TEXT
)
        """

            cursor.execute(yenikarne)

            flash(f"{id} numaralı kullanıcının karnesi oluşturuldu")
            kısımbirekle = f"""

             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('001-Hastanın kimliğini doğrulama','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                                                                                                          ('002-Fizik muayene yapma','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                                                                                                          ('003-Timpanik Membran Sıcaklığını Değerlendirme','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                                                                                                          ('004-Radial arterden nabzı ölçme','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                                                                                                          ('005-Solunumu değerlendirme ','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                              ('006-Apikal nabzı değerlendirme ','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                              ('007-Brakial arterden kan basıncını ölçme (cuff ile)','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}'),
                                                                                              ('008-Arteriyel monitorizasyon yapılan hastanın kan basıncını ölçme','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('009-Oksijen Saturasyonunu Değerlendirme','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','{None}','','','','','',''),
                                                                                              ('010-Düşme riskini değerlendirme','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('011-Düşme önlemlerini alma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('012-Basınç yarasını önleme uygulamalarını (mobilizasyon, pozisyon verme,
                                                                                                geriatri koltuğuna alma, hava yatak kullanımı, masaj vb.) yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('013-Sırt masajı uygulama','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('014-Tıbbı atık yönetimi','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('015-Kesici delici alet yönetimi','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('016-Kemoterapik ilacın dökülmesi sırasında gerekli önlemleri alma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('017-Annenin ihtiyaç duyduğu sağlık eğitimini planlama ve uygulama','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('018-Yenidoğana fototerapi bakımı verme','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('019-Yenidoğanın fiziksel muayenesini yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('020-Biyopsi hazırlığını ve işlem sonrası takibini yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('021-Anjioya hazırlık ve işlem sonrası takibini yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('022-Endoskopi işlemine hazırlık ve izlem yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('023-Parasentez işlemine hazırlık ve izlem yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('024-Torasentez işlemine hazırlık ve izlem yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('025-Kemik iliği aspirasyon ve biyopsisine hazırlık ve izlem yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('026-Ameliyat öncesi hasta hazırlığını yapma','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('027-Ameliyat yatağının hazırlanması','{None}','','','','','','','','','','','','','','',''),
                                                                                              ('028-Hastanın taburcu edilmesi','{None}','','','','','','','','','','','','','','','')
             """

            cursor.execute(kısımbirekle)

            kısımikiekle = f"""

             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('029-Karın/Bel çevresi ölçümü','','','','','','','','','','','','','','','',''),
                                                                                                                                                                           ('030-Ağız içini değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                                                                                                           ('031-Ağız sağlığını sürdürme/bakımını yapma','','','','','','','','','','','','','','','',''),
                                                                                                                                                                           ('032-Nazogastrik Sondanın Takılması','','','','','','','','','','','','','','','',''),
                                                                                                                                                                           ('033-Nazogastrik Sondayla Beslenmenin Uygulanması ','','','','','','','','','','','','','','','',''),
                                                                                                                                                                           ('034-Nazogastrik sondadan ilaç verme','','','','','','','','','','','','','','','',''),
                                                                                                                                                                           ('035-Nazogastrik sondanın çıkarılması','','','','','','','','','','','','','','','',''),
                                                                                                                      ('036-Nazogastrik tüple beslenme','','','','','','','','','','','','','','','',''),
                                                                                                                      ('037-Total parenteral beslenme','','','','','','','','','','','','','','','',''),
                                                                                                                      ('038-PEG ile besleme /bakımını yapma','','','','','','','','','','','','','','','',''),
                                                                                                                      ('039-Glukometre kullanımı','','','','','','','','','','','','','','','',''),
                                                                                                                      ('040-Periferik Venöz Giriş (IV Kateterizasyon)','','','','','','','','','','','','','','','',''),
                                                                                                                      ('041-IV sıvıları hazırlama ve uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                      ('042-IV infüzyon ilaçlarını hazırlama ','','','','','','','','','','','','','','','',''),
                                                                                                                       ('043-İntravenöz solüsyon torbasını/şişesini değiştirme','','','','','','','','','','','','','','','',''),
                                                                                                                      ('044-İntravenöz kateterin çıkarılması','','','','','','','','','','','','','','','',''),
                                                                                                                      ('045-Oral Yoldan İlaç Uygulanması','','','','','','','','','','','','','','','',''),
                                                                                                                       ('046-Order alma kurallarını uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                       ('047-İntravenöz kateterden/üç yollu musluktan bolus/puşe yolu ile ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                       ('048-İntravenöz sıvı seti portundan bolus/puşe yolu ile ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                        ('049-İlaçları deri yolu ile uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                        ('050-Göze ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                         ('051-Kulağa ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                         ('052-Buruna ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                         ('053-Vajinaya ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                          ('054-Rektuma ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                                         ('055-İnhaler ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                ('056-Nebulizatör maske ile ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                                 ('057-Flakondan Enjektöre Toz Halindeki İlacın Çekilmesi','','','','','','','','','','','','','','','',''),
                                                                                                  ('058-İntradermal Enjeksiyon Uygulaması','','','','','','','','','','','','','','','',''),
                                                                                                 ('059-Subcutan Enjeksiyon Uygulaması','','','','','','','','','','','','','','','',''),
                                                                                                ('060-İntramusküler Enjeksiyon Uygulaması','','','','','','','','','','','','','','','',''),
                                                                                                ('061-Port katateri olan hastaya ilaç uygulama','','','','','','','','','','','','','','','',''),
                                                                                               ('062-Kemoterapi ilaçların güvenli verilmesi','','','','','','','','','','','','','','','',''),
                                                                                               ('063-Minidrip ve doseflow kullanımı','','','','','','','','','','','','','','','',''),
                                                                                              ('064-Deri bütünlüğünü (renk, sıcaklık, turgor, ekimoz, kızarıklık, kaşıntı vb.) değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('065-Basınç yaralarını evrelendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('066-Basınç yarası bakımını yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('067-Yanık alanının derecelendirmesini yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('068-Yanıklı hastanın sıvı hesabını yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('069-Kuru Sıcak Uygulama (Termofor)','','','','','','','','','','','','','','','',''),
                                                                                              ('070-Buz kesesi uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('071-Sıcak/soğuk paket uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('072-Yaş Sıcak Uygulama (Sıcak Kompres)','','','','','','','','','','','','','','','',''),
                                                                                              ('073-Yaş Sıcak Uygulama (Oturma Banyosu)','','','','','','','','','','','','','','','',''),
                                                                                              ('074-Soğuk Uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('075-Soğuk sünger banyosu yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('076-Aldığı çıkardığı sıvı takibi yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('077-Hijyenik el yıkama ','','','','','','','','','','','','','','','',''),
                                                                                              ('078-Cerrahi el yıkama','','','','','','','','','','','','','','','',''),
                                                                                              ('079-Steril Eldivenlerin Giyilmesi Ve Kirli Eldivenlerin Çıkarılması','','','','','','','','','','','','','','','',''),
                                                                                              ('080-Hazır Steril Paket ya da Steril Malzeme İçeren Tepsi Kullanılarak Steril Alan Hazırlanması','','','','','','','','','','','','','','','',''),
                                                                                              ('081-Kan kültürü alma','','','','','','','','','','','','','','','',''),
                                                                                              ('082-Boğaz kültürü alma','','','','','','','','','','','','','','','',''),
                                                                                              ('083-Gaita kültürü alma','','','','','','','','','','','','','','','',''),
                                                                                              ('084-Yara kültürü alma','','','','','','','','','','','','','','','',''),
                                                                                              ('085-İdrar kateterinden kültür alma','','','','','','','','','','','','','','','',''),
                                                                                              ('086-Tam idrar tetkiki örneği alma','','','','','','','','','','','','','','','',''),
                                                                                              ('087-Kateter Bakımı (...........................) yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('088-İzole edilmiş hastanın bakımı için kişisel koruyucu ekipmanları doğru kullanma','','','','','','','','','','','','','','','','')


            """

            cursor.execute(kısımikiekle)

            kısımüçekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('089-Rektal tüp uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('090-Nazogastrik dekompresyon uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('091-Sürgü Kullanan Bireye Yardım Etme','','','','','','','','','','','','','','','',''),
                                                                                              ('092-Yüksek volümlü lavman uygulaması','','','','','','','','','','','','','','','',''),
                                                                                              ('093-Düşük volümlü lavman uygulaması ','','','','','','','','','','','','','','','',''),
                                                                                              ('094-Çift parçalı stoma torba adaptör değişimi','','','','','','','','','','','','','','','',''),
                                                                                              ('095-Tek parçalı stoma torba adaptör değişimi','','','','','','','','','','','','','','','',''),
                                                                                              ('096-Stoma Torbasının Boşaltma','','','','','','','','','','','','','','','',''),
                                                                                              ('097-Total Parenteral beslenme','','','','','','','','','','','','','','','',''),
                                                                                              ('098-Bağırsak seslerini dinleme ve değerlendirme ','','','','','','','','','','','','','','','',''),
                                                                                              ('099-Üriner Kataterizasyon Uygulaması','','','','','','','','','','','','','','','',''),
                                                                                              ('100-Kalıcı Üriner Kateterden Steril İdrar Örneği Alma','','','','','','','','','','','','','','','',''),
                                                                                              ('101-Üriner Kateteri Çıkarma','','','','','','','','','','','','','','','',''),
                                                                                              ('102-İdrar torbası boşaltma ','','','','','','','','','','','','','','','',''),
                                                                                              ('103-Prezervatif sonda uygulaması ve bakımı','','','','','','','','','','','','','','','',''),
                                                                                              ('104-Mesane jimnastiği yaptırma','','','','','','','','','','','','','','','',''),
                                                                                              ('105-24 saatlik idrar biriktirme ve gönderme','','','','','','','','','','','','','','','','')



             """

            cursor.execute(kısımüçekle)

            kısımdörtekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('106-Hastayı Yatakta Yukarı Doğru çekme','','','','','','','','','','','','','','','',''),
                                                                                              ('107-Hastanın yatak kenarına çekilmesi','','','','','','','','','','','','','','','',''),
                                                                                              ('108-Eklem hareket açıklığı (ROM) egzersizlerini uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('109-Hastayı ilk kez ayağa kaldırma','','','','','','','','','','','','','','','',''),
                                                                                              ('110-Hastayı yürütme ','','','','','','','','','','','','','','','',''),
                                                                                              ('111-Hastayı sedyeye alma','','','','','','','','','','','','','','','',''),
                                                                                              ('112-Hastayı geriatri koltuğuna alma','','','','','','','','','','','','','','','',''),
                                                                                              ('113-Nazal kanül ile oksijen uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('114-Maske ile oksijen uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('115-Nazofarengeal ve Orofarengeal Havayollarının Aspirasyonu ','','','','','','','','','','','','','','','',''),
                                                                                              ('116-Trakeostomi aspirasyonu yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('117-Trakeostomi iç kanültemizliğini yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('118-Peristomal cilt bakımı ve kanül bağı değişimi','','','','','','','','','','','','','','','',''),
                                                                                              ('119-Nebulizatör kullanma ','','','','','','','','','','','','','','','',''),
                                                                                              ('120-Airway uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('121-Ambu uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('122-Oksijen sistemi hazırlanma ve oksijen verme ','','','','','','','','','','','','','','','',''),
                                                                                              ('123-Solunum seslerini dinleme','','','','','','','','','','','','','','','',''),
                                                                                              ('124-PEEP uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('125-Derin Soluma Egzersizi','','','','','','','','','','','','','','','',''),
                                                                                              ('126-Öksürük Egzersiz Uygulaması','','','','','','','','','','','','','','','',''),
                                                                                              ('127-Buhar uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('128-Kapalı göğüs drenajı takibi','','','','','','','','','','','','','','','',''),
                                                                                              ('129-Hastanın entübe edilmesine yardım','','','','','','','','','','','','','','','',''),
                                                                                              ('130-Hastanın ekstübe edilmesine yardım','','','','','','','','','','','','','','','',''),
                                                                                              ('131-Dekonneksiyon işlemi yapma ','','','','','','','','','','','','','','','',''),
                                                                                              ('132-Yüksek akım oksijen tedavisi bakımı	','','','','','','','','','','','','','','','',''),
                                                                                              ('133-Mekanik ventilasyona bağlı hastanın bakımı','','','','','','','','','','','','','','','',''),
                                                                                              ('134-CPAP uygulaması','','','','','','','','','','','','','','','',''),
                                                                                              ('135-CVP ölçümü','','','','','','','','','','','','','','','',''),
                                                                                              ('136-Kan gazı alma ','','','','','','','','','','','','','','','',''),
                                                                                              ('137-Subklavian kateter takılmasına yardım ','','','','','','','','','','','','','','','',''),
                                                                                              ('138-Santral venöz kateterinin çıkarılması yardım ','','','','','','','','','','','','','','','',''),
                                                                                              ('139-Kan ürünleri transfüzyonu (...................)','','','','','','','','','','','','','','','',''),
                                                                                              ('140-Kan örneği alma ve laboratuara gönderme','','','','','','','','','','','','','','','',''),
                                                                                              ('141-Enjektör Kullanarak Venöz Kan Alma','','','','','','','','','','','','','','','',''),
                                                                                              ('142-EKG çekme','','','','','','','','','','','','','','','',''),
                                                                                              ('143-Hastayı monitörize etme','','','','','','','','','','','','','','','',''),
                                                                                              ('144-Hastanın arteriyel kan basıncını izleme','','','','','','','','','','','','','','','',''),
                                                                                              ('145-Manifold sistemini hazırlama ve kullanma','','','','','','','','','','','','','','','',''),
                                                                                              ('146-AV fistül bakımı','','','','','','','','','','','','','','','',''),
                                                                                              ('147-Dren(Hemovak ................) takibi','','','','','','','','','','','','','','','',''),
                                                                                              ('148-Yatak Banyosu Yaptırma','','','','','','','','','','','','','','','',''),
                                                                                              ('149-Yetişkin kadında perine bakımı	','','','','','','','','','','','','','','','',''),
                                                                                              ('150-Yetişkin erkekte perine bakımı','','','','','','','','','','','','','','','',''),
                                                                                              ('151-Saç Banyosu','','','','','','','','','','','','','','','',''),
                                                                                              ('152-Bilinçli hastada ağız bakımı','','','','','','','','','','','','','','','',''),
                                                                                              ('153-Bağımlı Hastalarda Özel Ağız Bakımı','','','','','','','','','','','','','','','',''),
                                                                                              ('154-Temel yaşam desteği basamaklarının uygulanması','','','','','','','','','','','','','','','',''),
                                                                                              ('155-Defibrilatör kullanılması','','','','','','','','','','','','','','','',''),
                                                                                              ('156-Acil arabası kontrolü ve kullanımı','','','','','','','','','','','','','','','','')



             """

            cursor.execute(kısımdörtekle)

            kısımbeşekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('157-Sağlıklı uyku için çevre yönetimini sağlama','','','','','','','','','','','','','','','','')


             """

            cursor.execute(kısımbeşekle)

            kısımaltıekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('158-Hastanın ağrı düzeyini, yerini ve şeklini değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('159-Entübe hastanın ağrı düzeyini değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('160-Çocuk hastanın ağrı ağrı düzeyini değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('161-Bilinci kapalı hastanın ağrı düzeyini değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('162Hasta kontrollü analjezi (PCA) izlemi yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('163-Glaskow koma skalasını değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('164-Bilinç- pupil takibini yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('165-Nörövasküler takip yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('166-Kafa içi basınç artışı belirti ve bulgularını izleme ','','','','','','','','','','','','','','','',''),
                                                                                              ('167-Eksternal ventriküler drenaj sistemi takibi','','','','','','','','','','','','','','','',''),
                                                                                              ('168-Aspirasyon riskini önleme','','','','','','','','','','','','','','','',''),
                                                                                              ('169-Bulantıyı azaltma girişimleri uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('170-EKT uygulanacak hastayı işleme hazırlama','','','','','','','','','','','','','','','',''),
                                                                                              ('171-EKT uygulanan hastanın işlem sonrası takibini yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('172-Delüsyon/ Sanrı Yönetimini yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('173-Hallüsinasyon Yönetimini yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('174-Deliryum yönetimini yapma','','','','','','','','','','','','','','','','')




             """

            cursor.execute(kısımaltıekle)

            kısımyediekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('175-Anksiyete düzeyini belirleme','','','','','','','','','','','','','','','',''),
                                                                                              ('176-Anksiyetesi olan bireye yaklaşımda bulunma','','','','','','','','','','','','','','','','')


             """

            cursor.execute(kısımyediekle)

            kısımsekizekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('177-Hasta ile iletişim/görüşme yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('178-Psikiyatri hastasıyla ilgili gözlem yazma','','','','','','','','','','','','','','','','')


             """

            cursor.execute(kısımsekizekle)

            kısımdokuzekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('179-Kendi kendine meme muayenesi öğretilmesi ','','','','','','','','','','','','','','','',''),
                                                                                              ('180-Kadını jinekolojik muayeneye hazırlama','','','','','','','','','','','','','','','',''),
                                                                                              ('181-Leopold manevralarını (Uterusun büyüklüğü ve pozisyonunu değerlendirme) uygulama','','','','','','','','','','','','','','','',''),
                                                                                              ('182-NST takibi yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('183-Emzirmenin öğretilmesi (meme kontrolü, bakımı vb)','','','','','','','','','','','','','','','',''),
                                                                                              ('184-Anne sütünün elle boşaltılması','','','','','','','','','','','','','','','',''),
                                                                                              ('185-Doğum öncesi izlem (bakım yönetimi)','','','','','','','','','','','','','','','',''),
                                                                                              ('186-Sezaryen doğumda erken ten teması sağlanması ve ilk emzirmenin başlatılması','','','','','','','','','','','','','','','',''),
                                                                                              ('187-Doğum, doğum sonu ve jinekolojik işlemler için perine bakımı yapma','','','','','','','','','','','','','','','',''),
                                                                                              ('188-Doğum sonu kanama kontrolü (uterus involüsyonunu değerlendirme, Fundus masajı yapma)','','','','','','','','','','','','','','','',''),
                                                                                              ('189-Aile planlaması eğitimi ','','','','','','','','','','','','','','','','')


             """

            cursor.execute(kısımdokuzekle)

            kısımonekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('190-Başetme yöntemlerini değerlendirme','','','','','','','','','','','','','','','',''),
                                                                                              ('191-Etkili başetmeye yardım etme','','','','','','','','','','','','','','','',''),
                                                                                              ('192-Kendine zarar verme riski olan hastaya yönelik önlemleri alma','','','','','','','','','','','','','','','','')


             """

            cursor.execute(kısımonekle)

            kısımonbirekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('193-Hastanın mahremiyetini ve bilgi gizliliğini koruma','','','','','','','','','','','','','','','','')



             """

            cursor.execute(kısımonbirekle)

            diğeruygulamalarekle = f"""



             insert into {ad}{soyad}{id}checklist(Özellik,kb1,Öeg1,hg1,imzatarih1,kb2,Öeg2,hg2,imzatarih2,kb3,Öeg3,hg3,imzatarih3,kb4,Öeg4,hg4,imzatarih4) values ('194-Hastanın servise kabulü','','','','','','','','','','','','','','','',''),
                                                                                              ('195-Hastanın yoğun bakım servisine kabulü','','','','','','','','','','','','','','','',''),
                                                                                              ('196-Hastanın teslim alınıp verilmesi','','','','','','','','','','','','','','','',''),
                                                                                              ('197-Hastanın başka bir üniteye nakledilmesi','','','','','','','','','','','','','','','',''),
                                                                                              ('198-Servisler arası malzeme alışverişi','','','','','','','','','','','','','','','',''),
                                                                                              ('199-Exitus Hazırlığı','','','','','','','','','','','','','','','','')


             """

            cursor.execute(diğeruygulamalarekle)

      return render_template('register.html',form_data=form_data)


@app.route("/update_user", methods=['GET'])
def update_user_get():

    return render_template("update.html")


@app.route("/update_user", methods=['PUT','POST'])
def update_user():
    id = request.form.get("id")
    ad = request.form.get('name')

    newid=request.form.get("newid")
    newname=request.form.get("newname")
    newsurname=request.form.get("newsurname")
    newpassword=request.form.get("newpassword")
    newrol=request.form.get("newrol")
    if newrol == '0' or 0:
        newrol = False

    else:

        newrol = True



    update = f"UPDATE users SET  id='{newid}',name='{newname}',surname='{newsurname}',password='{newpassword}',rol={newrol} where id='{id}'  "
    flash(f"{id} numarılı kişi güncellendi")

    cursor.execute(update)

    return render_template("update.html")

@app.route("/delete_user", methods=['GET'])
def delete_user_get():
    return render_template("delete.html")

@app.route("/delete_user", methods=['DELETE','POST'])
def delete_user_post():
    id = request.form.get("id")
    ad = request.form.get('name')

    delete = f"DELETE FROM users WHERE id='{id}'"

    cursor.execute(delete)

    flash(f"{id} numaralı kullanıcı silindi")

    return render_template("delete.html")

@app.route("/home",methods=['GET','POST'])
def homepage():
    if request.method=='POST':

     if request.form.get('1.sınıf'):
         secim=1
         session['secim']=secim
         numara=session['num']
         print(secim, numara)

         return redirect("checklistbutonları")
     elif request.form.get('2.sınıf'):
         secim=2
         session['secim'] = secim
         numara = session['num']
         print(secim, numara)
         return redirect("checklistbutonları")
     elif request.form.get('3.sınıf'):
         secim=3
         session['secim'] = secim
         numara = session['num']
         print(secim, numara)
         return redirect("checklistbutonları")
     elif request.form.get('4.sınıf'):
        secim=4
        session['secim'] = secim
        numara = session['num']
        print(secim, numara)
        return redirect("checklistbutonları")
    elif request.method=='GET' :
     return render_template("home.html")


@app.route("/profnursehome",methods=['GET','POST'])
def homeprofnursehome():
    if request.method=='POST':

     if request.form.get('sınıfileara'):
         return redirect("sınıfbutonları")
     elif request.form.get('öğrencinumarasıylaara'):
        searchwithid=request.form.get('öğrencinumarasıylaara')
        return redirect("search")
     elif request.form.get('not ver'):
        searchwithid=request.form.get('öğrencinumarasıylaara')
        return redirect("search")

    elif request.method=='GET' :
     return render_template("profnursehome.html")


@app.route("/adminhome",methods=['GET','POST'])
def adminhome():
    if request.method=='POST':

     if request.form.get('kişi ekle'):
          return redirect("create_user")
     elif request.form.get('kişi güncelle'):
        return redirect("update_user")
     elif request.form.get('kişi sil'):
         return redirect("delete_user")
     elif request.form.get("kişi ara"):
         return redirect("searchuser")




    elif request.method=='GET' :
     return render_template("adminhome.html")

@app.route("/logout",methods=['GET'])
def logout():
    return redirect(url_for('login'))









@app.route("/search",methods=['GET'])
def search():
    return render_template("search.html")


@app.route("/search",methods=['POST'])
def search_post():
    id=request.form.get("id")
    session['num']=id
    searchwithid = f"SELECT id,name,surname,password,rol  FROM users WHERE id= '{id}'"
    cursor.execute(searchwithid)
    users = cursor.fetchall()
    print(f"{id}")
    studentnumber=None
    for usernum,username,usersurname,userpassword,userrol in users:
        if usernum==id or f'{id}':
            id=usernum
            studentnumber=usernum
            print(f"studentnumber:{studentnumber}")
            name=username
            surname=usersurname
            password=userpassword
            rol=userrol

            break
        elif studentnumber == None or usernum==None:
            print("öğrenci bulunamadı")
            return render_template("500.html")

    session['cad']=name
    session['csoyad']=surname
    session['cid']=studentnumber



    return redirect("sınıfbutonları")
    print(id,name,surname,password,rol)
    #user = request.json


   # user=[{id},{name},{surname},{password},{rol}]

    #return jsonify(user)
    return f"{id,name,surname,rol}"

    return render_template("search.html",id=id)








@app.route("/checklistbutonları",methods=['get','post'])
def checklist_butonları():
    if request.method=='POST':

        if request.form.get('1.Sağlığı Algılama ve Sağlığın Yönetimi'):
            Özellikheader = '1.Sağlığı Algılama ve Sağlığın Yönetimi'
            i=1
            kısım=1
            numara=session['num']
            öğrenciad=f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users=cursor.fetchall()
            for isim,soyisim in users:
                ad=isim
                soyad=soyisim



            secim=session['secim']
            print(numara,secim,kısım)
            #özellik=arr.array('','')
            özellik=[None]*30
            #kb=arr.array('','')
            kb=[None]*30
            #öeg=arr.array('','')
            öeg=[None]*30
           # hg=arr.array('','')
            hg=[None]*30

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '001-Hastanın kimliğini doğrulama'and '028-Hastanın taburcu edilmesi'"
            cursor.execute(slctclass1)
            öğrencikarne=f"{ad}{soyad}{numara}checklist"
            öğrencikarne= cursor.fetchall()
            for özellik1,kb1,öeg1,hg1 in öğrencikarne:

                  özellik[i]=özellik1
                  kb[i]=kb1
                  öeg[i]=öeg1
                  hg[i]=hg1


                  print(f"{özellik[i]},{kb[i]},{hg[i]},index:{i}")
                  i=i+1
                  tarihfunc=today=datetime.datetime.today()
                  tarih=f"{today.day}-{today.month}-{today.year}"
            i=1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik[i], kb1=kb[i], öeg1=öeg[i], hg1=hg[i], tarih1=tarih,
                                   Özellik2=özellik[i + 1], kb2=kb[i + 1], öeg2=öeg[i + 1], hg2=hg[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik[i + 2], kb3=kb[i + 2], öeg3=öeg[i + 2], hg3=hg[i + 2],
                                   tarih3=tarih,
                                   Özellik4=özellik[i + 3], kb4=kb[i + 3], öeg4=öeg[i + 3], hg4=hg[i + 3],
                                   tarih4=tarih,
                                   Özellik5=özellik[i + 4], kb5=kb[i + 4], öeg5=öeg[i + 4], hg5=hg[i + 4],
                                   tarih5=tarih,
                                   Özellik6=özellik[i + 5], kb6=kb[i + 5], öeg6=öeg[i + 5], hg6=hg[i + 5],
                                   tarih6=tarih,
                                   Özellik7=özellik[i + 6], kb7=kb[i + 6], öeg7=öeg[i + 6], hg7=hg[i + 6],
                                   tarih7=tarih,
                                   Özellik8=özellik[i + 7], kb8=kb[i + 7], öeg8=öeg[i + 7], hg8=hg[i + 7],
                                   tarih8=tarih,
                                   Özellik9=özellik[i + 8], kb9=kb[i + 8], öeg9=öeg[i + 8], hg9=hg[i + 8],
                                   tarih9=tarih,
                                   Özellik10=özellik[i + 9], kb10=kb[i + 9], öeg10=öeg[i + 9], hg10=hg[i + 9],
                                   tarih10=tarih,
                                   Özellik11=özellik[i + 10], kb11=kb[i + 10], öeg11=öeg[i + 10], hg11=hg[i + 10],
                                   tarih11=tarih,
                                   Özellik12=özellik[i + 11], kb12=kb[i + 11], öeg12=öeg[i + 11], hg12=hg[i + 11],
                                   tarih12=tarih,
                                   Özellik13=özellik[i + 12], kb13=kb[i + 12], öeg13=öeg[i + 12], hg13=hg[i + 12],
                                   tarih13=tarih,
                                   Özellik14=özellik[i + 13], kb14=kb[i + 13], öeg14=öeg[i + 13], hg14=hg[i + 13],
                                   tarih14=tarih,
                                   Özellik15=özellik[i + 14], kb15=kb[i + 14], öeg15=öeg[i + 14], hg15=hg[i + 14],
                                   tarih15=tarih,
                                   Özellik16=özellik[i + 15], kb16=kb[i + 15], öeg16=öeg[i + 15], hg16=hg[i + 15],
                                   tarih16=tarih,
                                   Özellik17=özellik[i + 16], kb17=kb[i + 16], öeg17=öeg[i + 16], hg17=hg[i + 16],
                                   tarih17=tarih,
                                   Özellik18=özellik[i + 17], kb18=kb[i + 17], öeg18=öeg[i + 17], hg18=hg[i + 17],
                                   tarih18=tarih,
                                   Özellik19=özellik[i + 18], kb19=kb[i + 18], öeg19=öeg[i + 18], hg19=hg[i + 18],
                                   tarih19=tarih,
                                   Özellik20=özellik[i + 19], kb20=kb[i + 19], öeg20=öeg[i + 19], hg20=hg[i + 19],
                                   tarih20=tarih,
                                   Özellik21=özellik[i + 20], kb21=kb[i + 20], öeg21=öeg[i + 20], hg21=hg[i + 20],
                                   tarih21=tarih,
                                   Özellik22=özellik[i + 21], kb22=kb[i + 21], öeg22=öeg[i + 21], hg22=hg[i + 21],
                                   tarih22=tarih,
                                   Özellik23=özellik[i + 22], kb23=kb[i + 22], öeg23=öeg[i + 22], hg23=hg[i + 22],
                                   tarih23=tarih,
                                   Özellik24=özellik[i + 23], kb24=kb[i + 23], öeg24=öeg[i + 23], hg24=hg[i + 23],
                                   tarih24=tarih,
                                   Özellik25=özellik[i + 24], kb25=kb[i + 24], öeg25=öeg[i + 24], hg25=hg[i + 24],
                                   tarih25=tarih,
                                   Özellik26=özellik[i + 25], kb26=kb[i + 25], öeg26=öeg[i + 25], hg26=hg[i + 25],
                                   tarih26=tarih,
                                   Özellik27=özellik[i + 26], kb27=kb[i + 26], öeg27=öeg[i + 26], hg27=hg[i + 26],
                                   tarih27=tarih,
                                   Özellik28=özellik[i + 27], kb28=kb[i + 27], öeg28=öeg[i + 27], hg28=hg[i + 27],
                                   tarih28=tarih
                                   )
            for i in range(0,28):
             return f"{özellik[i-1]} , {kb[i-1]} , {öeg[i-1]} , {hg[i-1]} , {tarih}" \
                 f" {özellik[i]} , {kb[i]} , {öeg[i]} , {hg[i]} , {tarih} {os.linesep.join(tarih)}" \
                    f"  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------"\
                    f" {özellik[i+1]} , {kb[i+1]} , {öeg[i+1]} , {hg[i+1]} , {tarih}   " \
                    f"  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"   {özellik[i+2]} , {kb[i+2]} , {öeg[i+2]} , {hg[i+2]} , {tarih}" \
                    f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"    {özellik[i+3]} , {kb[i+3]} , {öeg[i+3]} , {hg[i+3]} , {tarih}" \
                    f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+4]} , {kb[i+4]} , {öeg[i+4]} , {hg[i+4]} , {tarih}" \
                    f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+5]} , {kb[i+5]} , {öeg[i+5]} , {hg[i+5]} , {tarih}" \
                    f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+6]} , {kb[i+6]} , {öeg[i+6]} , {hg[i+6]} , {tarih}" \
                    f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+7]} , {kb[i+7]} , {öeg[i+7]} , {hg[i+7]} , {tarih}" \
                    f"  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+8]} , {kb[i+8]} , {öeg[i+8]} , {hg[i+8]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+9]} , {kb[i+9]} , {öeg[i+9]} , {hg[i+9]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+10]} , {kb[i+10]} , {öeg[i+10]} , {hg[i+10]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+11]} , {kb[i+11]} , {öeg[i+11]} , {hg[i+11]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+12]} , {kb[i+12]} , {öeg[i+12]} , {hg[i+12]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+13]} , {kb[i+13]} , {öeg[i+13]} , {hg[i+13]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+14]} , {kb[i+14]} , {öeg[i+14]} , {hg[i+14]} , {tarih}  " \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+15]} , {kb[i+15]} , {öeg[i+15]} , {hg[i+15]} , {tarih} " \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+16]} , {kb[i+16]} , {öeg[i+16]} , {hg[i+16]} , {tarih}  " \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+17]} , {kb[i+17]} , {öeg[i+17]} , {hg[i+17]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+18]} , {kb[i+18]} , {öeg[i+18]} , {hg[i+18]} , {tarih}" \
                    f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f"{özellik[i+19]} , {kb[i+19]} , {öeg[i+19]} , {hg[i+19]} , {tarih}" \
                    f" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                    f" {özellik[i+20]} , {kb[i+20]} , {öeg[i+20]} , {hg[i+20]} , {tarih}  "\
                    f"----------------------------------------------------------------------------------"\
                     f" {özellik[i + 21]} , {kb[i + 21]} , {öeg[i + 21]} , {hg[i + 21]} , {tarih}  " \
                    f" {özellik[i + 22]} , {kb[i + 22]} , {öeg[i + 22]} , {hg[i + 22]} , {tarih}  " \
                    f" {özellik[i + 23]} , {kb[i + 23]} , {öeg[i + 23]} , {hg[i + 23]} , {tarih}  " \
                    f" {özellik[i + 24]} , {kb[i + 24]} , {öeg[i + 24]} , {hg[i + 24]} , {tarih}  " \
                    f" {özellik[i + 25]} , {kb[i + 25]} , {öeg[i + 25]} , {hg[i + 25]} , {tarih}  " \
                    f" {özellik[i + 26]} , {kb[i + 26]} , {öeg[i + 26]} , {hg[i + 26]} , {tarih}  " \




        elif request.form.get('2.Beslenme ve Metabolik'):
            Özellikheader = '2.Beslenme ve Metabolik'
            i = 1
            kısım = 2
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik2 = [None] * 61
            # kb=arr.array('','')
            kb2 = [None] * 61
            # öeg=arr.array('','')
            öeg2 = [None] * 61
            # hg=arr.array('','')
            hg2 = [None] * 61

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '029-Karın/Bel çevresi ölçümü'and '088-İzole edilmiş hastanın bakımı için kişisel koruyucu ekipmanları doğru kullanma'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik2[i] = özellik1
                kb2[i] = kb1
                öeg2[i] = öeg1
                hg2[i] = hg1


                print(f"{özellik2[i]},{kb2[i]},{hg2[i]},index:{i}")
                i=i+1

                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            print(f"index:{i}")
            i=1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik2[i], kb1=kb2[i], öeg1=öeg2[i], hg1=hg2[i], tarih1=tarih,
                                   Özellik2=özellik2[i + 1], kb2=kb2[i + 1], öeg2=öeg2[i + 1], hg2=hg2[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik2[i + 2], kb3=kb2[i + 2], öeg3=öeg2[i + 2], hg3=hg2[i + 2],
                                   tarih3=tarih,
                                   Özellik4=özellik2[i + 3], kb4=kb2[i + 3], öeg4=öeg2[i + 3], hg4=hg2[i + 3],
                                   tarih4=tarih,
                                   Özellik5=özellik2[i + 4], kb5=kb2[i + 4], öeg5=öeg2[i + 4], hg5=hg2[i + 4],
                                   tarih5=tarih,
                                   Özellik6=özellik2[i + 5], kb6=kb2[i + 5], öeg6=öeg2[i + 5], hg6=hg2[i + 5],
                                   tarih6=tarih,
                                   Özellik7=özellik2[i + 6], kb7=kb2[i + 6], öeg7=öeg2[i + 6], hg7=hg2[i + 6],
                                   tarih7=tarih,
                                   Özellik8=özellik2[i + 7], kb8=kb2[i + 7], öeg8=öeg2[i + 7], hg8=hg2[i + 7],
                                   tarih8=tarih,
                                   Özellik9=özellik2[i + 8], kb9=kb2[i + 8], öeg9=öeg2[i + 8], hg9=hg2[i + 8],
                                   tarih9=tarih,
                                   Özellik10=özellik2[i + 9], kb10=kb2[i + 9], öeg10=öeg2[i + 9], hg10=hg2[i + 9],
                                   tarih10=tarih,
                                   Özellik11=özellik2[i + 10], kb11=kb2[i + 10], öeg11=öeg2[i + 10], hg11=hg2[i + 10],
                                   tarih11=tarih,
                                   Özellik12=özellik2[i + 11], kb12=kb2[i + 11], öeg12=öeg2[i + 11], hg12=hg2[i + 11],
                                   tarih12=tarih,
                                   Özellik13=özellik2[i + 12], kb13=kb2[i + 12], öeg13=öeg2[i + 12], hg13=hg2[i + 12],
                                   tarih13=tarih,
                                   Özellik14=özellik2[i + 13], kb14=kb2[i + 13], öeg14=öeg2[i + 13], hg14=hg2[i + 13],
                                   tarih14=tarih,
                                   Özellik15=özellik2[i + 14], kb15=kb2[i + 14], öeg15=öeg2[i + 14], hg15=hg2[i + 14],
                                   tarih15=tarih,
                                   Özellik16=özellik2[i + 15], kb16=kb2[i + 15], öeg16=öeg2[i + 15], hg16=hg2[i + 15],
                                   tarih16=tarih,
                                   Özellik17=özellik2[i + 16], kb17=kb2[i + 16], öeg17=öeg2[i + 16], hg17=hg2[i + 16],
                                   tarih17=tarih,
                                   Özellik18=özellik2[i + 17], kb18=kb2[i + 17], öeg18=öeg2[i + 17], hg18=hg2[i + 17],
                                   tarih18=tarih,
                                   Özellik19=özellik2[i + 18], kb19=kb2[i + 18], öeg19=öeg2[i + 18], hg19=hg2[i + 18],
                                   tarih19=tarih,
                                   Özellik20=özellik2[i + 19], kb20=kb2[i + 19], öeg20=öeg2[i + 19], hg20=hg2[i + 19],
                                   tarih20=tarih,
                                   Özellik21=özellik2[i + 20], kb21=kb2[i + 20], öeg21=öeg2[i + 20], hg21=hg2[i + 20],
                                   tarih21=tarih,
                                   Özellik22=özellik2[i + 21], kb22=kb2[i + 21], öeg22=öeg2[i + 21], hg22=hg2[i + 21],
                                   tarih22=tarih,
                                   Özellik23=özellik2[i + 22], kb23=kb2[i + 22], öeg23=öeg2[i + 22], hg23=hg2[i + 22],
                                   tarih23=tarih,
                                   Özellik24=özellik2[i + 23], kb24=kb2[i + 23], öeg24=öeg2[i + 23], hg24=hg2[i + 23],
                                   tarih24=tarih,
                                   Özellik25=özellik2[i + 24], kb25=kb2[i + 24], öeg25=öeg2[i + 24], hg25=hg2[i + 24],
                                   tarih25=tarih,
                                   Özellik26=özellik2[i + 25], kb26=kb2[i + 25], öeg26=öeg2[i + 25], hg26=hg2[i + 25],
                                   tarih26=tarih,
                                   Özellik27=özellik2[i + 26], kb27=kb2[i + 26], öeg27=öeg2[i + 26], hg27=hg2[i + 26],
                                   tarih27=tarih,
                                   Özellik28=özellik2[i + 27], kb28=kb2[i + 27], öeg28=öeg2[i + 27], hg28=hg2[i + 27],
                                   tarih28=tarih,
                                   Özellik29=özellik2[i + 28], kb29=kb2[i + 28], öeg29=öeg2[i + 28], hg29=hg2[i + 28],
                                   tarih29=tarih,
                                   Özellik30=özellik2[i + 29], kb30=kb2[i + 29], öeg30=öeg2[i + 29], hg30=hg2[i + 29],
                                   tarih30=tarih,
                                   Özellik31=özellik2[i + 30], kb31=kb2[i + 30], öeg31=öeg2[i + 30], hg31=hg2[i + 30],
                                   tarih31=tarih,
                                   Özellik32=özellik2[i + 31], kb32=kb2[i + 31], öeg32=öeg2[i + 31], hg32=hg2[i + 31],
                                   tarih32=tarih,
                                   Özellik33=özellik2[i + 32], kb33=kb2[i + 32], öeg33=öeg2[i + 32], hg33=hg2[i + 32],
                                   tarih33=tarih,
                                   Özellik34=özellik2[i + 33], kb34=kb2[i + 33], öeg34=öeg2[i + 33], hg34=hg2[i + 33],
                                   tarih34=tarih,
                                   Özellik35=özellik2[i + 34], kb35=kb2[i + 34], öeg35=öeg2[i + 34], hg35=hg2[i + 34],
                                   tarih35=tarih,
                                   Özellik36=özellik2[i + 35], kb36=kb2[i + 35], öeg36=öeg2[i + 35], hg36=hg2[i + 35],
                                   tarih36=tarih,
                                   Özellik37=özellik2[i + 36], kb37=kb2[i + 36], öeg37=öeg2[i + 36], hg37=hg2[i + 36],
                                   tarih37=tarih,
                                   Özellik38=özellik2[i + 37], kb38=kb2[i + 37], öeg38=öeg2[i + 37], hg38=hg2[i + 37],
                                   tarih38=tarih,
                                   Özellik39=özellik2[i + 38], kb39=kb2[i + 38], öeg39=öeg2[i + 38], hg39=hg2[i + 38],
                                   tarih39=tarih,
                                   Özellik40=özellik2[i + 39], kb40=kb2[i + 39], öeg40=öeg2[i + 39], hg40=hg2[i + 39],
                                   tarih40=tarih,
                                   Özellik41=özellik2[i + 40], kb41=kb2[i + 40], öeg41=öeg2[i + 40], hg41=hg2[i + 40],
                                   tarih41=tarih,
                                   Özellik42=özellik2[i + 41], kb42=kb2[i + 41], öeg42=öeg2[i + 41], hg42=hg2[i + 41],
                                   tarih42=tarih,
                                   Özellik43=özellik2[i + 42], kb43=kb2[i + 42], öeg43=öeg2[i + 42], hg43=hg2[i + 42],
                                   tarih43=tarih,
                                   Özellik44=özellik2[i + 43], kb44=kb2[i + 43], öeg44=öeg2[i + 43], hg44=hg2[i + 43],
                                   tarih44=tarih,
                                   Özellik45=özellik2[i + 44], kb45=kb2[i + 44], öeg45=öeg2[i + 44], hg45=hg2[i + 44],
                                   tarih45=tarih,
                                   Özellik46=özellik2[i + 45], kb46=kb2[i + 45], öeg46=öeg2[i + 45], hg46=hg2[i + 45],
                                   tarih46=tarih,
                                   Özellik47=özellik2[i + 46], kb47=kb2[i + 46], öeg47=öeg2[i + 46], hg47=hg2[i + 46],
                                   tarih47=tarih,
                                   Özellik48=özellik2[i + 47], kb48=kb2[i + 47], öeg48=öeg2[i + 47], hg48=hg2[i + 47],
                                   tarih48=tarih,
                                   Özellik49=özellik2[i + 48], kb49=kb2[i + 48], öeg49=öeg2[i + 48], hg49=hg2[i + 48],
                                   tarih49=tarih,
                                   Özellik50=özellik2[i + 49], kb50=kb2[i + 49], öeg50=öeg2[i + 49], hg50=hg2[i + 49],
                                   tarih50=tarih,
                                   Özellik51=özellik2[i + 50], kb51=kb2[i + 50], öeg51=öeg2[i + 50], hg51=hg2[i + 50],
                                   tarih51=tarih,
                                   Özellik52=özellik2[i + 51], kb52=kb2[i + 51], öeg52=öeg2[i + 51], hg52=hg2[i + 51],
                                   tarih52=tarih,
                                   Özellik53=özellik2[i + 52], kb53=kb2[i + 52], öeg53=öeg2[i + 52], hg53=hg2[i + 52],
                                   tarih53=tarih,
                                   Özellik54=özellik2[i + 53], kb54=kb2[i + 53], öeg54=öeg2[i + 53], hg54=hg2[i + 53],
                                   tarih54=tarih,
                                   Özellik55=özellik2[i + 54], kb55=kb2[i + 54], öeg55=öeg2[i + 54], hg55=hg2[i + 54],
                                   tarih55=tarih,
                                   Özellik56=özellik2[i + 55], kb56=kb2[i + 55], öeg56=öeg2[i + 55], hg56=hg2[i + 55],
                                   tarih56=tarih,
                                   Özellik57=özellik2[i + 56], kb57=kb2[i + 56], öeg57=öeg2[i + 56], hg57=hg2[i + 56],
                                   tarih57=tarih,
                                   Özellik58=özellik2[i + 57], kb58=kb2[i + 57], öeg58=öeg2[i + 57], hg58=hg2[i + 57],
                                   tarih58=tarih,
                                   Özellik59=özellik2[i + 58], kb59=kb2[i + 58], öeg59=öeg2[i + 58], hg59=hg2[i + 58],
                                   tarih59=tarih,
                                   Özellik60=özellik2[i + 59], kb60=kb2[i + 59], öeg60=öeg2[i + 59], hg60=hg2[i + 59],
                                   tarih60=tarih

                                   )

            for i in range(1,59):
                return f" {özellik2[i]} , {kb2[i]} , {öeg2[i]} , {hg2[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik2[i +1]} , {kb2[i +1]} , {öeg2[i +1]} , {hg2[i+1]} , {tarih}   " \
                       f" {özellik2[i +2]} , {kb2[i +2]} , {öeg2[i +2]} , {hg2[i+2]} , {tarih}   " \
                       f" {özellik2[i +3]} , {kb2[i +3]} , {öeg2[i +3]} , {hg2[i+3]} , {tarih}   " \
                       f" {özellik2[i +4]} , {kb2[i +4]} , {öeg2[i +4]} , {hg2[i+4]} , {tarih}   " \
                       f" {özellik2[i +5]} , {kb2[i +5]} , {öeg2[i +5]} , {hg2[i+5]} , {tarih}   " \
                       f" {özellik2[i +6]} , {kb2[i +6]} , {öeg2[i +6]} , {hg2[i+6]} , {tarih}   " \
                       f" {özellik2[i +7]} , {kb2[i +7]} , {öeg2[i +7]} , {hg2[i+7]} , {tarih}   " \
                       f" {özellik2[i + 8]} ,{kb2[i + 8]} ,{öeg2[i + 8]} ,{hg2[i + 8]} , {tarih}   " \
                       f" {özellik2[i + 9]} , {kb2[i + 9]} , {öeg2[i + 9]} , {hg2[i + 9]} , {tarih}   " \
                       f" {özellik2[i + 10]} , {kb2[i + 10]} , {öeg2[i + 10]} , {hg2[i + 10]} , {tarih}   " \
                       f" {özellik2[i + 11]} , {kb2[i + 11]} , {öeg2[i + 11]} , {hg2[i + 11]} , {tarih}   " \
                       f" {özellik2[i + 12]} , {kb2[i + 12]} , {öeg2[i + 12]} , {hg2[i + 12]} , {tarih}   " \
                       f" {özellik2[i + 13]} , {kb2[i + 13]} , {öeg2[i + 13]} , {hg2[i + 13]} , {tarih}   " \
                       f" {özellik2[i + 14]} , {kb2[i + 14]} , {öeg2[i + 14]} , {hg2[i + 14]} , {tarih}   " \
                       f" {özellik2[i + 15]} , {kb2[i + 15]} , {öeg2[i + 15]} , {hg2[i + 15]} , {tarih}   " \
                        f" {özellik2[i + 16]} , {kb2[i + 16]} , {öeg2[i + 16]} , {hg2[i + 16]} , {tarih}   " \
                        f" {özellik2[i + 17]} , {kb2[i + 17]} , {öeg2[i + 17]} , {hg2[i + 17]} , {tarih}   " \
                        f" {özellik2[i + 18]} , {kb2[i + 18]} , {öeg2[i + 18]} , {hg2[i + 18]} , {tarih}   " \
                        f" {özellik2[i + 19]} , {kb2[i + 19]} , {öeg2[i + 19]} , {hg2[i + 19]} , {tarih}   " \
                        f" {özellik2[i + 20]} , {kb2[i + 20]} , {öeg2[i + 20]} , {hg2[i + 20]} , {tarih}   " \
                       f" {özellik2[i + 21]} , {kb2[i + 21]} , {öeg2[i + 21]} , {hg2[i + 21]} , {tarih}   " \
                       f" {özellik2[i + 22]} , {kb2[i + 22]} , {öeg2[i + 22]} , {hg2[i + 22]} , {tarih}   " \
                       f" {özellik2[i + 23]} , {kb2[i + 23]} , {öeg2[i + 23]} , {hg2[i + 23]} , {tarih}   " \
                       f" {özellik2[i + 24]} , {kb2[i + 24]} , {öeg2[i + 24]} , {hg2[i + 24]} , {tarih}   " \
                       f" {özellik2[i + 25]} , {kb2[i + 25]} , {öeg2[i + 25]} , {hg2[i + 25]} , {tarih}   " \
                       f" {özellik2[i + 26]} , {kb2[i + 26]} , {öeg2[i + 26]} , {hg2[i + 26]} , {tarih}   " \
                       f" {özellik2[i + 27]} , {kb2[i + 27]} , {öeg2[i + 27]} , {hg2[i + 27]} , {tarih}   " \
                       f" {özellik2[i + 28]} , {kb2[i + 28]} , {öeg2[i + 28]} , {hg2[i + 28]} , {tarih}   " \
                       f" {özellik2[i + 29]} , {kb2[i + 29]} , {öeg2[i + 29]} , {hg2[i + 29]} , {tarih}   " \
                       f" {özellik2[i + 30]} , {kb2[i + 30]} , {öeg2[i + 30]} , {hg2[i + 30]} , {tarih}   " \
                       f" {özellik2[i + 31]} , {kb2[i + 31]} , {öeg2[i + 31]} , {hg2[i + 31]} , {tarih}   " \
                       f" {özellik2[i + 32]} , {kb2[i + 32]} , {öeg2[i + 32]} , {hg2[i + 32]} , {tarih}   " \
                       f" {özellik2[i + 33]} , {kb2[i + 33]} , {öeg2[i + 33]} , {hg2[i + 33]} , {tarih}   " \
                       f" {özellik2[i + 34]} , {kb2[i + 34]} , {öeg2[i + 34]} , {hg2[i + 34]} , {tarih}   " \
                       f" {özellik2[i + 35]} , {kb2[i + 35]} , {öeg2[i + 35]} , {hg2[i + 35]} , {tarih}   " \
                       f" {özellik2[i + 36]} , {kb2[i + 36]} , {öeg2[i + 36]} , {hg2[i + 36]} , {tarih}   " \
                       f" {özellik2[i + 37]} , {kb2[i + 37]} , {öeg2[i + 37]} , {hg2[i + 37]} , {tarih}   " \
                       f" {özellik2[i + 38]} , {kb2[i + 38]} , {öeg2[i + 38]} , {hg2[i + 38]} , {tarih}   " \
                       f" {özellik2[i + 39]} , {kb2[i + 39]} , {öeg2[i + 39]} , {hg2[i + 39]} , {tarih}   " \
                       f" {özellik2[i + 40]} , {kb2[i + 40]} , {öeg2[i + 40]} , {hg2[i + 40]} , {tarih}   " \
                       f" {özellik2[i + 41]} , {kb2[i + 41]} , {öeg2[i + 41]} , {hg2[i + 41]} , {tarih}   " \
                       f" {özellik2[i + 42]} , {kb2[i + 42]} , {öeg2[i + 42]} , {hg2[i + 42]} , {tarih}   " \
                       f" {özellik2[i + 43]} , {kb2[i + 43]} , {öeg2[i + 43]} , {hg2[i + 43]} , {tarih}   " \
                       f" {özellik2[i + 44]} , {kb2[i + 44]} , {öeg2[i + 44]} , {hg2[i + 44]} , {tarih}   " \
                       f" {özellik2[i + 45]} , {kb2[i + 45]} , {öeg2[i + 45]} , {hg2[i + 45]} , {tarih}   " \
                       f" {özellik2[i + 46]} , {kb2[i + 46]} , {öeg2[i + 46]} , {hg2[i + 46]} , {tarih}   " \
                       f" {özellik2[i + 47]} , {kb2[i + 47]} , {öeg2[i + 47]} , {hg2[i + 47]} , {tarih}   " \
                       f" {özellik2[i + 48]} , {kb2[i + 48]} , {öeg2[i + 48]} , {hg2[i + 48]} , {tarih}   " \
                       f" {özellik2[i + 49]} , {kb2[i + 49]} , {öeg2[i + 49]} , {hg2[i + 49]} , {tarih}   " \
                       f" {özellik2[i + 50]} , {kb2[i + 50]} , {öeg2[i + 50]} , {hg2[i + 50]} , {tarih}   " \
                       f" {özellik2[i + 51]} , {kb2[i + 51]} , {öeg2[i + 51]} , {hg2[i + 51]} , {tarih}   " \
                       f" {özellik2[i + 52]} , {kb2[i + 52]} , {öeg2[i + 52]} , {hg2[i + 52]} , {tarih}   " \
                       f" {özellik2[i + 53]} , {kb2[i + 53]} , {öeg2[i + 53]} , {hg2[i + 53]} , {tarih}   " \
                       f" {özellik2[i + 54]} , {kb2[i + 54]} , {öeg2[i + 54]} , {hg2[i + 54]} , {tarih}   " \
                       f" {özellik2[i + 55]} , {kb2[i + 55]} , {öeg2[i + 55]} , {hg2[i + 55]} , {tarih}   " \
                       f" {özellik2[i + 56]} , {kb2[i + 56]} , {öeg2[i + 56]} , {hg2[i + 56]} , {tarih}   " \
                       f" {özellik2[i + 57]} , {kb2[i + 57]} , {öeg2[i + 57]} , {hg2[i + 57]} , {tarih}   " \
                       f" {özellik2[i + 58]} , {kb2[i + 58]} , {öeg2[i + 58]} , {hg2[i + 58]} , {tarih}   " \
                       f" {özellik2[i + 59]} , {kb2[i + 59]} , {öeg2[i + 59]} , {hg2[i + 59]} , {tarih}   " \

                return render_template("checklistbutonları.html")
        elif request.form.get('3.Eliminasyon'):
            Özellikheader = '3.Eliminasyon'
            i = 1
            kısım = 3
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik3 = [None] * 19
            # kb=arr.array('','')
            kb3 = [None] * 19
            # öeg=arr.array('','')
            öeg3 = [None] * 19
            # hg=arr.array('','')
            hg3 = [None] * 19

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '089-Rektal tüp uygulama'and '105-24 saatlik idrar biriktirme ve gönderme'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik3[i] = özellik1
                kb3[i] = kb1
                öeg3[i] = öeg1
                hg3[i] = hg1

                print(f"{özellik3[i]}{kb3[i]}{hg3[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik3[i], kb1=kb3[i], öeg1=öeg3[i], hg1=hg3[i], tarih1=tarih,
                                   Özellik2=özellik3[i + 1], kb2=kb3[i + 1], öeg2=öeg3[i + 1], hg2=hg3[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik3[i + 2], kb3=kb3[i + 2], öeg3=öeg3[i + 2], hg3=hg3[i + 2],
                                   tarih3=tarih,
                                   Özellik4=özellik3[i + 3], kb4=kb3[i + 3], öeg4=öeg3[i + 3], hg4=hg3[i + 3],
                                   tarih4=tarih,
                                   Özellik5=özellik3[i + 4], kb5=kb3[i + 4], öeg5=öeg3[i + 4], hg5=hg3[i + 4],
                                   tarih5=tarih,
                                   Özellik6=özellik3[i + 5], kb6=kb3[i + 5], öeg6=öeg3[i + 5], hg6=hg3[i + 5],
                                   tarih6=tarih,
                                   Özellik7=özellik3[i + 6], kb7=kb3[i + 6], öeg7=öeg3[i + 6], hg7=hg3[i + 6],
                                   tarih7=tarih,
                                   Özellik8=özellik3[i + 7], kb8=kb3[i + 7], öeg8=öeg3[i + 7], hg8=hg3[i + 7],
                                   tarih8=tarih,
                                   Özellik9=özellik3[i + 8], kb9=kb3[i + 8], öeg9=öeg3[i + 8], hg9=hg3[i + 8],
                                   tarih9=tarih,
                                   Özellik10=özellik3[i + 9], kb10=kb3[i + 9], öeg10=öeg3[i + 9], hg10=hg3[i + 9],
                                   tarih10=tarih,
                                   Özellik11=özellik3[i + 10], kb11=kb3[i + 10], öeg11=öeg3[i + 10], hg11=hg3[i + 10],
                                   tarih11=tarih,
                                   Özellik12=özellik3[i + 11], kb12=kb3[i + 11], öeg12=öeg3[i + 11], hg12=hg3[i + 11],
                                   tarih12=tarih,
                                   Özellik13=özellik3[i + 12], kb13=kb3[i + 12], öeg13=öeg3[i + 12], hg13=hg3[i + 12],
                                   tarih13=tarih,
                                   Özellik14=özellik3[i + 13], kb14=kb3[i + 13], öeg14=öeg3[i + 13], hg14=hg3[i + 13],
                                   tarih14=tarih,
                                   Özellik15=özellik3[i + 14], kb15=kb3[i + 14], öeg15=öeg3[i + 14], hg15=hg3[i + 14],
                                   tarih15=tarih,
                                   Özellik16=özellik3[i + 15], kb16=kb3[i + 15], öeg16=öeg3[i + 15], hg16=hg3[i + 15],
                                   tarih16=tarih,
                                   Özellik17=özellik3[i + 16], kb17=kb3[i + 16], öeg17=öeg3[i + 16], hg17=hg3[i + 16],
                                   tarih17=tarih
                                   )
            for i in range(1, 18):
                return f" {özellik3[i]} , {kb3[i]} , {öeg3[i]} , {hg3[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik3[i + 1]} , {kb3[i + 1]} , {öeg3[i + 1]} , {hg3[i + 1]} , {tarih}   " \
                       f"   {özellik3[i + 2]} , {kb3[i + 2]} , {öeg3[i + 2]} , {hg3[i + 2]} , {tarih}" \
                       f"    {özellik3[i + 3]} , {kb3[i + 3]} , {öeg3[i + 3]} , {hg3[i + 3]} , {tarih}" \
                       f"{özellik3[i + 4]} , {kb3[i + 4]} , {öeg3[i + 4]} , {hg3[i + 4]} , {tarih}" \
                       f"{özellik3[i + 5]} , {kb3[i + 5]} , {öeg3[i + 5]} , {hg3[i + 5]} , {tarih}" \
                       f"{özellik3[i + 6]} , {kb3[i + 6]} , {öeg3[i + 6]} , {hg3[i + 6]} , {tarih}" \
                       f"{özellik3[i + 7]} , {kb3[i + 7]} , {öeg3[i + 7]} , {hg3[i + 7]} , {tarih}" \
                       f"{özellik3[i + 8]} , {kb3[i + 8]} , {öeg3[i + 8]} , {hg3[i + 8]} , {tarih}" \
                       f"{özellik3[i + 9]} , {kb3[i + 9]} , {öeg3[i + 9]} , {hg3[i + 9]} , {tarih}" \
                       f"{özellik3[i + 10]} , {kb3[i + 10]} , {öeg3[i + 10]} , {hg3[i + 10]} , {tarih}" \
                       f"{özellik3[i + 11]} , {kb3[i + 11]} , {öeg3[i + 11]} , {hg3[i + 11]} , {tarih}" \
                       f"{özellik3[i + 12]} , {kb3[i + 12]} , {öeg3[i + 12]} , {hg3[i + 12]} , {tarih}" \
                       f"{özellik3[i + 13]} , {kb3[i + 13]} , {öeg3[i + 13]} , {hg3[i + 13]} , {tarih}" \
                       f"{özellik3[i + 14]} , {kb3[i + 14]} , {öeg3[i + 14]} , {hg3[i + 14]} , {tarih}"\
                       f"{özellik3[i + 15]} , {kb3[i + 15]} , {öeg3[i + 15]} , {hg3[i + 15]} , {tarih}"\
                       f"{özellik3[i + 16]} , {kb3[i + 16]} , {öeg3[i + 16]} , {hg3[i + 16]} , {tarih}"
            return render_template("checklistbutonları.html")
        elif request.form.get('4.Aktivite -Egzersiz') :
            Özellikheader = '4.Aktivite -Egzersiz'
            i = 1
            kısım = 4
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik4 = [None] * 52
            # kb=arr.array('','')
            kb4 = [None] * 52
            # öeg=arr.array('','')
            öeg4 = [None] * 52
            # hg=arr.array('','')
            hg4 = [None] * 52

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '106-Hastayı Yatakta Yukarı Doğru çekme'and '156-Acil arabası kontrolü ve kullanımı'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik4[i] = özellik1
                kb4[i] = kb1
                öeg4[i] = öeg1
                hg4[i] = hg1

                print(f"{özellik4[i]},{kb4[i]},{hg4[i]},index:{i}")
                i=i+1

                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik4[i], kb1=kb4[i], öeg1=öeg4[i], hg1=hg4[i], tarih1=tarih,
                                   Özellik2=özellik4[i + 1], kb2=kb4[i + 1], öeg2=öeg4[i + 1], hg2=hg4[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik4[i + 2], kb3=kb4[i + 2], öeg3=öeg4[i + 2], hg3=hg4[i + 2],
                                   tarih3=tarih,
                                   Özellik4=özellik4[i + 3], kb4=kb4[i + 3], öeg4=öeg4[i + 3], hg4=hg4[i + 3],
                                   tarih4=tarih,
                                   Özellik5=özellik4[i + 4], kb5=kb4[i + 4], öeg5=öeg4[i + 4], hg5=hg4[i + 4],
                                   tarih5=tarih,
                                   Özellik6=özellik4[i + 5], kb6=kb4[i + 5], öeg6=öeg4[i + 5], hg6=hg4[i + 5],
                                   tarih6=tarih,
                                   Özellik7=özellik4[i + 6], kb7=kb4[i + 6], öeg7=öeg4[i + 6], hg7=hg4[i + 6],
                                   tarih7=tarih,
                                   Özellik8=özellik4[i + 7], kb8=kb4[i + 7], öeg8=öeg4[i + 7], hg8=hg4[i + 7],
                                   tarih8=tarih,
                                   Özellik9=özellik4[i + 8], kb9=kb4[i + 8], öeg9=öeg4[i + 8], hg9=hg4[i + 8],
                                   tarih9=tarih,
                                   Özellik10=özellik4[i + 9], kb10=kb4[i + 9], öeg10=öeg4[i + 9], hg10=hg4[i + 9],
                                   tarih10=tarih,
                                   Özellik11=özellik4[i + 10], kb11=kb4[i + 10], öeg11=öeg4[i + 10], hg11=hg4[i + 10],
                                   tarih11=tarih,
                                   Özellik12=özellik4[i + 11], kb12=kb4[i + 11], öeg12=öeg4[i + 11], hg12=hg4[i + 11],
                                   tarih12=tarih,
                                   Özellik13=özellik4[i + 12], kb13=kb4[i + 12], öeg13=öeg4[i + 12], hg13=hg4[i + 12],
                                   tarih13=tarih,
                                   Özellik14=özellik4[i + 13], kb14=kb4[i + 13], öeg14=öeg4[i + 13], hg14=hg4[i + 13],
                                   tarih14=tarih,
                                   Özellik15=özellik4[i + 14], kb15=kb4[i + 14], öeg15=öeg4[i + 14], hg15=hg4[i + 14],
                                   tarih15=tarih,
                                   Özellik16=özellik4[i + 15], kb16=kb4[i + 15], öeg16=öeg4[i + 15], hg16=hg4[i + 15],
                                   tarih16=tarih,
                                   Özellik17=özellik4[i + 16], kb17=kb4[i + 16], öeg17=öeg4[i + 16], hg17=hg4[i + 16],
                                   tarih17=tarih,
                                   Özellik18=özellik4[i + 17], kb18=kb4[i + 17], öeg18=öeg4[i + 17], hg18=hg4[i + 17],
                                   tarih18=tarih,
                                   Özellik19=özellik4[i + 18], kb19=kb4[i + 18], öeg19=öeg4[i + 18], hg19=hg4[i + 18],
                                   tarih19=tarih,
                                   Özellik20=özellik4[i + 19], kb20=kb4[i + 19], öeg20=öeg4[i + 19], hg20=hg4[i + 19],
                                   tarih20=tarih,
                                   Özellik21=özellik4[i + 20], kb21=kb4[i + 20], öeg21=öeg4[i + 20], hg21=hg4[i + 20],
                                   tarih21=tarih,
                                   Özellik22=özellik4[i + 21], kb22=kb4[i + 21], öeg22=öeg4[i + 21], hg22=hg4[i + 21],
                                   tarih22=tarih,
                                   Özellik23=özellik4[i + 22], kb23=kb4[i + 22], öeg23=öeg4[i + 22], hg23=hg4[i + 22],
                                   tarih23=tarih,
                                   Özellik24=özellik4[i + 23], kb24=kb4[i + 23], öeg24=öeg4[i + 23], hg24=hg4[i + 23],
                                   tarih24=tarih,
                                   Özellik25=özellik4[i + 24], kb25=kb4[i + 24], öeg25=öeg4[i + 24], hg25=hg4[i + 24],
                                   tarih25=tarih,
                                   Özellik26=özellik4[i + 25], kb26=kb4[i + 25], öeg26=öeg4[i + 25], hg26=hg4[i + 25],
                                   tarih26=tarih,
                                   Özellik27=özellik4[i + 26], kb27=kb4[i + 26], öeg27=öeg4[i + 26], hg27=hg4[i + 26],
                                   tarih27=tarih,
                                   Özellik28=özellik4[i + 27], kb28=kb4[i + 27], öeg28=öeg4[i + 27], hg28=hg4[i + 27],
                                   tarih28=tarih,
                                   Özellik29=özellik4[i + 28], kb29=kb4[i + 28], öeg29=öeg4[i + 28], hg29=hg4[i + 28],
                                   tarih29=tarih,
                                   Özellik30=özellik4[i + 29], kb30=kb4[i + 29], öeg30=öeg4[i + 29], hg30=hg4[i + 29],
                                   tarih30=tarih,
                                   Özellik31=özellik4[i + 30], kb31=kb4[i + 30], öeg31=öeg4[i + 30], hg31=hg4[i + 30],
                                   tarih31=tarih,
                                   Özellik32=özellik4[i + 31], kb32=kb4[i + 31], öeg32=öeg4[i + 31], hg32=hg4[i + 31],
                                   tarih32=tarih,
                                   Özellik33=özellik4[i + 32], kb33=kb4[i + 32], öeg33=öeg4[i + 32], hg33=hg4[i + 32],
                                   tarih33=tarih,
                                   Özellik34=özellik4[i + 33], kb34=kb4[i + 33], öeg34=öeg4[i + 33], hg34=hg4[i + 33],
                                   tarih34=tarih,
                                   Özellik35=özellik4[i + 34], kb35=kb4[i + 34], öeg35=öeg4[i + 34], hg35=hg4[i + 34],
                                   tarih35=tarih,
                                   Özellik36=özellik4[i + 35], kb36=kb4[i + 35], öeg36=öeg4[i + 35], hg36=hg4[i + 35],
                                   tarih36=tarih,
                                   Özellik37=özellik4[i + 36], kb37=kb4[i + 36], öeg37=öeg4[i + 36], hg37=hg4[i + 36],
                                   tarih37=tarih,
                                   Özellik38=özellik4[i + 37], kb38=kb4[i + 37], öeg38=öeg4[i + 37], hg38=hg4[i + 37],
                                   tarih38=tarih,
                                   Özellik39=özellik4[i + 38], kb39=kb4[i + 38], öeg39=öeg4[i + 38], hg39=hg4[i + 38],
                                   tarih39=tarih,
                                   Özellik40=özellik4[i + 39], kb40=kb4[i + 39], öeg40=öeg4[i + 39], hg40=hg4[i + 39],
                                   tarih40=tarih,
                                   Özellik41=özellik4[i + 40], kb41=kb4[i + 40], öeg41=öeg4[i + 39], hg41=hg4[i + 39],
                                   tarih41=tarih,
                                   Özellik42=özellik4[i + 41], kb42=kb4[i + 41], öeg42=öeg4[i + 39], hg42=hg4[i + 39],
                                   tarih42=tarih,
                                   Özellik43=özellik4[i + 42], kb43=kb4[i + 42], öeg43=öeg4[i + 39], hg43=hg4[i + 39],
                                   tarih43=tarih,
                                   Özellik44=özellik4[i + 43], kb44=kb4[i + 43], öeg44=öeg4[i + 39], hg44=hg4[i + 39],
                                   tarih44=tarih,
                                   Özellik45=özellik4[i + 44], kb45=kb4[i + 44], öeg45=öeg4[i + 39], hg45=hg4[i + 39],
                                   tarih45=tarih,
                                   Özellik46=özellik4[i + 45], kb46=kb4[i + 45], öeg46=öeg4[i + 39], hg46=hg4[i + 39],
                                   tarih46=tarih,
                                   Özellik47=özellik4[i + 46], kb47=kb4[i + 46], öeg47=öeg4[i + 39], hg47=hg4[i + 39],
                                   tarih47=tarih,
                                   Özellik48=özellik4[i + 47], kb48=kb4[i + 47], öeg48=öeg4[i + 39], hg48=hg4[i + 39],
                                   tarih48=tarih,
                                   Özellik49=özellik4[i + 48], kb49=kb4[i + 48], öeg49=öeg4[i + 39], hg49=hg4[i + 39],
                                   tarih49=tarih,
                                   Özellik50=özellik4[i + 49], kb50=kb4[i + 49], öeg50=öeg4[i + 39], hg50=hg4[i + 39],
                                   tarih50=tarih,
                                   Özellik51=özellik4[i + 50], kb51=kb4[i + 50], öeg51=öeg4[i + 39], hg51=hg4[i + 39],
                                   tarih51=tarih



                                   )
            for i in range(1, 51):
                return f" {özellik[i]} , {kb[i]} , {öeg[i]} , {hg[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik[i + 1]} , {kb[i + 1]} , {öeg[i + 1]} , {hg[i + 1]} , {tarih}   " \
                       f"   {özellik[i + 2]} , {kb[i + 2]} , {öeg[i + 2]} , {hg[i + 2]} , {tarih}" \
                       f"    {özellik[i + 3]} , {kb[i + 3]} , {öeg[i + 3]} , {hg[i + 3]} , {tarih}" \
                       f"{özellik[i + 4]} , {kb[i + 4]} , {öeg[i + 4]} , {hg[i + 4]} , {tarih}" \
                       f"{özellik[i + 5]} , {kb[i + 5]} , {öeg[i + 5]} , {hg[i + 5]} , {tarih}" \
                       f"{özellik[i + 6]} , {kb[i + 6]} , {öeg[i + 6]} , {hg[i + 6]} , {tarih}" \
                       f"{özellik[i + 7]} , {kb[i + 7]} , {öeg[i + 7]} , {hg[i + 7]} , {tarih}" \
                       f"{özellik[i + 8]} , {kb[i + 8]} , {öeg[i + 8]} , {hg[i + 8]} , {tarih}" \
                       f"{özellik[i + 9]} , {kb[i + 9]} , {öeg[i + 9]} , {hg[i + 9]} , {tarih}" \
                       f"{özellik[i + 10]} , {kb[i + 10]} , {öeg[i + 10]} , {hg[i + 10]} , {tarih}" \
                       f"{özellik[i + 11]} , {kb[i + 11]} , {öeg[i + 11]} , {hg[i + 11]} , {tarih}" \
                       f"{özellik[i + 12]} , {kb[i + 12]} , {öeg[i + 12]} , {hg[i + 12]} , {tarih}" \
                       f"{özellik[i + 13]} , {kb[i + 13]} , {öeg[i + 13]} , {hg[i + 13]} , {tarih}" \
                       f"{özellik[i + 14]} , {kb[i + 14]} , {öeg[i + 14]} , {hg[i + 14]} , {tarih}  "\
                       f" {özellik[i + 15]} , {kb[i + 15]} , {öeg[i + 15]} , {hg[i + 15]} , {tarih}   " \
                       f"   {özellik[i + 16]} , {kb[i + 16]} , {öeg[i + 16]} , {hg[i + 16]} , {tarih}" \
                       f"    {özellik[i + 17]} , {kb[i + 17]} , {öeg[i + 17]} , {hg[i + 17]} , {tarih}" \
                       f"{özellik[i + 18]} , {kb[i + 18]} , {öeg[i + 18]} , {hg[i + 18]} , {tarih}" \
                       f"{özellik[i + 19]} ,  {kb[i + 19]} , {öeg[i + 19]} , {hg[i + 19]} , {tarih}" \
                       f"{özellik[i + 20]} , {kb[i + 20]} , {öeg[i + 20]} , {hg[i + 20]} , {tarih}" \
                       f"{özellik[i + 21]} , {kb[i + 21]} , {öeg[i + 21]} , {hg[i + 21]} , {tarih}" \
                       f"{özellik[i + 22]} , {kb[i + 22]} , {öeg[i + 22]} , {hg[i + 22]} , {tarih}" \
                       f"{özellik[i + 23]} , {kb[i + 23]} , {öeg[i + 23]} , {hg[i + 23]} , {tarih}" \
                       f"{özellik[i + 24]} , {kb[i + 24]} , {öeg[i + 24]} , {hg[i + 24]} , {tarih}" \
                       f"{özellik[i + 25]} , {kb[i + 25]} , {öeg[i + 25]} , {hg[i + 25]} , {tarih}" \
                       f"{özellik[i + 26]} , {kb[i + 26]} , {öeg[i + 26]} , {hg[i + 26]} , {tarih}" \
                       f"{özellik[i + 27]} , {kb[i + 27]} , {öeg[i + 27]} , {hg[i + 27]} , {tarih}" \
                       f"{özellik[i + 28]} , {kb[i + 28]} , {öeg[i + 28]} , {hg[i + 28]} , {tarih}  "\
                       f" {özellik[i + 29]} , {kb[i + 29]} , {öeg[i + 29]} , {hg[i + 29]} , {tarih}   " \
                       f"   {özellik[i + 30]} , {kb[i + 30]} , {öeg[i + 30]} , {hg[i + 30]} , {tarih}" \
                       f"    {özellik[i + 31]} , {kb[i + 31]} , {öeg[i + 31]} , {hg[i + 31]} , {tarih}" \
                       f"{özellik[i + 32]} , {kb[i + 32]} , {öeg[i + 32]} , {hg[i + 32]} , {tarih}" \
                       f"{özellik[i + 33]} ,  {kb[i + 33]} , {öeg[i + 33]} , {hg[i + 33]} , {tarih}" \
                       f"{özellik[i + 34]} , {kb[i + 34]} , {öeg[i + 34]} , {hg[i + 34]} , {tarih}" \
                       f"{özellik[i + 35]} , {kb[i + 35]} , {öeg[i + 35]} , {hg[i + 35]} , {tarih}" \
                      f"{özellik[i + 36]} , {kb[i + 36]} , {öeg[i + 36]} , {hg[i + 36]} , {tarih}" \
                      f"{özellik[i + 37]} , {kb[i + 37]} , {öeg[i + 37]} , {hg[i + 37]} , {tarih}" \
                      f"{özellik[i + 38]} , {kb[i + 38]} , {öeg[i + 38]} , {hg[i + 38]} , {tarih}" \
                      f"{özellik[i + 39]} , {kb[i + 39]} , {öeg[i + 39]} , {hg[i + 39]} , {tarih}" \
                      f"{özellik[i + 40]} , {kb[i + 40]} , {öeg[i + 40]} , {hg[i + 40]} , {tarih}" \
                      f"{özellik[i + 41]} , {kb[i + 41]} , {öeg[i + 41]} , {hg[i + 41]} , {tarih}" \
                      f"{özellik[i + 42]} , {kb[i + 42]} , {öeg[i + 42]} , {hg[i + 42]} , {tarih}  " \
                       f"{özellik[i + 43]} , {kb[i + 43]} , {öeg[i + 43]} , {hg[i + 43]} , {tarih}" \
                       f"{özellik[i + 44]} , {kb[i + 44]} , {öeg[i + 44]} , {hg[i + 44]} , {tarih}" \
                       f"{özellik[i + 45]} , {kb[i + 45]} , {öeg[i + 45]} , {hg[i + 45]} , {tarih}" \
                       f"{özellik[i + 46]} , {kb[i + 46]} , {öeg[i + 46]} , {hg[i + 46]} , {tarih}" \
                       f"{özellik[i + 47]} , {kb[i + 47]} , {öeg[i + 47]} , {hg[i + 47]} , {tarih}" \
                       f"{özellik[i + 48]} , {kb[i + 48]} , {öeg[i + 48]} , {hg[i + 48]} , {tarih}" \
                       f"{özellik[i + 49]} , {kb[i + 49]} , {öeg[i + 49]} , {hg[i + 49]} , {tarih}" \
                       f"{özellik[i + 50]} , {kb[i + 50]} , {öeg[i + 50]} , {hg[i + 50]} , {tarih}"


        elif request.form.get('5.Uyku-Dinlenme  ') :
            Özellikheader = '5.Uyku-Dinlenme  '
            i = 1
            kısım = 5
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik5 = [None] * 2
            # kb=arr.array('','')
            kb5 = [None] * 2
            # öeg=arr.array('','')
            öeg5 = [None] * 2
            # hg=arr.array('','')
            hg5 = [None] * 2

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik = '157-Sağlıklı uyku için çevre yönetimini sağlama'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik5[i] = özellik1
                kb5[i] = kb1
                öeg5[i] = öeg1
                hg5[i] = hg1


                print(f"{özellik5[i]}{kb5[i]}{hg5[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik5[i], kb1=kb5[i], öeg1=öeg5[i], hg1=hg5[i], tarih1=tarih,


                                   )

            return f" {özellik5[i]} , {kb5[i]} , {öeg5[i]} , {hg5[i]} , {tarih}" \

            return render_template("checklistbutonları.html")
        elif request.form.get('6.Bilişsel-Algısal ') :
            Özellikheader = '6.Bilişsel-Algısal '
            i = 1
            kısım = 6
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik6 = [None] * 19
            # kb=arr.array('','')
            kb6 = [None] * 19
            # öeg=arr.array('','')
            öeg6 = [None] * 19
            # hg=arr.array('','')
            hg6 = [None] * 19

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '158-Hastanın ağrı düzeyini, yerini ve şeklini değerlendirme'and '174-Deliryum yönetimini yapma'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik6[i] = özellik1
                kb6[i] = kb1
                öeg6[i] = öeg1
                hg6[i] = hg1

                print(f"{özellik6[i]}{kb6[i]}{hg6[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik6[i], kb1=kb6[i], öeg1=öeg6[i], hg1=hg6[i], tarih1=tarih,
                                   Özellik2=özellik6[i + 1], kb2=kb6[i + 1], öeg2=öeg6[i + 1], hg2=hg6[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik6[i + 2], kb3=kb6[i + 2], öeg3=öeg6[i + 2], hg3=hg6[i + 2],
                                   tarih3=tarih,
                                   Özellik4=özellik6[i + 3], kb4=kb6[i + 3], öeg4=öeg6[i + 3], hg4=hg6[i + 3],
                                   tarih4=tarih,
                                   Özellik5=özellik6[i + 4], kb5=kb6[i + 4], öeg5=öeg6[i + 4], hg5=hg6[i + 4],
                                   tarih5=tarih,
                                   Özellik6=özellik6[i + 5], kb6=kb6[i + 5], öeg6=öeg6[i + 5], hg6=hg6[i + 5],
                                   tarih6=tarih,
                                   Özellik7=özellik6[i + 6], kb7=kb6[i + 6], öeg7=öeg6[i + 6], hg7=hg6[i + 6],
                                   tarih7=tarih,
                                   Özellik8=özellik6[i + 7], kb8=kb6[i + 7], öeg8=öeg6[i + 7], hg8=hg6[i + 7],
                                   tarih8=tarih,
                                   Özellik9=özellik6[i + 8], kb9=kb6[i + 8], öeg9=öeg6[i + 8], hg9=hg6[i + 8],
                                   tarih9=tarih,
                                   Özellik10=özellik6[i + 9], kb10=kb6[i + 9], öeg10=öeg6[i + 9], hg10=hg6[i + 9],
                                   tarih10=tarih,
                                   Özellik11=özellik6[i + 10], kb11=kb6[i + 10], öeg11=öeg6[i + 10], hg11=hg6[i + 10],
                                   tarih11=tarih,
                                   Özellik12=özellik6[i+11], kb12=kb6[i+11], öeg12=öeg6[i+11], hg12=hg6[i+11], tarih12=tarih,
                                   Özellik13=özellik6[i + 12], kb13=kb6[i + 12], öeg13=öeg6[i + 12], hg13=hg6[i + 12],
                                   tarih13=tarih,
                                   Özellik14=özellik6[i + 13], kb14=kb6[i + 13], öeg14=öeg6[i + 13], hg14=hg6[i + 13],
                                   tarih14=tarih,
                                   Özellik15=özellik6[i + 14], kb15=kb6[i + 14], öeg15=öeg6[i + 14], hg15=hg6[i + 14],
                                   tarih15=tarih,
                                   Özellik16=özellik6[i + 15], kb16=kb6[i + 15], öeg16=öeg6[i + 15], hg16=hg6[i + 15],
                                   tarih16=tarih,
                                   Özellik17=özellik6[i + 16], kb17=kb6[i + 16], öeg17=öeg6[i + 16], hg17=hg6[i + 16],
                                   tarih17=tarih

                                   )
            for i in range(1, 17):
                return f" {özellik6[i]} , {kb6[i]} , {öeg6[i]} , {hg6[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik6[i + 1]} , {kb6[i + 1]} , {öeg6[i + 1]} , {hg6[i + 1]} , {tarih}   " \
                       f"   {özellik6[i + 2]} , {kb6[i + 2]} , {öeg6[i + 2]} , {hg6[i + 2]} , {tarih}" \
                       f"    {özellik6[i + 3]} , {kb6[i + 3]} , {öeg6[i + 3]} , {hg6[i + 3]} , {tarih}" \
                       f"{özellik6[i + 4]} , {kb6[i + 4]} , {öeg6[i + 4]} , {hg6[i + 4]} , {tarih}" \
                       f"{özellik6[i + 5]} , {kb6[i + 5]} , {öeg6[i + 5]} , {hg6[i + 5]} , {tarih}" \
                       f"{özellik6[i + 6]} , {kb6[i + 6]} , {öeg6[i + 6]} , {hg6[i + 6]} , {tarih}" \
                       f"{özellik6[i + 7]} , {kb6[i + 7]} , {öeg6[i + 7]} , {hg6[i + 7]} , {tarih}" \
                       f"{özellik6[i + 8]} , {kb6[i + 8]} , {öeg6[i + 8]} , {hg6[i + 8]} , {tarih}" \
                       f"{özellik6[i + 9]} , {kb6[i + 9]} , {öeg6[i + 9]} , {hg6[i + 9]} , {tarih}" \
                       f"{özellik6[i + 10]} , {kb6[i + 10]} , {öeg6[i + 10]} , {hg6[i + 10]} , {tarih}" \
                       f"{özellik6[i + 11]} , {kb6[i + 11]} , {öeg6[i + 11]} , {hg6[i + 11]} , {tarih}" \
                       f"{özellik6[i + 12]} , {kb6[i + 12]} , {öeg6[i + 12]} , {hg6[i + 12]} , {tarih}" \
                       f"{özellik6[i + 13]} , {kb6[i + 13]} , {öeg6[i + 13]} , {hg6[i + 13]} , {tarih}" \
                       f"{özellik6[i + 14]} , {kb6[i + 14]} , {öeg6[i + 14]} , {hg6[i + 14]} , {tarih}  "\
                       f"{özellik6[i + 15]} , {kb6[i + 15]} , {öeg6[i + 15]} , {hg6[i + 15]} , {tarih}  "\
                       f"{özellik6[i + 16]} , {kb6[i + 16]} , {öeg6[i + 16]} , {hg6[i + 16]} , {tarih}  "
            return render_template("checklistbutonları.html")
        elif request.form.get('7.Kendini algılama') :
            Özellikheader = '7.Kendini algılama'
            i = 1
            kısım = 7
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik7 = [None] * 3
            # kb=arr.array('','')
            kb7 = [None] * 3
            # öeg=arr.array('','')
            öeg7 = [None] * 3
            # hg=arr.array('','')
            hg7 = [None] * 3

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '175-Anksiyete düzeyini belirleme'and '176-Anksiyetesi olan bireye yaklaşımda bulunma'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik7[i] = özellik1
                kb7[i] = kb1
                öeg7[i] = öeg1
                hg7[i] = hg1

                print(f"{özellik7[i]}{kb7[i]}{hg7[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik7[i], kb1=kb7[i], öeg1=öeg7[i], hg1=hg7[i], tarih1=tarih,
                                   Özellik2=özellik7[i + 1], kb2=kb7[i + 1], öeg2=öeg7[i + 1], hg2=hg7[i + 1],
                                   tarih2=tarih

                                   )

            for i in range(1, 3):
                return f" {özellik7[i]} , {kb7[i]} , {öeg7[i]} , {hg7[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik7[i + 1]} , {kb7[i + 1]} , {öeg7[i + 1]} , {hg7[i + 1]} , {tarih}   " \



            return render_template("checklistbutonları.html")
        elif request.form.get('8.Rol-ilişki') :
            Özellikheader = '8.Rol-ilişki'
            i = 1
            kısım = 8
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik8 = [None] * 3
            # kb=arr.array('','')
            kb8 = [None] * 3
            # öeg=arr.array('','')
            öeg8 = [None] * 3
            # hg=arr.array('','')
            hg8= [None] * 3

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '177-Hasta ile iletişim/görüşme yapma' and '178-Psikiyatri hastasıyla ilgili gözlem yazma'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik8[i] = özellik1
                kb8[i] = kb1
                öeg8[i] = öeg1
                hg8[i] = hg1

                print(f"{özellik8[i]}{kb8[i]}{hg8[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik8[i], kb1=kb8[i], öeg1=öeg8[i], hg1=hg8[i], tarih1=tarih,
                                   Özellik2=özellik8[i + 1], kb2=kb8[i + 1], öeg2=öeg8[i + 1], hg2=hg8[i + 1],
                                   tarih2=tarih


                                   )

            for i in range(1, 3):
                return f" {özellik8[i]} , {kb8[i]} , {öeg8[i]} , {hg8[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik8[i + 1]} , {kb8[i + 1]} , {öeg8[i + 1]} , {hg8[i + 1]} , {tarih}   " \



            return render_template("checklistbutonları.html")
        elif request.form.get('9.Cinsellik -Üreme') :
            Özellikheader = '9.Cinsellik -Üreme'
            i = 1
            kısım = 9
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik9 = [None] * 12
            # kb=arr.array('','')
            kb9 = [None] * 12
            # öeg=arr.array('','')
            öeg9 = [None] * 12
            # hg=arr.array('','')
            hg9 = [None] * 12

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '179-Kendi kendine meme muayenesi öğretilmesi 'and '189-Aile planlaması eğitimi '"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik9[i] = özellik1
                kb9[i] = kb1
                öeg9[i] = öeg1
                hg9[i] = hg1

                print(f"{özellik9[i]}{kb9[i]}{hg9[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik9[i], kb1=kb9[i], öeg1=öeg9[i], hg1=hg9[i], tarih1=tarih,
                                   Özellik2=özellik9[i + 1], kb2=kb9[i + 1], öeg2=öeg9[i + 1], hg2=hg9[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik9[i + 2], kb3=kb9[i + 2], öeg3=öeg9[i + 2], hg3=hg9[i + 2],
                                   tarih3=tarih,
                                   Özellik4=özellik9[i + 3], kb4=kb9[i + 3], öeg4=öeg9[i + 3], hg4=hg9[i + 3],
                                   tarih4=tarih,
                                   Özellik5=özellik9[i + 4], kb5=kb9[i + 4], öeg5=öeg9[i + 4], hg5=hg9[i + 4],
                                   tarih5=tarih,
                                   Özellik6=özellik9[i + 5], kb6=kb9[i + 5], öeg6=öeg9[i + 5], hg6=hg9[i + 5],
                                   tarih6=tarih,
            Özellik7 = özellik9[i+6], kb7 = kb9[i+6], öeg7 = öeg9[i+6], hg7 = hg9[i+6], tarih7 = tarih,
            Özellik8 = özellik9[i + 7], kb8 = kb9[i + 7], öeg8 = öeg9[i + 7], hg8 = hg9[i + 7],
            tarih8 = tarih,
            Özellik9 = özellik9[i + 8], kb9 = kb9[i + 8], öeg9 = öeg9[i + 8], hg9 = hg9[i + 8],
            tarih9 = tarih,
            Özellik10 = özellik9[i + 9], kb10 = kb9[i + 9], öeg10 = öeg9[i + 9], hg10 = hg9[i + 9],
            tarih10 =tarih,
            Özellik11=özellik9[i + 10], kb11=kb9[i + 10], öeg11=öeg9[i + 10], hg11=hg9[i + 10],
            tarih11=tarih
                             )

            for i in range(1, 11):
                return f" {özellik9[i]} , {kb9[i]} , {öeg9[i]} , {hg9[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik9[i + 1]} , {kb9[i + 1]} , {öeg9[i + 1]} , {hg9[i + 1]} , {tarih}   " \
                       f"   {özellik9[i + 2]} , {kb9[i + 2]} , {öeg9[i + 2]} , {hg9[i + 2]} , {tarih}" \
                       f"    {özellik9[i + 3]} , {kb9[i + 3]} , {öeg9[i + 3]} , {hg9[i + 3]} , {tarih}" \
                       f"{özellik9[i + 4]} , {kb9[i + 4]} , {öeg9[i + 4]} , {hg9[i + 4]} , {tarih}" \
                       f"{özellik9[i + 5]} , {kb9[i + 5]} , {öeg9[i + 5]} , {hg9[i + 5]} , {tarih}" \
                       f"{özellik9[i + 6]} , {kb9[i + 6]} , {öeg9[i + 6]} , {hg9[i + 6]} , {tarih}" \
                       f"{özellik9[i + 7]} , {kb9[i + 7]} , {öeg9[i + 7]} , {hg9[i + 7]} , {tarih}" \
                       f"{özellik9[i + 8]} , {kb9[i + 8]} , {öeg9[i + 8]} , {hg9[i + 8]} , {tarih}" \
                       f"{özellik9[i + 9]} , {kb9[i + 9]} , {öeg9[i + 9]} , {hg9[i + 9]} , {tarih}" \
                       f"{özellik9[i + 10]} , {kb9[i + 10]} , {öeg9[i + 10]} , {hg9[i + 10]} , {tarih}" \


            return render_template("checklistbutonları.html")
        elif request.form.get('10.Başetme-Stres toleransı ') :
            Özellikheader = '10.Başetme-Stres toleransı '
            i = 1
            kısım = 10
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik10 = [None] * 4
            # kb=arr.array('','')
            kb10 = [None] * 4
            # öeg=arr.array('','')
            öeg10 = [None] * 4
            # hg=arr.array('','')
            hg10 = [None] * 4

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '190-Başetme yöntemlerini değerlendirme'and '192-Kendine zarar verme riski olan hastaya yönelik önlemleri alma'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik10[i] = özellik1
                kb10[i] = kb1
                öeg10[i] = öeg1
                hg10[i] = hg1

                print(f"{özellik10[i]}{kb10[i]}{hg10[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik10[i], kb1=kb10[i], öeg1=öeg10[i], hg1=hg10[i], tarih1=tarih,
                                   Özellik2=özellik10[i + 1], kb2=kb10[i + 1], öeg2=öeg10[i + 1], hg2=hg10[i + 1],
                                   tarih2=tarih,
                                   Özellik3=özellik10[i + 2], kb3=kb10[i + 2], öeg3=öeg10[i + 2], hg3=hg10[i + 2],
                                   tarih3=tarih,


                                   )
            for i in range(1, 4):
                return f" {özellik10[i]} , {kb10[i]} , {öeg10[i]} , {hg10[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik10[i + 1]} , {kb10[i + 1]} , {öeg10[i + 1]} , {hg10[i + 1]} , {tarih}   " \
                       f"   {özellik10[i + 2]} , {kb10[i + 2]} , {öeg10[i + 2]} , {hg10[i + 2]} , {tarih}" \


            return render_template("checklistbutonları.html")
        elif request.form.get('11.Değer- İnanç') :
            Özellikheader ='11.Değer- İnanç'
            i = 1
            kısım = 11
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik11 = [None] * 2
            # kb=arr.array('','')
            kb11 = [None] * 2
            # öeg=arr.array('','')
            öeg11 = [None] * 2
            # hg=arr.array('','')
            hg11 = [None] * 2

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik ='193-Hastanın mahremiyetini ve bilgi gizliliğini koruma'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik11[i] = özellik1
                kb11[i] = kb1
                öeg11[i] = öeg1
                hg11[i] = hg1


                print(f"{özellik11[i]}{kb11[i]}{hg11[i]},index:{i}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1

            return render_template("checklist.html", Özellik=Özellikheader,
                                   Özellik1=özellik11[i], kb1=kb11[i], öeg1=öeg11[i], hg1=hg11[i], tarih1=tarih,


                                   )

            return f" {özellik11[i]} , {kb11[i]} , {öeg11[i]} , {hg11[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \


            return render_template("checklistbutonları.html")
        elif request.form.get('Diğer Uygulamalar (Hastanın kabulü, teslimi, formların kullanımı) '):
            Özellikheader='Diğer Uygulamalar (Hastanın kabulü, teslimi, formların kullanımı) '
            i = 1
            kısım = 12
            numara = session['num']
            öğrenciad = f"select name,surname from users where id='{numara}'"
            cursor.execute(öğrenciad)
            users = cursor.fetchall()
            for isim, soyisim in users:
                ad = isim
                soyad = soyisim

            secim = session['secim']
            print(numara, secim, kısım)
            # özellik=arr.array('','')
            özellik12 = [None] * 7
            # kb=arr.array('','')
            kb12 = [None] * 7
            # öeg=arr.array('','')
            öeg12 = [None] * 7
            # hg=arr.array('','')
            hg12 = [None] * 7

            slctclass1 = f"SELECT Özellik,kb{secim},Öeg{secim},hg{secim}   FROM {ad}{soyad}{numara}checklist where Özellik between '194-Hastanın servise kabulü'and '199-Exitus Hazırlığı'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik12[i] = özellik1
                kb12[i] = kb1
                öeg12[i] = öeg1
                hg12[i] = hg1


                print(f"{özellik12[i]},{kb12[i]},{hg12[i]}")
                i = i + 1
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 1
            return render_template("checklist.html",Özellik=Özellikheader,
                                                    Özellik1=özellik12[i],kb1=kb12[i],öeg1=öeg12[i],hg1=hg12[i],tarih1=tarih,
                                                    Özellik2=özellik12[i+1],kb2=kb12[i+1],öeg2=öeg12[i+1],hg2=hg12[i+1],tarih2=tarih,
                                                    Özellik3=özellik12[i+2],kb3=kb12[i+2],öeg3=öeg12[i+2],hg3=hg12[i+2],tarih3=tarih,
                                                    Özellik4=özellik12[i+3], kb4=kb12[i+3], öeg4=öeg12[i+3], hg4=hg12[i+3], tarih4=tarih,
                                                    Özellik5=özellik12[i + 4],kb5 = kb12[i + 4], öeg5 = öeg12[i + 4], hg5 = hg12[i + 4], tarih5 = tarih,
                                                    Özellik6=özellik12[i + 5], kb6=kb12[i + 5], öeg6=öeg12[i + 5], hg6=hg12[i + 5],tarih6=tarih



                                                                                                                            )
            for i in range(1, 7):
                return f" {özellik12[i]} , {kb12[i]} , {öeg12[i]} , {hg12[i]} , {tarih}" \
                       f"  -------------------------------                                                      " \
                       f" {özellik12[i + 1]} , {kb12[i + 1]} , {öeg12[i + 1]} , {hg12[i + 1]} , {tarih}   " \
                       f"   {özellik12[i + 2]} , {kb12[i + 2]} , {öeg12[i + 2]} , {hg12[i + 2]} , {tarih}" \
                       f"    {özellik12[i + 3]} , {kb12[i + 3]} , {öeg12[i + 3]} , {hg12[i + 3]} , {tarih}" \
                       f"{özellik12[i + 4]} , {kb12[i + 4]} , {öeg12[i + 4]} , {hg12[i + 4]} , {tarih}" \
                       f"{özellik12[i + 5]} , {kb12[i + 5]} , {öeg12[i + 5]} , {hg12[i + 5]} , {tarih}" \

            return render_template("checklistbutonları.html")


    elif request.method=='GET':
        return render_template("checklistbutonları.html")



@app.route("/sınıfbutonları",methods=['get','post'])
def sınıf_butonları():
    if request.method=='POST':

        if request.form.get('1.sınıf'):
            session['secim'] = 1
            return redirect("checklistbutonları")
            i=1
            özellik=' '
            numara= session['cid']
            ad = session['cad']
            soyad=session['csoyad']
            özellik = [None] * 28
            # kb=arr.array('','')
            kb = [None] * 28
            # öeg=arr.array('','')
            öeg = [None] * 28
            # hg=arr.array('','')
            hg = [None] * 28

            slctclass1 = f"SELECT Özellik,kb1,Öeg1,hg1   FROM {ad}{soyad}{numara}checklist where Özellik between '001-Hastanın kimliğini doğrulama 'and '028-Hastanın taburcu edilmesi'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik[i] = özellik1
                kb[i] = kb1
                öeg[i] = öeg1
                hg[i] = hg1

                i = i + 1
                print(f"{özellik}{kb1}{hg1}")
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 2
            for i in range(1, 27):
                return f" {özellik[i]} , {kb[i]} , {öeg[i]} , {hg[i]} , {tarih}" \
                       f"  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 1]} , {kb[i + 1]} , {öeg[i + 1]} , {hg[i + 1]} , {tarih}   " \
                       f"  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"   {özellik[i + 2]} , {kb[i + 2]} , {öeg[i + 2]} , {hg[i + 2]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"    {özellik[i + 3]} , {kb[i + 3]} , {öeg[i + 3]} , {hg[i + 3]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 4]} , {kb[i + 4]} , {öeg[i + 4]} , {hg[i + 4]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 5]} , {kb[i + 5]} , {öeg[i + 5]} , {hg[i + 5]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 6]} , {kb[i + 6]} , {öeg[i + 6]} , {hg[i + 6]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 7]} , {kb[i + 7]} , {öeg[i + 7]} , {hg[i + 7]} , {tarih}" \
                       f"  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 8]} , {kb[i + 8]} , {öeg[i + 8]} , {hg[i + 8]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 9]} , {kb[i + 9]} , {öeg[i + 9]} , {hg[i + 9]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 10]} , {kb[i + 10]} , {öeg[i + 10]} , {hg[i + 10]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 11]} , {kb[i + 11]} , {öeg[i + 11]} , {hg[i + 11]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 12]} , {kb[i + 12]} , {öeg[i + 12]} , {hg[i + 12]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 13]} , {kb[i + 13]} , {öeg[i + 13]} , {hg[i + 13]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 14]} , {kb[i + 14]} , {öeg[i + 14]} , {hg[i + 14]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 15]} , {kb[i + 15]} , {öeg[i + 15]} , {hg[i + 15]} , {tarih} " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 16]} , {kb[i + 16]} , {öeg[i + 16]} , {hg[i + 16]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 17]} , {kb[i + 17]} , {öeg[i + 17]} , {hg[i + 17]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 18]} , {kb[i + 18]} , {öeg[i + 18]} , {hg[i + 18]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 19]} , {kb[i + 19]} , {öeg[i + 19]} , {hg[i + 19]} , {tarih}" \
                       f" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 20]} , {kb[i + 20]} , {öeg[i + 20]} , {hg[i + 20]} , {tarih}  " \
                       f"----------------------------------------------------------------------------------"\
                       f"{özellik[i + 21]} , {kb[i + 21]} , {öeg[i + 21]} , {hg[i + 21]} , {tarih}"\
                       f"{özellik[i + 22]} , {kb[i + 22]} , {öeg[i + 22]} , {hg[i + 22]} , {tarih}"\
                       f"{özellik[i + 23]} , {kb[i + 23]} , {öeg[i + 23]} , {hg[i + 23]} , {tarih}"\
                       f"{özellik[i + 24]} , {kb[i + 24]} , {öeg[i + 24]} , {hg[i + 24]} , {tarih}"


        elif request.form.get('2.sınıf'):
            i = 1
            session['secim'] = 2
            return redirect("checklistbutonları")
            özellik = ' '
            numara = session['cid']
            ad = session['cad']
            soyad = session['csoyad']
            özellik = [None] * 28
            # kb=arr.array('','')
            kb = [None] * 28
            # öeg=arr.array('','')
            öeg = [None] * 28
            # hg=arr.array('','')
            hg = [None] * 28

            slctclass1 = f"SELECT Özellik,kb2,Öeg2,hg2   FROM {ad}{soyad}{numara}checklist where Özellik between '001-Hastanın kimliğini doğrulama 'and '028-Hastanın taburcu edilmesi'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik[i] = özellik1
                kb[i] = kb1
                öeg[i] = öeg1
                hg[i] = hg1

                i = i + 1
                print(f"{özellik}{kb1}{hg1}")
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 2
            for i in range(1, 27):
                return f" {özellik[i]} , {kb[i]} , {öeg[i]} , {hg[i]} , {tarih}" \
                       f"  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 1]} , {kb[i + 1]} , {öeg[i + 1]} , {hg[i + 1]} , {tarih}   " \
                       f"  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"   {özellik[i + 2]} , {kb[i + 2]} , {öeg[i + 2]} , {hg[i + 2]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"    {özellik[i + 3]} , {kb[i + 3]} , {öeg[i + 3]} , {hg[i + 3]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 4]} , {kb[i + 4]} , {öeg[i + 4]} , {hg[i + 4]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 5]} , {kb[i + 5]} , {öeg[i + 5]} , {hg[i + 5]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 6]} , {kb[i + 6]} , {öeg[i + 6]} , {hg[i + 6]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 7]} , {kb[i + 7]} , {öeg[i + 7]} , {hg[i + 7]} , {tarih}" \
                       f"  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 8]} , {kb[i + 8]} , {öeg[i + 8]} , {hg[i + 8]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 9]} , {kb[i + 9]} , {öeg[i + 9]} , {hg[i + 9]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 10]} , {kb[i + 10]} , {öeg[i + 10]} , {hg[i + 10]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 11]} , {kb[i + 11]} , {öeg[i + 11]} , {hg[i + 11]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 12]} , {kb[i + 12]} , {öeg[i + 12]} , {hg[i + 12]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 13]} , {kb[i + 13]} , {öeg[i + 13]} , {hg[i + 13]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 14]} , {kb[i + 14]} , {öeg[i + 14]} , {hg[i + 14]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 15]} , {kb[i + 15]} , {öeg[i + 15]} , {hg[i + 15]} , {tarih} " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 16]} , {kb[i + 16]} , {öeg[i + 16]} , {hg[i + 16]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 17]} , {kb[i + 17]} , {öeg[i + 17]} , {hg[i + 17]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 18]} , {kb[i + 18]} , {öeg[i + 18]} , {hg[i + 18]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 19]} , {kb[i + 19]} , {öeg[i + 19]} , {hg[i + 19]} , {tarih}" \
                       f" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 20]} , {kb[i + 20]} , {öeg[i + 20]} , {hg[i + 20]} , {tarih}  " \
                       f"----------------------------------------------------------------------------------"


        elif request.form.get('3.sınıf'):
            i = 1
            session['secim'] = 3
            return redirect("checklistbutonları")
            özellik = ' '
            numara = session['cid']
            ad = session['cad']
            soyad = session['csoyad']
            özellik = [None] * 28
            # kb=arr.array('','')
            kb = [None] * 28
            # öeg=arr.array('','')
            öeg = [None] * 28
            # hg=arr.array('','')
            hg = [None] * 28

            slctclass1 = f"SELECT Özellik,kb3,Öeg3,hg3   FROM {ad}{soyad}{numara}checklist where Özellik between '001-Hastanın kimliğini doğrulama 'and '028-Hastanın taburcu edilmesi'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik[i] = özellik1
                kb[i] = kb1
                öeg[i] = öeg1
                hg[i] = hg1

                i = i + 1
                print(f"{özellik}{kb1}{hg1}")
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 2
            for i in range(1, 27):
                return f" {özellik[i]} , {kb[i]} , {öeg[i]} , {hg[i]} , {tarih}" \
                       f"  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 1]} , {kb[i + 1]} , {öeg[i + 1]} , {hg[i + 1]} , {tarih}   " \
                       f"  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"   {özellik[i + 2]} , {kb[i + 2]} , {öeg[i + 2]} , {hg[i + 2]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"    {özellik[i + 3]} , {kb[i + 3]} , {öeg[i + 3]} , {hg[i + 3]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 4]} , {kb[i + 4]} , {öeg[i + 4]} , {hg[i + 4]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 5]} , {kb[i + 5]} , {öeg[i + 5]} , {hg[i + 5]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 6]} , {kb[i + 6]} , {öeg[i + 6]} , {hg[i + 6]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 7]} , {kb[i + 7]} , {öeg[i + 7]} , {hg[i + 7]} , {tarih}" \
                       f"  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 8]} , {kb[i + 8]} , {öeg[i + 8]} , {hg[i + 8]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 9]} , {kb[i + 9]} , {öeg[i + 9]} , {hg[i + 9]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 10]} , {kb[i + 10]} , {öeg[i + 10]} , {hg[i + 10]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 11]} , {kb[i + 11]} , {öeg[i + 11]} , {hg[i + 11]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 12]} , {kb[i + 12]} , {öeg[i + 12]} , {hg[i + 12]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 13]} , {kb[i + 13]} , {öeg[i + 13]} , {hg[i + 13]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 14]} , {kb[i + 14]} , {öeg[i + 14]} , {hg[i + 14]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 15]} , {kb[i + 15]} , {öeg[i + 15]} , {hg[i + 15]} , {tarih} " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 16]} , {kb[i + 16]} , {öeg[i + 16]} , {hg[i + 16]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 17]} , {kb[i + 17]} , {öeg[i + 17]} , {hg[i + 17]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 18]} , {kb[i + 18]} , {öeg[i + 18]} , {hg[i + 18]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 19]} , {kb[i + 19]} , {öeg[i + 19]} , {hg[i + 19]} , {tarih}" \
                       f" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 20]} , {kb[i + 20]} , {öeg[i + 20]} , {hg[i + 20]} , {tarih}  " \
                       f"----------------------------------------------------------------------------------"


        elif request.form.get('4.sınıf') :
            i = 1
            session['secim'] = 4
            return redirect("checklistbutonları")
            özellik = ' '
            numara = session['cid']
            ad = session['cad']
            soyad = session['csoyad']
            özellik = [None] * 28
            # kb=arr.array('','')
            kb = [None] * 28
            # öeg=arr.array('','')
            öeg = [None] * 28
            # hg=arr.array('','')
            hg = [None] * 28

            slctclass1 = f"SELECT Özellik,kb4,Öeg4,hg4   FROM {ad}{soyad}{numara}checklist where Özellik between '001-Hastanın kimliğini doğrulama 'and '028-Hastanın taburcu edilmesi'"
            cursor.execute(slctclass1)
            öğrencikarne = f"{ad}{soyad}{numara}checklist"
            öğrencikarne = cursor.fetchall()
            for özellik1, kb1, öeg1, hg1 in öğrencikarne:
                özellik[i] = özellik1
                kb[i] = kb1
                öeg[i] = öeg1
                hg[i] = hg1

                i = i + 1
                print(f"{özellik}{kb1}{öeg1}{hg1}")
                tarihfunc = today = datetime.datetime.today()
                tarih = f"{today.day}-{today.month}-{today.year}"
            i = 0
            for i in range(0, 28):
                return f" {özellik[i]} , {kb[i]} , {öeg[i]} , {hg[i]} , {tarih}" \
                       f"  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 1]} , {kb[i + 1]} , {öeg[i + 1]} , {hg[i + 1]} , {tarih}   " \
                       f"  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"   {özellik[i + 2]} , {kb[i + 2]} , {öeg[i + 2]} , {hg[i + 2]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"    {özellik[i + 3]} , {kb[i + 3]} , {öeg[i + 3]} , {hg[i + 3]} , {tarih}" \
                       f"  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 4]} , {kb[i + 4]} , {öeg[i + 4]} , {hg[i + 4]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 5]} , {kb[i + 5]} , {öeg[i + 5]} , {hg[i + 5]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 6]} , {kb[i + 6]} , {öeg[i + 6]} , {hg[i + 6]} , {tarih}" \
                       f"  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 7]} , {kb[i + 7]} , {öeg[i + 7]} , {hg[i + 7]} , {tarih}" \
                       f"  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 8]} , {kb[i + 8]} , {öeg[i + 8]} , {hg[i + 8]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 9]} , {kb[i + 9]} , {öeg[i + 9]} , {hg[i + 9]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 10]} , {kb[i + 10]} , {öeg[i + 10]} , {hg[i + 10]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 11]} , {kb[i + 11]} , {öeg[i + 11]} , {hg[i + 11]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 12]} , {kb[i + 12]} , {öeg[i + 12]} , {hg[i + 12]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 13]} , {kb[i + 13]} , {öeg[i + 13]} , {hg[i + 13]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 14]} , {kb[i + 14]} , {öeg[i + 14]} , {hg[i + 14]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 15]} , {kb[i + 15]} , {öeg[i + 15]} , {hg[i + 15]} , {tarih} " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 16]} , {kb[i + 16]} , {öeg[i + 16]} , {hg[i + 16]} , {tarih}  " \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 17]} , {kb[i + 17]} , {öeg[i + 17]} , {hg[i + 17]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 18]} , {kb[i + 18]} , {öeg[i + 18]} , {hg[i + 18]} , {tarih}" \
                       f"  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f"{özellik[i + 19]} , {kb[i + 19]} , {öeg[i + 19]} , {hg[i + 19]} , {tarih}" \
                       f" -----------------------------------------------------------------------------------------------------------------------------------------------------------------------" \
                       f" {özellik[i + 20]} , {kb[i + 20]} , {öeg[i + 20]} , {hg[i + 20]} , {tarih}  " \
                       f"----------------------------------------------------------------------------------"\
                       f" {özellik[i + 21]} , {kb[i + 21]} , {öeg[i + 21]} , {hg[i + 21]} , {tarih}  " \
                       f"----------------------------------------------------------------------------------"\
                       f" {özellik[i + 22]} , {kb[i + 22]} , {öeg[i + 22]} , {hg[i + 22]} , {tarih}  " \
                       f"----------------------------------------------------------------------------------"



    elif request.method=='GET':
        return render_template("sınıfbutonları.html")




@app.route("/searchuser",methods=['GET'])
def searchuser():
    return render_template("search.html")


@app.route("/searchuser",methods=['POST'])
def searchuser_post():
    id=request.form.get("id")
    searchwithid = f"SELECT id,name,surname,password,rol  FROM users WHERE id= '{id}'"
    cursor.execute(searchwithid)
    users = cursor.fetchall()
    print(f"{id}")
    for usernum,username,usersurname,userpassword,userrol in users:
        if usernum==id or f'{id}':
            id=usernum
            name=username
            surname=usersurname
            password=userpassword
            rol=userrol

            break



    print(id,name,surname,password,rol)
    #user = request.json


   # user=[{id},{name},{surname},{password},{rol}]
    roladı=None
    if rol==False:
        roladı='öğrenci'
    else:
        roladı='prof-hemşire'

    #return jsonify(user)
    return f"{id,name,surname,rol,roladı}"






@app.errorhandler(404)
def error(hata):
    return render_template("404.html")

@app.errorhandler(500)
def error500(hata500):
    return render_template("500.html")



if __name__== "__main__":
    app.debug=True
    app.run()
"""@app.route('/', methods=['GET'])
def get():
    response = {
        'message': 'Hi, there!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

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
# ozellikleri de ekleyebilirsiniz."""
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
