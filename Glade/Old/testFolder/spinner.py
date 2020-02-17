
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from subprocess import Popen
import threading
# all variables


# all functions
def submitClicked(self):
    combovalue = combo.get_model()[combo.get_active()]
    organization = combovalue[1]
    # print(value[1])
    entryvalue = entry.get_text()

    if(organization and entryvalue):
        dump.set_text(' ')
        self.lock = threading.allocate_lock()
        threading.start_new_thread(self.spin,(self.lock,))
        self.lock.acquire()
        spinner.start()
        # token = os.popen('./registration.sh ' + entryvalue + ' ' + organization.lower()).read()
        # command = "python3 test2.py " + token.strip("\n") + " " + organization.upper()
        Popen('sh test.sh', shell=True,stdin=None, stdout=None, stderr=None, close_fds=True)
        self.lock.release()
        spinner.stop()
        # os.system(command)
    else:
        dump.set_text('Fields are empty.')
        print(entryvalue)
        print(organization)
        print('Fields are empty')

def comboValueChange(self):
    combovalue = combo.get_model()[combo.get_active()]
    organization = combovalue[1]
    window.set_title(organization)


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
button = builder.get_object('submitButton')
spinner = builder.get_object('Spinker')
button.connect('clicked',submitClicked)

window = builder.get_object("window1")
window.connect('delete-event',Gtk.main_quit)
window.show_all()
Gtk.main()
