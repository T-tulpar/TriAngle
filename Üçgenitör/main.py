from Base_Triangle import TriAngle as Ta  # Üçgen sınıfını tanımladığımız dosyadan üçgen sınıfını Ta olarak import ediyoruz


def check_none(i):  # Base dosyasında yaptığımız gibi Burda da input değer girilmediğinde None değil '' döndürdüğü için Bu değeri None'a Çeviriyoruz Ayrıca dönen değeri de int yapıyoruz ki str olmasın
    return int(i) if i != '' else None
    pass


x = (check_none(input("Üçgenin X Açısını girin:")))
y = (check_none(input("Üçgenin Y Açısını girin:")))
z = (check_none(input("Üçgenin Z Açısını girin:")))
a = (check_none(input("Üçgenin X Köşesini girin:")))
b = (check_none(input("Üçgenin Y Köşesini girin:")))
c = (check_none(input("Üçgenin Z Köşesini girin:")))

ta = Ta(x, y, z, a, b, c)
