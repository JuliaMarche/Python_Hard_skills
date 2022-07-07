from model.contact import Contact

def test_modify_contact_firstname(app):
    app.contact.modify_form(Contact(firstname="Proverka"))

def test_modify_contact_homephone(app):
    app.contact.modify_form(Contact(home="89215676577"))

