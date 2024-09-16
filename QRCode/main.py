from shutil import ExecError
# import qrcode as qr
from PIL import Image
import requests
from bs4 import BeautifulSoup


starter = 'https://www.'
end = '.com/'
for i in range(2):
    userInput = input("\nWhich Website QR code do u wanna create : ")
    # url = starter + userInput + end

    reqs = requests.get(userInput)
    soup = BeautifulSoup(reqs.content, 'html.parser')

    dict2 = {}
    i = 0

    for link in soup.find_all('a'):
        dict2[i] = link.get('href')
        i += 1

    x = dict2[1]
    try:
        img = qr.make(x)
        img.save(f"{userInput}.png")
        print("QR Code Generated..!")
    except Exception as e:
        print(e)
