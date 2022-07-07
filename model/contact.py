class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None ,company=None,
                 address=None, home=None, work=None, email=None, bday=None, bmonth=None, byear=None, address2=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.company_address = address
        self.home_phone = home
        self.work_phone = work
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.notes = notes