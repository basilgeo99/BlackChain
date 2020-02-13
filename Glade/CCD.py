
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
        messageLabel.set_text(str(value))
        message.run()
        message.destroy()


# all widgets
builder = Gtk.Builder()
builder.add_from_file("CCD.glade")


button2 = builder.get_object('button2')
button2.connect('clicked',queryButton)
entry = builder.get_object('entry')
label = builder.get_object('label')
message = builder.get_object('message')
messageButton = builder.get_object('messageButton')
messageLabel = builder.get_object('messageLabel')

window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
