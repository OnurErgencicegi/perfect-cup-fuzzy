# ☕ Mükemmel Filtre Kahve / Çay Demleme Makinesi
## Bulanık Mantık Kontrolcüsü

**Mersin Üniversitesi — Bilişim Sistemleri ve Teknolojileri Bölümü**
**Bulanık Mantık Dersi Dönem Projesi**
**Hazırlayan:** Onur Ergençiçeği

---

## 📌 Proje Hakkında

Bu proje, geleneksel filtre kahve ve çay demleme makinelerindeki sabit parametre problemini çözmek amacıyla geliştirilmiş bir **Bulanık Mantık (Fuzzy Logic) Kontrolcüsü** uygulamasıdır.

Sistem; su sıcaklığı, malzeme miktarı ve su sertliği gibi 3 giriş değişkenini alarak optimal **su akış hızını** hesaplar. Böylece hem aşırı acı (over-extraction) hem de yavan (under-extraction) demleme senaryolarının önüne geçilir.

---

## 📁 Proje Yapısı

```
├── .streamlit/
│   └── config.toml       # Şık Camgöbeği (Teal) tema konfigürasyonu
├── main.py                # Streamlit GUI ve Bulanık Mantık motoru kaynak kodu
├── README.md             # Proje genel tanıtım ve kurulum belgesi
└── PROJE_RAPORU.md       # Akademik formatta hazırlanmış detaylı dönem raporu
```

---

## 📊 Teknolojiler ve Kütüphaneler

| Kütüphane | Kullanım Amacı |
|-----------|----------------|
| **Python 3.10+** | Ana programlama dili |
| **Scikit-Fuzzy** | Bulanık küme ve kontrolcü tasarımı |
| **NumPy** | Evrensel küme dizilimleri ve matematiksel arka plan |
| **Matplotlib** | Üyelik fonksiyonları ve çıkarım grafiklerinin çizimi |
| **Streamlit** | Reaktif ve modern web tabanlı kullanıcı arayüzü |

---

## 🔢 Sistem Değişkenleri

### Giriş Değişkenleri

| Değişken | Birim | Aralık | Dilsel Terimler |
|----------|-------|--------|-----------------|
| Su Sıcaklığı | °C | [60 – 100] | Düşük / İdeal / Yüksek |
| Malzeme Miktarı | Gram | [5 – 40] | Az / Normal / Fazla |
| Su Sertliği | dH | [0 – 18] | Yumuşak / Orta / Sert |

### Çıkış Değişkeni

| Değişken | Birim | Aralık | Dilsel Terimler |
|----------|-------|--------|-----------------|
| Su Akış Hızı | ml/sn | [2 – 12] | Yavaş / Normal / Hızlı |

---

## ⚙️ Kurulum ve Çalıştırma

### Gereksinimler

```bash
pip install -r requirements.txt
```

### Uygulamayı Başlatma

```bash
streamlit run main.py
```

Tarayıcınızda `http://localhost:8501` adresine gidin.

---

## 🧪 Test Senaryoları

| Senaryo | Sıcaklık | Miktar | Sertlik | Beklenen Çıktı |
|---------|----------|--------|---------|----------------|
| Over-extraction riski | 98°C (Yüksek) | 38 gr (Fazla) | 16 dH (Sert) | ~10.45 ml/sn (Hızlı) |
| Under-extraction riski | 65°C (Düşük) | 8 gr (Az) | 2 dH (Yumuşak) | ~3.33 ml/sn (Yavaş) |
| Altın oran (Gold Cup) | 85°C (İdeal) | 20 gr (Normal) | 8 dH (Orta) | ~7.00 ml/sn (Normal) |

---

## 🎨 Arayüz Özellikleri

- **Sol Panel (Sidebar):** Su sıcaklığı, kahve gramajı ve su sertliği için dinamik slider'lar ve "Hesapla" butonu.
- **Sağ Panel (Outputs):** Hesaplanan net akış hızı (ml/sn), durulaştırma grafiği (Ağırlık Merkezi kesişim çizgisi dahil) ve giriş değişkenlerinin üyelik fonksiyon grafikleri.
- **Tema:** Akademik sunuma uygun, göz yormayan Camgöbeği (Teal — `#008080`) renk teması.

---

## 📚 Kaynakça

- Zadeh, L. A. (1965). *Fuzzy sets*. Information and Control, 8(3), 338–353.
- Mamdani, E. H., & Assilian, S. (1975). *An experiment in linguistic synthesis with a fuzzy logic controller*. International Journal of Man-Machine Studies, 7(1), 1–13.
- Ross, T. J. (2010). *Fuzzy Logic with Engineering Applications*. John Wiley & Sons.
- Scikit-Fuzzy Documentation. (2023). *Fuzzy Control System Design*. Module API Reference.
