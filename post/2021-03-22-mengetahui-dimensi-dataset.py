---
date: 2021-03-22
title: Mengetahui dimensi dataset python
tags: [slackware, python, statistik]
---
Untuk mengetahui dimensi atau jumlah baris dan kolom dataset dapat menggunakan shape dari pandas. Data diambil dari https://catalog.data.gov/dataset/alzheimers-disease-and-healthy-aging-data/

```python
import pandas as pd
data = pd.read\_csv("Alzheimer\_s\_Disease\_and\_Healthy\_Aging\_Data.csv")
print(data.shape)
```
Output: 
```
(178539, 39)
```
Dari output tersebut diketahui dataset mempunyai 178539 baris dan 39 kolom.
