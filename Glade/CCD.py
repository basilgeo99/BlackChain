
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# all variables


# all functions
def queryButton(self):
    label.set_text('Querying Data')



# all widgets
builder = Gtk.Builder()
builder.add_from_file("CCD.glade")


button2 = builder.get_object('button2')
button2.connect('clicked',queryButton)

label = builder.get_object('label')

window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
