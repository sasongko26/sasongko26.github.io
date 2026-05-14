---
date: 2021-03-16
title: Load dataset csv dengan python
categories: [manajemen file, python, statistika]
tags: [csv]
---
Misalkan ada dataset dalam format csv. Data tersebut dapat di-*load* atau diimpor dengan **python** dengan *library* **pandas**. Berikut script untuk load file data.csv.

```python
import pandas as pd
data = pd.read_csv("data.csv")
```
