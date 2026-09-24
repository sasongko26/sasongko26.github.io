---
date: 2021-05-01
title: Membuat histogram dengan python
categories: [sains data]
tags: [python, matplotlib, pandas]
---

Untuk membuat **histogram** dengan **python** dibutuhkan library **pandas** dan **matplotlib** dengan fungsi <code>.hist()</code> dan rangkaiannya seperti contoh histogram konsumsi bir berikut:

```python
#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

# sumber data https://github.com/fivethirtyeight/data/blob/master/alcohol-consumption/drinks.csv
# dengan editing header variabel
alkohol = pd.read_csv("../dataset/drinks.csv")

# histogram
plt.hist(x='beer_servings', data=alkohol)
plt.xlabel('Kaleng')
plt.ylabel('Jumlah')
plt.title('Konsumsi bir tahun 2010 (kaleng)')
plt.tight_layout()
plt.show()
```