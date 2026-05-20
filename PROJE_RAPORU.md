
## BULANIK MANTIK DÖNEM PROJESİ RAPORU

---

**Proje Başlığı:** Mükemmel Filtre Kahve / Çay Demleme Makinesi Bulanık Mantık Kontrolcüsü Tasarımı ve Uygulaması

**Hazırlayan:** Onur Ergençiçeği

**Ders Sorumlusu:** Dönem Projesi Değerlendirme Kurulu

**Öğrenci Numarası:** 22430070017

---

## 1. GİRİŞ VE PROBLEMİN TANIMI

### 1.1. Gerçek Dünya Problemi

Geleneksel filtre kahve ve çay demleme makineleri, su akış hızını ve demleme süresini sabit parametrelerle (genellikle mekanik bir valf veya basit bir zamanlayıcı ile) yürütür. Ancak kahve ve çay demleme işlemleri, kimyasal olarak "ekstraksiyon" (özünüm) süreçleridir. Suyun sıcaklığı, kullanılan kahve/çay miktarı ve suyun mineral yoğunluğu (sertlik) çözünme hızını doğrudan etkiler.

Sabit akış hızı kullanan makinelerde şu problemler yaşanır:

- **Yüksek sıcaklık ve sert su** bir araya geldiğinde kahve/çay aşırı çözünür (*Over-extraction*), bu da içeceği aşırı acı hale getirir.
- **Düşük sıcaklık ve yumuşak su** bir araya geldiğinde ise yeterli çözünme gerçekleşmez (*Under-extraction*), içecek yavan ve gövdesiz kalır.

### 1.2. Giriş ve Çıkış Değişkenlerinin Tanımı

Sistemin dinamik ve lezzetli bir demleme yapabilmesi için **3 giriş** ve **1 çıkış** değişkeni kurgulanmıştır:

| Değişken | Açıklama | Aralık |
|----------|----------|--------|
| **Giriş 1 — Su Sıcaklığı (°C)** | Suyun termal enerjisini temsil eder | [60, 100] |
| **Giriş 2 — Malzeme Miktarı (Gram)** | Hazneye konulan filtre kahve veya çay miktarı | [5, 40] |
| **Giriş 3 — Su Sertliği (dH)** | Suyun Alman sertlik derecesi cinsinden mineral yoğunluğu | [0, 18] |
| **Çıkış — Su Akış Hızı (ml/sn)** | Suyun malzemeyle temas süresini belirleyen ana unsur | [2, 12] |

### 1.3. Bulanık Mantığın Uygunluk Gerekçesi

Demleme işlemindeki optimal dengeler, kesin matematiksel denklemlerle (örneğin diferansiyel denklemlerle) ifade edilemeyecek kadar çok varyasyona sahiptir. "İdeal sıcaklık", "biraz fazla kahve", "orta sertlikte su" gibi insan diline ait kavramsal belirsizlikler mevcuttur.

Bulanık mantık, uzman kahve baristalarının ve çay gurmelerinin deneyimsel kural tabanlarını doğrudan bilgisayar koduna aktarmaya izin verir. Sistem, doğrusal olmayan bu problemi karmaşık sensör kalibrasyonlarına ihtiyaç duymadan, dilsel esneklikle çözebildiği için bulanık mantık modeline tam uyumludur.

---

## 2. SİSTEM TASARIMI

### 2.1. Giriş ve Çıkış Değişkenlerinin Dilsel Tanımlamaları ve Evrensel Kümeleri

Sistemdeki tüm değişkenler için **üçer adet dilsel terim** tanımlanmış ve **üçgensel üyelik fonksiyonları (trimf)** kullanılmıştır.

#### Su Sıcaklığı (Universe: [60 – 100] °C)

| Dilsel Terim | trimf Parametreleri |
|--------------|---------------------|
| Düşük | [60, 60, 80] |
| İdeal | [75, 85, 90] |
| Yüksek | [85, 100, 100] |

#### Malzeme Miktarı (Universe: [5 – 40] Gram)

| Dilsel Terim | trimf Parametreleri |
|--------------|---------------------|
| Az | [5, 5, 15] |
| Normal | [10, 20, 25] |
| Fazla | [20, 40, 40] |

#### Su Sertliği (Universe: [0 – 18] dH)

