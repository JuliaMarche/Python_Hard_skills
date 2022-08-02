from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="Test", middlename="Test", lastname="Test", nickname="Test", title="Test", company="Test",
          address="Test", homephone="6666666666666", workphone="55555555555555", mobile="77777777", secondphone="9999999", email="Test",
          second_email="Test", third_email="Test", bday="19", bmonth="June", byear="1994", second_address="Test", notes="Test"),
    Contact(firstname="Test2", middlename="Test2", lastname="Test2", nickname="Test2", title="Test2", company="Test2",
          address="Test2", homephone="6666666666666", workphone="55555555555555", mobile="77777777", secondphone="9999999", email="Test2",
          second_email="Test2", third_email="Test2", bday="18", bmonth="June", byear="1992", second_address="Test2", notes="Test2")
]


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
for i in range(3)
]

