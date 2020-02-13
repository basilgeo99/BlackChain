
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# all variables


# all functions
def submitClicked(self):
    combovalue = combo.get_model()[combo.get_active()]
    # print(value[1])
    entryvalue = entry.get_text()
    if(combovalue[1] and entryvalue):
        dump.set_text(' ')
        spin.start()
        # enter your code here
        spin.stop()
    else:
        dump.set_text('Fields are empty.')
        print('Fields are empty')

def comboValueChange(self):
    print('combo changed')


# all widgets
builder = Gtk.Builder()
builder.add_from_file("basic.glade")


orgstore=Gtk.ListStore(int,str)
orgOptions = ["User","Airport","CCD"]
for org in orgOptions:
    orgstore.append([None,org])
combo = builder.get_object("comboBox")
combo.set_model(orgstore)
combo.set_entry_text_column(1)
combo.connect('changed',comboValueChange)

entry = builder.get_object('entryBox')
label1 = builder.get_object('usernameLabel')
label2 = builder.get_object('organizationLabel')
dump = builder.get_object('dumpLabel')
spin = builder.get_object('Spinker')
button = builder.get_object('submitButton')

button.connect('clicked',submitClicked)

window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