| Dilsel Terim | trimf Parametreleri |
|--------------|---------------------|
| Yumuşak | [0, 0, 7] |
| Orta | [5, 9, 12] |
| Sert | [10, 18, 18] |

#### Çıkış Değişkeni — Su Akış Hızı (Universe: [2 – 12] ml/sn)

| Dilsel Terim | trimf Parametreleri |
|--------------|---------------------|
| Yavaş | [2, 2, 6] |
| Normal | [5, 7, 9] |
| Hızlı | [8, 12, 12] |

---

### 2.2. Kural Tabanı (Rule Base)

Sistemde `and (&)` mantıksal operatörü (Min operatörü) kullanılarak **15 adet kural** yapılandırılmıştır:

| Kural No | IF (Sıcaklık) | AND (Miktar) | AND (Sertlik) | THEN (Akış Hızı) |
|----------|--------------|-------------|--------------|-----------------|
| Kural 1 | Düşük | Az | Yumuşak | Yavaş |
| Kural 2 | Yüksek | Fazla | Sert | Hızlı |
| Kural 3 | İdeal | Normal | Orta | Normal |
| Kural 4 | Düşük | Fazla | Yumuşak | Yavaş |
| Kural 5 | Yüksek | Az | Orta | Hızlı |
| Kural 6 | İdeal | Fazla | Sert | Normal |
| Kural 7 | Düşük | Normal | Sert | Yavaş |
| Kural 8 | Yüksek | Normal | Yumuşak | Hızlı |
| Kural 9 | İdeal | Az | Yumuşak | Yavaş |
| Kural 10 | Düşük | Fazla | Sert | Yavaş |
| Kural 11 | Yüksek | Az | Sert | Normal |
| Kural 12 | İdeal | Fazla | Yumuşak | Hızlı |
| Kural 13 | Düşük | Az | Orta | Yavaş |
| Kural 14 | Yüksek | Fazla | Orta | Hızlı |
| Kural 15 | İdeal | Normal | Sert | Normal |

---

### 2.3. Çıkarım Motoru ve Durulaştırma (Defuzzification)

Çıkarım motorunda **Mamdani tipi minimum çıkarım yöntemi** tercih edilmiştir. Kuralların tetiklenme dereceleri belirlendikten sonra, çıktı üyelik fonksiyonları kesilir ve bileşke bulanık küme elde edilir.

Durulaştırma aşamasında, çıktının net ve fiziksel olarak bir motor/valf tarafından işlenebilmesi için **Ağırlık Merkezi (Centroid)** metodu kullanılmıştır. Formülasyon şu şekildedir:

$$Z^* = \frac{\int \mu(z) \cdot z \, dz}{\int \mu(z) \, dz}$$

---

## 3. UYGULAMANIN DETAYLARI

### 3.1. Kod Mimarisi ve Algoritmik Akış

Uygulama, Python dilinde **scikit-fuzzy** kütüphanesi üzerine inşa edilmiştir. `numpy` evrensel kümeleri oluştururken, `matplotlib` ise arka planda grafiklerin matematiksel izdüşümlerini çıkarır. Kullanıcı arayüzü (GUI) **Streamlit** kütüphanesiyle reaktif hale getirilmiştir.

### 3.2. Arayüz Tasarımı ve Kullanıcı Deneyimi

