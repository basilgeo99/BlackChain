
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# all variables


# all functions
def queryButton(self):
    value = str(entry.get_text())
    if value == '':
        label.set_text('username field is empty')
    else:
        label.set_text('Querying Data for '+str(value))
        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Queried data for "+str(value))
        result = 'some text' # insert your querying data command here after formatting it as required
        dialog.format_secondary_text(result)
        dialog.run()
        dialog.destroy()

def revokeButton(self):
    label.set_text('Revoking Consent')

def deleteButton(self):
    label.set_text('Deleting data from system')

def applicationFormButton(self):
    label.set_text('Form window is now open')
    os.system('python3 form.py')


# all widgets
builder = Gtk.Builder()
builder.add_from_file("user.glade")


button1 = builder.get_object('button1')
button1.connect('clicked',queryButton)
button2 = builder.get_object('button2')
button2.connect('clicked',revokeButton)
button3 = builder.get_object('button3')
button3.connect('clicked',deleteButton)
button4 = builder.get_object('button4')
button4.connect('clicked',applicationFormButton)
entry = builder.get_object('entry')
label = builder.get_object('label')
message = builder.get_object('message')
window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()