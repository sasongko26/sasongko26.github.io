---
date: 2024-05-20
title: Klasifikasi decision tree dengan sklearn
categories: [sains data]
tags: [python, sklearn]
---

*Machine learning* belakangan ini semakin populer. Salah satu yang bisa dilakukan dengan *machine learning* adalah klasifikasi. Ada beberapa metode klasifikasi. Kali ini akan melakukan klasifikasi dengan cara *decision tree supervised learning*.

Skenario klasifikasi yang akan kita lakukan adalah menentukan jenis (label) bunga iris berdasarkan kriteria (atribut) yang diberikan. Jenis bunga irisnya adalah iris setosa, iris versicolor dan iris virginica. Adapun kriterianya berdasarkan panjang sepal, lebar sepal, panjang petal dan lebar petal.

*Tools* yang digunakan adalah **python** dengan *library* **pandas** dan **scikit-learn**. Datasetnya data **iris** yang sangat populer untuk pembelajaran *basic machine learning* khususnya klasifikasi. Data tersebut bisa diunduh [di sini](https://www.kaggle.com/datasets/uciml/iris). Setelah diunduh, ekstrak dan tempatkan file dataset **Iris.csv** pada direktori yang sama dengan file skrip pythonnya apabila menghendaki mode *scripting*. Sebagai alternatif bisa menggunakan mode interaktif. Alternatif lainnya adalah menjalankan dengan **jupyter notebook** atau **Google colab**

Pertama, impor *library* **pandas**, kemudian baca dataset sebagai dataframe dengan fungsi **read_csv** yang disediakan **pandas**.

```python
import pandas as pd
iris = pd.read_csv('Iris.csv')
```

Kemudian cek deskripsi dataset

```python
iris.info()
```

Dataset iris ini mempunyai 150 baris/entries (range index), terdiri dari 6 kolom (Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, dan Species) dan tidak ada *missing value* (non-null count sama dengan jumlah baris)

```shell
RangeIndex: 150 entries, 0 to 149
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype  
---  ------         --------------  -----  
 0   Id             150 non-null    int64  
 1   SepalLengthCm  150 non-null    float64
 2   SepalWidthCm   150 non-null    float64
 3   PetalLengthCm  150 non-null    float64
 4   PetalWidthCm   150 non-null    float64
 5   Species        150 non-null    object 
dtypes: float64(4), int64(1), object(1)
memory usage: 7.2+ KB
```

Selanjutnya menentukan mana yang merupakan y (jenis/hasil klasifikasi/label) dan mana yang merupakan X nya (kriteria/atribut).

```shell
X = iris[['SepalLengthCm', 'SepalWidthCm','PetalLengthCm', 'PetalWidthCm']]
y = iris['Species']
```

Setelah itu membuat model *decision tree*, melatih model dengan fungsi fit()

```python
from sklearn.tree import DecisionTreeClassifier
tree_model = DecisionTreeClassifier()
tree_model = tree_model.fit(X_train, y_train)
```

Setelah modelnya klasifikasinya jadi, kita bisa gunakan model itu untuk mengklasifikasi. Misal akan dicari jenis bunga iris dengan panjang sepal 6,5 cm, lebar sepal 3,2 cm, panjang petal 6 cm dan lebar petal 2,5 cm. Kriteria ini kita jadikan sebagai sebuah variabel cari_jenis.

```python
cari_y = [6.5, 3.2, 6.0, 2.5]
print(tree_model.predict([cari_y])[0])
```

Hasilnya?

```shell
Iris-virginica
```

</div>

Yes, iris viriginica. Lalu, apakah ini akurat? Kita tes akurasinya

```python
from sklearn.metrics import accuracy_score
y_pred = tree_model.predict(X_test)
akurasi = accuracy_score(y_pred, y_test)
print('Akurasi : ', 100*akurasi,'%')
```
Hasilnya

```shell
Akurasi :  93.33333333333333 %
```