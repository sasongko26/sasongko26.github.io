---
date: 2021-03-20
title: Menampilkan data baris pertama python
categories: [python, statistika]
tags: [pandas]
---
Untuk menampilkan data baris pertama dengan python dapat menggunakan fungsi head() dari **pandas**. Tuliskan banyaknya baris yang akan ditampilkan (n) dalam tanda kurung. Kalau n tidak ditulis maka secara default n=5.

Contoh, data diambil dari https://catalog.data.gov/dataset/alzheimers-disease-and-healthy-aging-data

```python
import pandas as pd
data = pd.read_csv("Alzheimer_s_Disease_and_Healthy_Aging_Data.csv")
print(data.head())
```

Output :

```shell
                                          RowId  ...  Report
0  2016~2016~12~Q27~AGE~AGE_OVERALL~GENDER~MALE  ...     NaN
1         2015~2015~66~Q43~AGE~5064~GENDER~MALE  ...     NaN
2         2018~2018~66~Q18~AGE~5064~GENDER~MALE  ...     NaN
3       2018~2018~66~Q34~AGE~5064~GENDER~FEMALE  ...     NaN
4     2015~2015~16~Q43~AGE~65PLUS~GENDER~FEMALE  ...     NaN

[5 rows x 39 columns]
```

Dari output tersebut juga dapat diperoleh informasi jumlah kolomnya, yaitu 39 yang tidak semua kolom ditampilkan.
