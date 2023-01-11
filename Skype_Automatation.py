# $ pip install SkPy
# $ pip install os.path2

from skpy import Skype
import os.path

login = Skype("skype@gmailAddress.here", "passwordHere")

contact = login.contacts["live:.cid.2405sd0JHVj328"]
with open("C:/Image/Link/Here/img.png", "rb") as f:
    contact.chat.sendFile(f, "skp.png", image=True) 

# group = login.chats.create(["live:.cid.24d*fsK76Dab4n"])

# contact = login.contacts["live:.cid.2405d0ce8ca7aff"]
# contact.chat.sendMsg("Welcome to the world of python!")

# contact = login.contacts
# for i in contact:
#     print(i)