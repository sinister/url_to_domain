import tldextract
import time

urlslist = open("urls.txt", encoding="utf8").read().splitlines()
for url in urlslist:
    extracted = tldextract.extract(url)
    print("{}.{}".format(extracted.domain, extracted.suffix))

time.sleep(1000)
