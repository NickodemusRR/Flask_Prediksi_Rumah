from flask import Flask, render_template, request, redirect, url_for, abort
import requests
import joblib

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return render_template('home.html')

# route untuk memasukkan data rumah yang dicari
@app.route('/post', methods=['POST'])
def cari():
    usia = int(request.form['usia'])
    kamar = int(request.form['kamar'])
    luas = int(request.form['luas'])
    harga = round(model.predict([[usia, kamar, luas]])[0], 2)
    return redirect(url_for('hasil', harga=harga))

# route untuk menampilkan hasil perhitungan
@app.route('/hasil/<int:harga>')
def hasil(harga):
    return render_template('hasil.html', harga=harga)

# route untuk menampilkan halaman error
@app.errorhandler(404)
def error(error):
    return render_template('error.html')

if __name__ == "__main__":
    # model diimport menggunakan package joblib
    model = joblib.load('modelJoblib')
    app.run(debug=True)