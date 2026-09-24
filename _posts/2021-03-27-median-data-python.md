---
date: 2021-03-27
title: Median data dengan python
categories: [sains data]
tags: [python, pandas]
---

Misalkan akan dicari berapa median konsumsi alkohol perkapita? Jawabannya bisa diketahui dengan menggunakan fungsi **describe()** atau **median()** yang dimiliki **pandas**.

```python
#!/usr/bin/env python3

import pandas as pd

# sumber data https://github.com/fivethirtyeight/data/blob/master/alcohol-consumption/drinks.csv
# dengan editing header variabel 
data = pd.read_csv("../dataset/drinks.csv")

# median
print('median konsumsi bir adalah ',data['beer_servings'].median(),'kaleng')
print('median konsumsi spirit adalah ', data['spirit_servings'].median())
print('median konsumsi anggur adalah ', data['wine_servings'].median(), 'gelas')
print('median konsumsi alkohol murni adalah ', data['pure_alcohol'].median(), 'liter')
```