Arayüz, akademik sunuma uygun, gözü yormayan ve modern bir **Camgöbeği (Teal — #008080)** renk temasıyla özelleştirilmiştir.

- **Sol Panel (Sidebar/Inputs):** Kullanıcının su sıcaklığını, kahve gramajını ve su sertliğini anlık olarak değiştirebileceği dinamik slider'lar içerir. Hemen altında "Hesapla" tetikleyici butonu yer alır.

- **Sağ Panel (Outputs/Visuals):** Hesaplanan net akış hızını mililitre/saniye (ml/sn) cinsinden büyük bir başarı kartı (success box) ile sunar. Altında ise Ağırlık Merkezi kesişim çizgisini içeren durulaştırma grafiği ve giriş değişkenlerinin üyelik fonksiyonu grafiklerini barındırır.

---

## 4. TEST SONUÇLARI VE ANALİZ

Sistemin kararlılığını doğrulamak amacıyla **3 ekstrem senaryo** üzerinde simülasyon gerçekleştirilmiştir:

---

### Senaryo 1: Ekstrem Acılaşma Riski (Over-extraction Önleme)

- **Girişler:** Sıcaklık = 98°C (Yüksek), Miktar = 38 Gr (Fazla), Sertlik = 16 dH (Sert)
- **Beklenen Davranış:** Suyun aşırı sıcak ve sert olması çözünmeyi tavan yaptırır. Yanık tadı engellemek için akış çok hızlı olmalıdır.
- **Hesaplanan Çıktı:** ~**10.45 ml/sn** (Hızlı)
- **Yorum:** Sistem başarıyla acılaşmayı önlemek için su akış hızını maksimuma yaklaştırmıştır. ✅

---

### Senaryo 2: Yavan Kalma Riski (Under-extraction Önleme)

- **Girişler:** Sıcaklık = 65°C (Düşük), Miktar = 8 Gr (Az), Sertlik = 2 dH (Yumuşak)
- **Beklenen Davranış:** Soğuk su ve az malzeme, kahvenin aromalarının suya geçmesini zorlaştırır. Temas süresi uzatılmalıdır.
- **Hesaplanan Çıktı:** ~**3.33 ml/sn** (Yavaş)
- **Yorum:** Sistem akış hızını minimum seviyelere çekerek suyun malzemeyle uzun süre kalmasını sağlamış, aromayı kurtarmıştır. ✅

---

### Senaryo 3: Optimum Altın Oran (Gold Cup Standardı)

- **Girişler:** Sıcaklık = 85°C (İdeal), Miktar = 20 Gr (Normal), Sertlik = 8 dH (Orta)
- **Beklenen Davranış:** Her şey standart ve dengeli, akış normal kalmalıdır.
- **Hesaplanan Çıktı:** ~**7.00 ml/sn** (Normal)
- **Yorum:** Sistem tam kararlılık göstererek kural 3'ü domine etmiş ve ideal akış hızını yakalamıştır. ✅

---

## 5. SONUÇ VE DEĞERLENDİRME

### 5.1. Sistemin Güçlü Yönleri

- **Kullanıcı Dostu Tasarım:** Doğrusal olmayan karmaşık bir gıda kimyası problemini basit insan mantığı kurallarıyla başarıyla yönetir.
- **Esneklik:** Yeni sensör girişleri (örn. kahve çekirdeği kavrulma derecesi) sisteme kural tabanı bozulmadan sadece yeni kurallar eklenerek entegre edilebilir.
- **Kararlılık:** Matematiksel olarak anlık sıçramalar (gürültüler) üyelik fonksiyonlarının yumuşak geçişleri sayesinde sönümlenir.

### 5.2. Sistemin Zayıf Yönleri ve Limitleri

- **Statik Üyelik Fonksiyonları:** Üyelik fonksiyonlarının sınırları (trimf üçgen uçları) sabittir. Zamanla eskiyen makine parçaları veya kireçlenen rezistanslar nedeniyle kayma yapabilir.

### 5.3. Güncel Yaklaşımlarla Kıyaslama

**PID Kontrolcüler ile Kıyaslama:**
Klasik PID'ler su sıcaklığını sabit tutmada iyidir ancak "su sertliği" veya "malzeme türü" gibi sayısal gradyanı doğrudan PID denklemine oturtulamayan dilsel parametreleri eşzamanlı yönetemezler.

**Makine Öğrenmesi (Yapay Sinir Ağları) ile Kıyaslama:**
Derin öğrenme modelleri çok daha yüksek hassasiyet sunabilir ancak çalışmaları için binlerce veri setine ve yüksek işlem gücüne ihtiyaç duyarlar. Geliştirilen bulanık kontrolcü ise sıfır veri setiyle, sadece uzman tecrübesiyle (barista kuralları) mikrodenetleyiciler üzerinde bile mikro saniyeler içinde çalışabilmektedir.

---

## 6. KAYNAKÇA

1. Zadeh, L. A. (1965). "Fuzzy sets". *Information and Control*, 8(3), 338–353.
2. Mamdani, E. H., & Assilian, S. (1975). "An experiment in linguistic synthesis with a fuzzy logic controller". *International Journal of Man-Machine Studies*, 7(1), 1–13.
3. Ross, T. J. (2010). *Fuzzy Logic with Engineering Applications*. John Wiley & Sons.
4. Scikit-Fuzzy Documentation. (2023). "Fuzzy Control System Design". Module API Reference.