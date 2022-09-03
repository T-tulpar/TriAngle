# Kendime Notlar

# lambda x: x + 10
# *args **kwargs işe yarar olabilir
# iç içe fonskiyonlar
# üreteçler

# sys path ile modül

# static method işlemler için belki lambda ile hoş gider

import math


class TriAngle:
    TOT_IN_ANG = 180  # Aynı zamanda iç ve dış açının toplamı olarak da kullanılacaktır.
    TOT_OUT_ANG = 360  #
    SIDE_COUNT = 3  # Aynı zamanda kenar sayısı için de kullanılacaktır.

    def __init__(self, angx=None, angy=None, angz=None, lenx=None, leny=None, lenz=None):
        self.code = [self.give_code(angx, angy, angz), self.give_code(lenx, leny, lenz)]  # Üçgene verdiğim kod diyebilirim yani üçgenin hangi kenarının hangi açısının olup olmamasına göre bu değer dğişiyor

        self.set(angx, angy, angz, lenx, leny, lenz)  # Üçgenin gerekli hesaplamalar ile set edilmesi yani kenarların ve açıların hesaplanıp set edilmesi

        self.show_prop()  # Üçgenin özelliklerini(prop) söyleyen fonksiyon

    def set(self, angx, angy, angz, lenx, leny, lenz):
        while 1:  # Bu sürekli döngü kısmı önemli çünkü her işlemden sonra tekrar başa dönüp eksik bişeyin kalıp kalmadığını kontrol etmeye yarıyor
            # Misal 2 açı 1 kenar var Önce toplama çıkarma işlemi ile açı sayımızı 3'e tamamlayıp bu bilgi ile diğer  kenarları buluyoruz yoksa 2 açı ile kenar bulamayabiliriz
            self.ang_x = self.check_none(angx)  # Burda bunları yapmamızın nedeni eğer kullanıcı herhangi bir açı veya kenar değerini vermezse hata almadan None düşmesi
            self.ang_y = self.check_none(angy)
            self.ang_z = self.check_none(angz)
            self.len_x = self.check_none(lenx)
            self.len_y = self.check_none(leny)
            self.len_z = self.check_none(lenz)

            self.set_type()  # Burda üçgenin türünü bulunuyor

            self.code = [self.give_code(angx, angy, angz), self.give_code(lenx, leny, lenz)]  # Yukarda Code'nin ne olduğunu söylemiştim burda da olma nedeni her hesaplama sonrası bir kenar veya açı bulunduktan sonra bu değeri değiştirmek

            if self.code[0][0] == 1:  # Burdaki İlk [0] Açı ile ilgilendiğimizi söylüyor İkinci [0] ise Türü sorguluyor. Bu değerin 1 olması ise 3 Açının da tam olduğu anlamına geliyor
                if self.code[1][0] == 1:  # Burdaki ilk [1] Kenar ile ilgilendiğimizi söylüyor İkinci [0] ise Türü sorguluyor. Bu değerin 1 olması da 3 kenarın da tam olduğu anlamına geliyor
                    self.set_ang(angx, angy, angz)
                    self.set_len(lenx, leny, lenz)  # Burda gerekli set işlemleri yapılıyor çünkü gerekli tüm verileri kullanıcı veriyor
                    break  # Döngüyü bitirme nedemim tüm verilerin set edimiş olması
                if self.code[1][0] == 2 or self.code[1][0] == 3:  # Burda 2 Veya 1 Kenar olduğundan bahsediyorum
                    if self.code[1][1] == 1:  # Z is None OR X Not None
                        lenz = self.sin1(lenx, angx, angz)  # Hangi kenar olmasına göre o kenarları kullanarak diğer kenarı buluyorum
                    if self.code[1][1] == 2:  # Y is None OR Z Not None
                        leny = self.sin1(lenz, angz, angy)
                    if self.code[1][1] == 3:  # X is None OR Y Not None
                        lenx = self.sin1(leny, angy, angx)
                if self.code[1][0] == 0:  # Burda Hiç kenar olmayan durumu inceliyorum ve sadece açıları set ediyorum
                    self.set_ang(angx, angy, angz)
                    break
            elif self.code[0][0] == 2:  # 2 Açı varsa demek
                if self.code[0][1] == 1:  # Hangi açının olmadığını kontrol edip ona göre diğer ikisini toplayıp 180 den çıkartıyorum
                    angz = 180 - (angy + angx)
                if self.code[0][1] == 2:
                    angy = 180 - (angz + angx)
                if self.code[0][1] == 3:
                    angx = 180 - (angy + angz)
            elif self.code[0][0] == 3:  # Bu ise tek açı olduğunu söylüyor
                if self.code[1][0] == 1:  # 3 Kenarında olduğu durum
                    if self.code[0][1] == 1:  # X Not None
                        angy = self.sin2(leny, angx, lenx)  # Hangi açı varsa o açı kullanılarak diğer açılar bulunan işlemi yaptırıyorum
                    if self.code[0][1] == 2:  # Y Not None
                        angz = self.sin2(lenz, angy, leny)
                    if self.code[0][1] == 3:  # Z Not None
                        angx = self.cos1(lenx, leny, lenz)[0]
                elif self.code[1][0] == 2:  # 2 Kenarında olduğu durum
                    if self.code[1][1] == 1:  # Z Kenar is None
                        if self.code[0][1] == 1:  # X Açı Not None
                            angy = self.sin2(leny, angx, lenx)  # Burda ise hangi kenar ve açı yok ise ona göre işlemlerimi yapıyorum. Eğer aynı açı ve kenar yoksa gördüğünüz gibi farklı işlem yapıyorum
                        if self.code[0][1] == 2:  # Y Açı Not None
                            angx = self.sin2(lenx, angy, leny)
                        if self.code[0][1] == 3:  # Z Açı Not None
                            lenz = self.cos2(angz, lenx, leny)  # Bakın aynı açı ve kenar olmadığından mütevellit sinüs(2) değil cosinüs(2) Yapıyorum
                    elif self.code[1][1] == 2:  # Y Kenar is None
                        if self.code[0][1] == 1:  # X Açı Not None
                            angz = self.sin2(lenz, angx, lenx)
                        if self.code[0][1] == 2:  # Y Açı Not None
                            lenz = self.cos2(angy, lenx, lenz)
                        if self.code[0][1] == 3:  # Z Açı Not None
                            angx = self.sin2(lenx, angz, lenz)
                    elif self.code[1][1] == 3:  # X Kenar is None
                        if self.code[0][1] == 1:  # X Açı Not None
                            lenx = self.cos2(angx, lenz, leny)
                        if self.code[0][1] == 2:  # Y Açı Not None
                            angz = self.sin2(lenz, angy, leny)
                        if self.code[0][1] == 3:  # Z Açı Not None
                            angy = self.sin2(leny, angz, lenz)  # Buraya kadar Yukarda anlattığım işlem
                else:
                    break  # Döngüye girmemesi için bişey yapmasını belirtmediğim durumlar için döngüyü burda kırıyorum

            elif self.code[0][0] == 0 and self.code[1][0] == 1:  # Burda ise hiç açı yok ama 3 kenar var
                angy = self.cos1(lenx, leny, lenz)[0]  # Bu 3 kenardan yararlanarak cosinüs işlemi ile 2 açıyı buluyorum sonra döngüde olduğumuz için sonra diğer kenarı toplama çıkarma işlemi ile buluyor
                angz = self.cos1(lenx, leny, lenz)[1]
            else:
                break

    def set_ang(self, x, y, z):  # Açı değerlerini set için kullandığım fonksiyon
        x, y, z = self.sort_values(x, y, z)  # Burda büyükten küçüğe değerlerin x,y,z olarak sıralanmasını sağlıyoruz

        st = True  # Situation
        if x + y + z != TriAngle.TOT_IN_ANG:  # Gerekli değerleri kontrol edip ona göre set edip etmiyorum
            st = False
        for ang in x, y, z:
            if ang <= 0:
                st = False
        if st is True:
            self.ang_x = x
            self.ang_y = y
            self.ang_z = z
            self.type_ang = self.find_type_ang()  # değerleri set ettikten sonra Type'ı set ediyorum
        else:
            print("Lütfen Geçerli sayı giriniz")

    def set_len(self, x=None, y=None, z=None):
        x, y, z = self.sort_values(x, y, z)  # Açı da olduğu gibi sıralayıp kontrol edip set ediyorum
        if self.check_side(x, y, z) and self.check_side(y, x, z) and self.check_side(z, x, y):
            self.len_x = x
            self.len_y = y
            self.len_z = z
            self.type_len = self.find_type_len()
        else:
            print("Lütfen Geçerli sayı giriniz")

    def set_type(self):  # Üçgenin 2 Türünün aynı anda set eden işlem
        self.type_ang = self.find_type_ang()
        self.type_len = self.find_type_len()

    def find_type_ang(self):  # Üçgenin açısına göre Türünü buluyor
        i, j = 0, 0
        for ang in self.ang_x, self.ang_y, self.ang_z:
            if ang is None:
                j += 1
                return None
            else:
                if ang == 90:
                    return "Dik Üçgen"
                elif ang > 90:
                    return "Geniş Açılı Üçgen"
                else:
                    i += 1
                    if i == 3:
                        return "Dar Açılı Üçgen"

    def find_type_len(self):  # Üçgenin kenarına göre türünü buluyor
        lens = [self.len_x, self.len_y, self.len_z]
        j = 0
        if self.len_x == self.len_y == self.len_z:
            return "Eşkaner Üçgen"
        else:
            for i in range(0, 2):
                if lens[i] == lens[0]:
                    j += 1
                if lens[i] == lens[1]:
                    j += 1
                if lens[i] == lens[2]:
                    j += 1
            if j == 3:
                return "ikizkenar üçgen"
            else:
                return "Çeşitkenar Üçgen"

    def show_prop(self):  # Üçgenin değerlerini göstermek için fonksiyon
        print(f"Üçgeninin Açıları:{'Yok' if self.ang_x is None else self.ang_x}, {'Yok' if self.ang_y is None else self.ang_y}, {'Yok' if self.ang_z is None else self.ang_z}")
        # Bakın print işlemi için de tek satır da if işlemi kullanıyorum None değer olup olmamasını kontrol edip varsa kendisini None ise 'yok' değerini yazmasını sağlıyorum
        print(f"Üçgeninin Kenar Uzunlukları: {self.len_x}, {self.len_y}, {self.len_z}")
        print(f"Üçgeninin Türü: {self.type_ang} --- {self.type_len} ")

    @staticmethod
    # Static method Self almayan yani nesneye özel olmayan fonksiyon
    def cos1(a, c, b):
        return math.degrees(math.asin(((a * a) + (c * c) - (b * b)) / (2 * c * a))), math.degrees(
            math.asin(((a * a) + (b * b) - (c * c)) / (2 * b * a)))

    @staticmethod
    def cos2(a, b, c, s=15):
        return round(math.sqrt(b * b + c * c - 2 * b * c * math.cos(math.radians(a))), s)  # Diğer kenarı buluyor #
        # a= x açısı b= y kenarı c= z kenarı

    @staticmethod
    def sin1(a, b, c):
        return a * math.sin(math.radians(c)) / math.sin(math.radians(b))

    @staticmethod
    def sin2(a, b, c):
        return math.degrees(math.asin(a * math.sin(math.radians(b)) / c))

    @staticmethod
    def sort_values(*args):  # args yardımı ile sınırsız sayıda verdiğin sayıyı sıralıyor
        # Aslında sadece bu clas için değil her yerde kullanıabilecek bir fonksiyon
        lst = []
        tple = ()  # Normalde listeleri sıralayan bu fonksiyonu liste için de olmayan değerleri sıralamak için tuple yani demet oluşturup
        for i in args:
            lst.append(i)   # Sonra Bu değerleri listeye ekliyip
        lst.sort(reverse=True)  # listelerin fonksiyonundan yararlanıp
        for i in lst:
            tple = tple + (i,)  # tekrer tuple' a döndürüp

        return tple  # return ediyorum

    @staticmethod
    def give_code(x, y, z):  # Burası da Yukarda bahsettiğim code değerinin oluşturulduğu fonksiyon
        if x is not None and y is not None and z is not None:
            return [1, 0]
        elif x is not None and y is not None and z is None:
            return [2, 1]
        elif x is not None and y is None and z is not None:
            return [2, 2]
        elif x is None and y is not None and z is not None:
            return [2, 3]
        else:
            if x is not None:
                return [3, 1]
            elif y is not None:
                return [3, 2]
            elif z is not None:
                return [3, 3]
            else:
                return [0, 0]

    @staticmethod
    def check_none(y):  # Bu fonksiyon da hata almamak adına yaptığım kendi fonksiyonum tanımlı mı diye kontrol ediyor tanımlı değilse Tanımlı deği hatası almamak adına None olarak değer dönüyor
        return y if y is not None else None

    @staticmethod
    def check_side(x, y, z):  # kenar olabilir mi diye kontrol ediyor x değerini
        if y + z > x > abs(y - z):  # Abs Mutlak değer işareti
            return True
        else:
            return False


if __name__ == '__main__':  # Herhangi bir dosyaya import ettiğimizde çalışmaması için bu if'i koyup bu dosya çalışırsa bu kısım çalışıyor ama import ettiğimiz de çalışmıyor
    ta = TriAngle(90, lenx=5, lenz=3)
