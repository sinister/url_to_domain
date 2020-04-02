import tldextract
import os

urlslist = open("urls.txt", encoding="utf8").read().splitlines()
for url in urlslist:
    extracted = tldextract.extract(url)
    print("{}.{}".format(extracted.domain, extracted.suffix))

os.system("pause")
