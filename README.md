# url_to_domain
Simple solution to extract **only** the domains from a list of urls in Python.

### Instructions
Requires the tldextract library (pip install tldextract) 
Place your URLs in a text file named urls.txt with one url per line. 
Place this text file in the same directory as the python file and then simply run the file.

### Code
```python
import tldextract
import os

urlslist = open("urls.txt", encoding="utf8").read().splitlines()
for url in urlslist:
    extracted = tldextract.extract(url)
    print("{}.{}".format(extracted.domain, extracted.suffix))

os.system("pause")
```

### Examples
Some example inputs and outputs are below
```
https://www.xxx.yyy.com > yyy.com
https://xxx.yyy.co.uk/aaa/bbb/ > yyy.co.uk
www.xxx.yyy.com.au > yyy.com.au
```
