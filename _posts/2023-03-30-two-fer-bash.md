---
date: 2023-03-30
title: Two fer bash
categories: [pemrograman]
tags: [bash]
---
*Two fer* merupakan salah satu soal latihan pemrograman yang ada di **exercism**. Latihan ini meminta untuk dibuatkan suatu *script* yang apabila script tersebut dieksekusi tanpa argumen apapun maka akan mengeluarkan output “One for you, one for me.”. Apabila diberikan suatu argumen yang merupakan nama seseorang misalnya Sasongko, maka outputnya “One for Sasongko, one for me.”.

Berikut adalah *script bash*-nya

```shell
#!/usr/bin/bash

main () {
  NAME=${1:-you}
  echo "One for $NAME, one for me."
}
main "$@"
```
