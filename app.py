import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load models
xgb_model = joblib.load('xgboost_model.pkl')
rf_model = joblib.load('random_forest_model.pkl')

# Helper function: classify performance
def classify_performance(avg_score):
    if avg_score >= 80:
        return "Baik"
    elif 60 <= avg_score < 80:
        return "Cukup"
    else:
        return "Kurang"

# App layout
st.title("Klasifikasi Performa Siswa")
st.sidebar.title("Navigasi")
option = st.sidebar.radio("Pilih halaman", ['Input Data', 'Hasil Klasifikasi'])

if option == 'Input Data':
    st.header("Input Data Siswa")

    # Input fields for user
    name = st.text_input("Nama Siswa")
    ipa = st.number_input("Nilai IPA", min_value=0, max_value=100, step=1)
    ips = st.number_input("Nilai IPS", min_value=0, max_value=100, step=1)
    mtk = st.number_input("Nilai Matematika", min_value=0, max_value=100, step=1)
    sejarah = st.number_input("Nilai Sejarah", min_value=0, max_value=100, step=1)
    fisika = st.number_input("Nilai Fisika", min_value=0, max_value=100, step=1)
    kimia = st.number_input("Nilai Kimia", min_value=0, max_value=100, step=1)

    # Save data to session state
    if st.button("Simpan Data"):
        if name:
            new_data = {
                "Nama": name,
                "IPA": ipa,
                "IPS": ips,
                "Matematika": mtk,
                "Sejarah": sejarah,
                "Fisika": fisika,
                "Kimia": kimia
            }
            if 'data' not in st.session_state:
                st.session_state['data'] = []
            st.session_state['data'].append(new_data)
            st.success("Data berhasil disimpan!")
        else:
            st.warning("Nama siswa tidak boleh kosong.")

elif option == 'Hasil Klasifikasi':
    st.header("Hasil Klasifikasi Performa Siswa")

    if 'data' not in st.session_state or len(st.session_state['data']) == 0:
        st.warning("Belum ada data siswa yang diinputkan.")
    else:
        # Load data from session state
        data = pd.DataFrame(st.session_state['data'])

        # Calculate average score and classify performance
        data['Rata-rata'] = data[['IPA', 'IPS', 'Matematika', 'Sejarah', 'Fisika', 'Kimia']].mean(axis=1)
        data['Performa'] = data['Rata-rata'].apply(classify_performance)

        # Display results
        st.subheader("Tabel Hasil Klasifikasi")
        st.dataframe(data)

        # Visualize results
        st.subheader("Visualisasi Performa Siswa")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=data, x='Nama', y='Rata-rata', hue='Performa', dodge=False, palette='viridis')
        plt.title("Distribusi Performa Siswa Berdasarkan Nilai")
        plt.xticks(rotation=45)
        plt.ylabel("Rata-rata Nilai")
        plt.xlabel("Nama Siswa")
        st.pyplot(plt)
