# url_to_domain
Simple solution to extract **only** the domains from a list of urls in Python.

### Requirements
Requires the tldextract library (pip install tldextract) 

### Instructions
Place your URLs in a text file named "urls.txt" with one url per line. 
Place this text file in the same directory as the python file and then simply run the file.

### Code
```python
import tldextract
import time

url_file = "urls.txt"

urlslist = open(url_file, encoding="utf8").read().splitlines()
for url in urlslist:
    extracted = tldextract.extract(url)
    print("{}.{}".format(extracted.domain, extracted.suffix))

time.sleep(1000) #os.pause() exits when trying to copy
```

### Examples
Some example inputs and outputs are below
```
https://www.xxx.yyy.com > yyy.com
https://xxx.yyy.co.uk/aaa/bbb/ > yyy.co.uk
www.xxx.yyy.com.au > yyy.com.au
```
