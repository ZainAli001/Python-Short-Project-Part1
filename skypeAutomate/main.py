from operator import contains
from skpy import Skype


slogin = Skype("03136219100", "sp20-bscs-0070")

contact = slogin.contacts

for i in contact:
    print(i)
