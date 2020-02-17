import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import os
import sys


entry = dict()
values = dict()


def buttonClick(self):
        for i in range(1,4):
            values[i] = str(entry[i].get_text())
            if(values[i] == ''):
                print('Missing values')
                return

        print(values[1]+values[2]+values[3])


builder = Gtk.Builder()
builder.add_from_file('combined.glade')


entry[1] = builder.get_object('entry1')
entry[2] = builder.get_object('entry2')
entry[3] = builder.get_object('entry3')
button = builder.get_object('submitButton')
button.connect('clicked',buttonClick)
window = builder.get_object('window1')
window.connect('delete-event',Gtk.main_quit)
window.show_all()

Gtk.main()
