from shutil import ExecError
# import qrcode as qr
from PIL import Image
import requests
from bs4 import BeautifulSoup


starter = 'https://www.'
end = '.com/'

userInput = input("\nWhich Website QR code do u wanna create : ")
# url = starter + userInput + end

reqs = requests.get(userInput)
soup = BeautifulSoup(reqs.content, 'html.parser')

dict2 = {}
i = 0

for link in soup.find_all('a'):
    dict2[i] = link.get('href')
    i += 1

print(dict2)
