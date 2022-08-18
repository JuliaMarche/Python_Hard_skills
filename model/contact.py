from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None ,company=None,
                 address=None, homephone=None, workphone=None, mobile=None, secondphone=None, email=None,second_email=None, bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, second_address=None, fax=None, notes=None, id=None, third_email=None, all_phones_from_home_page=None,
                 all_email_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobile = mobile
        self.secondphone=secondphone
        self.email = email
        self.second_email = second_email
        self.third_email = third_email
        self.fax = fax
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.second_address = second_address
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.mobile, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize