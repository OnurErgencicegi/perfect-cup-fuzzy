import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import streamlit as st
import matplotlib.pyplot as plt

# --- 1. BULANIK MANTIK DEĞİŞKENLERİ VE ÜYELİK FONKSİYONLARI ---
# Girişler
sicaklik = ctrl.Antecedent(np.arange(60, 101, 1), 'sicaklik')
miktar = ctrl.Antecedent(np.arange(5, 41, 1), 'miktar')
sertlik = ctrl.Antecedent(np.arange(0, 19, 1), 'sertlik')

# Çıkış
akis_hizi = ctrl.Consequent(np.arange(2, 13, 0.1), 'akis_hizi', defuzzify_method='centroid')

# Üyelik Fonksiyonları (Triangular)
sicaklik['düşük'] = fuzz.trimf(sicaklik.universe, [60, 60, 80])
sicaklik['ideal'] = fuzz.trimf(sicaklik.universe, [75, 85, 90])
sicaklik['yüksek'] = fuzz.trimf(sicaklik.universe, [85, 100, 100])

miktar['az'] = fuzz.trimf(miktar.universe, [5, 5, 15])
miktar['normal'] = fuzz.trimf(miktar.universe, [10, 20, 25])
miktar['fazla'] = fuzz.trimf(miktar.universe, [20, 40, 40])

sertlik['yumuşak'] = fuzz.trimf(sertlik.universe, [0, 0, 7])
sertlik['orta'] = fuzz.trimf(sertlik.universe, [5, 9, 12])
sertlik['sert'] = fuzz.trimf(sertlik.universe, [10, 18, 18])

akis_hizi['yavaş'] = fuzz.trimf(akis_hizi.universe, [2, 2, 6])
akis_hizi['normal'] = fuzz.trimf(akis_hizi.universe, [5, 7, 9])
akis_hizi['hızlı'] = fuzz.trimf(akis_hizi.universe, [8, 12, 12])

# --- 2. KURALLARIN TANIMLANMASI (15 Kural) ---
rule1  = ctrl.Rule(sicaklik['düşük']  & miktar['az']     & sertlik['yumuşak'], akis_hizi['yavaş'])
rule2  = ctrl.Rule(sicaklik['yüksek'] & miktar['fazla']  & sertlik['sert'],    akis_hizi['hızlı'])
rule3  = ctrl.Rule(sicaklik['ideal']  & miktar['normal'] & sertlik['orta'],    akis_hizi['normal'])
rule4  = ctrl.Rule(sicaklik['düşük']  & miktar['fazla']  & sertlik['yumuşak'], akis_hizi['yavaş'])
rule5  = ctrl.Rule(sicaklik['yüksek'] & miktar['az']     & sertlik['orta'],    akis_hizi['hızlı'])
rule6  = ctrl.Rule(sicaklik['ideal']  & miktar['fazla']  & sertlik['sert'],    akis_hizi['normal'])
rule7  = ctrl.Rule(sicaklik['düşük']  & miktar['normal'] & sertlik['sert'],    akis_hizi['yavaş'])
rule8  = ctrl.Rule(sicaklik['yüksek'] & miktar['normal'] & sertlik['yumuşak'], akis_hizi['hızlı'])
rule9  = ctrl.Rule(sicaklik['ideal']  & miktar['az']     & sertlik['yumuşak'], akis_hizi['yavaş'])
rule10 = ctrl.Rule(sicaklik['düşük']  & miktar['fazla']  & sertlik['sert'],    akis_hizi['yavaş'])
rule11 = ctrl.Rule(sicaklik['yüksek'] & miktar['az']     & sertlik['sert'],    akis_hizi['normal'])
rule12 = ctrl.Rule(sicaklik['ideal']  & miktar['fazla']  & sertlik['yumuşak'], akis_hizi['hızlı'])
rule13 = ctrl.Rule(sicaklik['düşük']  & miktar['az']     & sertlik['orta'],    akis_hizi['yavaş'])
rule14 = ctrl.Rule(sicaklik['yüksek'] & miktar['fazla']  & sertlik['orta'],    akis_hizi['hızlı'])
rule15 = ctrl.Rule(sicaklik['ideal']  & miktar['normal'] & sertlik['sert'],    akis_hizi['normal'])

