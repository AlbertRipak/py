#!/usr/bin/env python3

import urllib.request

# Змінна містить запит до "http://localhost:1234/"
fp = urllib.request.urlopen("http://localhost:1234/")

# 'endocdedContent' відповідає закодованій відповіді сервера ('index.html')
# 'decodedContent' відповідає розкодованій відповіді сервера
encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

# Виводимо вміст файла, отриманого з сервра ('index.html')
print(decodedContent)

# Закриваємо зєднання з сервером.
fp.close()
