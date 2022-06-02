# Project Introduction - Daegu Apartment

## About
Project ini merupakan project modul 3 dari program Job Connector Data Science Purwadhika.
<br>
<br>
Disini kita akan membangun sebuah model regresi untuk menentukan harga sewa dari penginapan yang ada di kota Daegu. Dataset ini bisa kalian akses [disini](https://drive.google.com/file/d/1MPDotXZNmiq6geRi8BkGd-fjttzoyTxW/view?usp=sharing). Di project ini saya ingin menggunakan 7 algoritma yaitu Linear Regression, K-Nearest Neighbors, Decision Tree, Random Forest, XGBoost, Ridge, dan Lasso. Dari keenam algoritma tersebut nantinya akan dipilih satu yang terbaik berdasarkan dari nilai evaluasi metriknya yaitu RMSE, MAE, dan MAPE.

## Model Building & Evaluation
Sebelum membangun model, saya telah melakukan beberapa tahap data processing seperti mengecek missing value, mendrop data duplikat, deteksi outliers, dan lain-lain sehingga data yang digunakan untuk pemodelan merupakan data yang bersih.
<br>
Dibawah ini merupakan hasil benchmark dari keenam model berdasarkan evaluasi metriknya.

![This is an image](https://github.com/cumapemula/Capstone-Project/blob/main/Capstone%20Project/Daegu%20Apartment/m1.png)
<br>
<br>
Nilai RMSE dan MAE mencapai ribuan dikarenakan value dari fitur target yaitu 'SalePrice' juga merupakan angka ribuan. Berdasarkan hasil diatas XGBoost dan Random Forest memiliki performa yang cukup baik dikarenakan nilai RMSE, MAE, dan MAPE yang rendah. Maka, kedua algoritma ini akan kita bandingkan lagi dengan melakukan prediksi pada test set dan hyperparameter tuning yang nantinya akan dipilih yang terbaik berdasarkan nilai dari evaluasi metriknya.
<br>
<br>
Dibawah ini hasil dari prediksi pada test set kedua algoritma tersebut.

![This is an image](https://github.com/cumapemula/Capstone-Project/blob/main/Capstone%20Project/Daegu%20Apartment/m2.png)
<br>
<br>
Performa Random Forest ketika dilakukan prediksi pada test set sedikit lebih baik daripada XGBoost. Kemudian kita akan lakukan hyperparameter tuning pada kedua model tersebut. Dibawah ini merupakan hasil dari hyperparameter tuning.

![This is an image](https://github.com/cumapemula/Capstone-Project/blob/main/Capstone%20Project/Daegu%20Apartment/m3.png)
<br>
<br>
Setelah dilakukan hyperparameter tuning, terlihat bahwa XGBoost memiliki performa yang lebih baik daripada Random Forest. Model XGBoost inilah yang akan kita gunakan sebagai model kita untuk memprediksi harga sewa penginapan di kota Daegu.
****
#### Terima Kasih Atas Perhatiannya!
E-mail : taufikaji350@gmail.com
