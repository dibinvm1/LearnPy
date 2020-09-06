import os
from downloads import download

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
email_text = os.path.join(BASE_DIR,"hello.txt")

content = ""

with open(email_text, 'r') as f:
    content = f.read()

print(content.format(name="john"))


DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")
url = "https://linagora.com/wp-content/uploads/2018/05/Ubuntu-logo-300x169.png"

print(download(url, DOWNLOAD_DIR))