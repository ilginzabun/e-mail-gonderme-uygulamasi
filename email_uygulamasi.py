import smtplib
""" 'smtplib' : python'un kütüphanesinde yer alan e-posta gönderimi işlemi için kullanılan modül.  """
from email.mime.text import MIMEText
""" 'MIMEText' : e-posta içeriğinin düz metin ya da HTML formatında oluşturmak için kullanılır. MIME (Multipurpose Internet Mail Extensions) standardına uygun bir şekilde biçimlendirilir. Bu, e-posta alıcısının mesajı doğru bir şekilde görüntüleyebilmesini sağlar. """
from email.mime.multipart import MIMEMultipart
""" 'MIMEMultipart' :  bir e-posta içinde hem düz metin hem de HTML formatını aynı anda göndermek istediğinizde kullanılır. Bu sayede, alıcının e-posta istemcisi HTML'i desteklemiyorsa bile mesajın düz metin versiyonu gösterilebilir."""


# e-posta detayları : 
gonderici_email = (input(" Gönderici maili : "))
alici_email = (input(" Alıcı maili : "))
sifre = input("Şifrenizi giriniz : ") 
"""şifre uygulama şifresi olmalıdır. bunun için iki aşamalı kimlik doğrulamanızın etkinleştirilmiş olması lazımdır."""


# e-posta oluşturma :
mesaj = MIMEMultipart("alternative") 
""" e-postanın içeriğinin aynnı mesajda bir araya getirmek için kullanılır. 
'alternative' parametresi, e-posta içeriğinin alternatif formatlarda sunulmasını sağlar.
"""
mesaj["Subject"] = "Test Email" 
mesaj["From"] = gonderici_email
mesaj["To"] = alici_email


# e-posta :
metin = "Merhaba, bu bir deneme amaçlı gönderilmiş maildir."
""" E-postanın düz metin içeriğini belirler. """
html = "<html><body><p>Merhaba, bu bir deneme amaçlı gönderilmiş maildir.</p></body></html>"
""" E-postanın HTML formatındaki içeriğini belirler. """


# E-posta içeriğini MIME türünde ekleme
parca1 = MIMEText(metin, "plain")
""" metin değişkeni, e-postanın düz metin içeriğini içerir. MIMEText sınıfı bu metni e-posta içeriği olarak biçimlendirir
ve "plain" parametresi, içeriğin düz metin olduğunu belirtir. """
parca2 = MIMEText(html, "html")
"""  e-posta mesajının HTML formatındaki içeriğini oluşturur. html değişkeni, e-postanın HTML formatındaki içeriğini içerir. 
MIMEText sınıfı bu içeriği e-posta içeriği olarak biçimlendirir ve "html" parametresi, içeriğin HTML formatında olduğunu belirtir. """
mesaj.attach(parca1)
""" e-posta mesajınızın içeriğini oluşturduğunuzda, bu içeriği mesajınıza eklemek için attach metodunu kullanırsınız. """
""" Bu satır, oluşturulan düz metin içeriğini (parca1) mesaj nesnesine ekler. mesaj nesnesi, daha önce MIMEMultipart("alternative") 
ile oluşturulmuş olan e-posta mesajını temsil eder. Bu ekleme işlemi, e-posta mesajına düz metin içeriğini dahil eder. """
mesaj.attach(parca2)
""" oluşturulan HTML içeriğini (parca2) mesaj nesnesine ekler. Bu, e-posta mesajına HTML içeriğini dahil eder. """


# E-posta gönderme
try: 
    """  e-posta gönderme işlemini denemek için try bloğu"""
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: 
        """Güvenli bir SMTP bağlantısı oluşturuluyor (Gmail için SSL kullanılıyor)"""
        server.login(gonderici_email, sifre) # Uygulama şifresi ile kimlik doğrulama
        server.sendmail(gonderici_email, alici_email, mesaj.as_string())
    print("E-posta başarıyla gönderildi!")
except Exception as e:
    print(f"E-posta gönderilirken bir hata oluştu: {e}")
""" Hata durumunda bilgi verir. """