# Kontrol Sistemini Oluşturma
akis_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8,
                                 rule9, rule10, rule11, rule12, rule13, rule14, rule15])
akis_simulasyon = ctrl.ControlSystemSimulation(akis_ctrl)

# --- 3. STREAMLIT ARAYÜZÜ (GUI) ---
st.set_page_config(page_title="Bulanık Mantık Demleme Kontrolcüsü", layout="wide")

st.title("☕ Mükemmel Filtre Kahve / Çay Demleme Kontrolcüsü")
st.markdown("Bulanık mantık kullanarak su sıcaklığı, malzeme miktarı ve su sertliğine göre "
            "optimum su akış hızını hesaplayan akıllı sistem.")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Giriş Değerleri")
    input_sicaklik = st.slider("Su Sıcaklığı (°C)", 60, 100, 85)
    input_miktar   = st.slider("Kahve/Çay Miktarı (Gr)", 5, 40, 20)
    input_sertlik  = st.slider("Su Sertliği (dH)", 0, 18, 8)

    hesapla_btn = st.button("Hesapla", type="primary")

with col2:
    st.header("Sonuç ve Durulaştırma (Defuzzification)")
    if hesapla_btn:
        akis_simulasyon.input['sicaklik'] = input_sicaklik
        akis_simulasyon.input['miktar']   = input_miktar
        akis_simulasyon.input['sertlik']  = input_sertlik

        akis_simulasyon.compute()
        sonuc = akis_simulasyon.output['akis_hizi']

        st.success(f"**Optimum Su Akış Hızı: {sonuc:.2f} ml/sn**")

        # Defuzzification grafiği
        fig, ax = plt.subplots(figsize=(8, 4))
        colors = ['#2196F3', '#4CAF50', '#FF9800']
        for label, color in zip(['yavaş', 'normal', 'hızlı'], colors):
            ax.plot(akis_hizi.universe, akis_hizi[label].mf, label=label, color=color, linewidth=2)

        ax.axvline(x=sonuc, color='red', linestyle='--', linewidth=2, label=f'Sonuç: {sonuc:.2f} ml/sn')
        ax.set_title('Durulaştırma (Ağırlık Merkezi - Centroid)')
        ax.set_xlabel('Akış Hızı (ml/sn)')
        ax.set_ylabel('Üyelik Derecesi')
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
        plt.close(fig)

st.divider()
st.subheader("Üyelik Fonksiyonları Grafikleri")

fig2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

# Sıcaklık üyelik fonksiyonları
for label, color in zip(['düşük', 'ideal', 'yüksek'], ['#2196F3', '#4CAF50', '#F44336']):
    ax1.plot(sicaklik.universe, sicaklik[label].mf, label=label, color=color, linewidth=2)
ax1.set_title('Su Sıcaklığı (°C)')
ax1.set_xlabel('Sıcaklık (°C)')
ax1.set_ylabel('Üyelik Derecesi')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Miktar üyelik fonksiyonları
for label, color in zip(['az', 'normal', 'fazla'], ['#2196F3', '#4CAF50', '#F44336']):
    ax2.plot(miktar.universe, miktar[label].mf, label=label, color=color, linewidth=2)
ax2.set_title('Kahve/Çay Miktarı (Gr)')
ax2.set_xlabel('Miktar (Gr)')
ax2.set_ylabel('Üyelik Derecesi')
ax2.legend()
ax2.grid(True, alpha=0.3)

# Sertlik üyelik fonksiyonları
for label, color in zip(['yumuşak', 'orta', 'sert'], ['#2196F3', '#4CAF50', '#F44336']):
    ax3.plot(sertlik.universe, sertlik[label].mf, label=label, color=color, linewidth=2)
ax3.set_title('Su Sertliği (dH)')
ax3.set_xlabel('Sertlik (dH)')
ax3.set_ylabel('Üyelik Derecesi')
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)