from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone():
    phone = "8" + "".join(random.choice(string.digits) for i in range(10))
    return phone

def random_email():
    email = string.ascii_letters + string.digits
    return "".join(random.choice(email) for i in range(7)) + "@mail.test"

testdata = [Contact(firstname="", lastname="", mobile="", email="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10), title=random_string("title", 10),
            company=random_string("company", 10), address=random_string("address", 10), homephone=random_phone(),
            workphone=random_phone(), mobile=random_phone(), secondphone=random_phone(),
            email=random_email(), second_email=random_email(), third_email=random_email(), bday="19", bmonth="June",
            byear="1994", second_address=random_string("second_address", 10), notes=random_string("notes", 10))
for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))