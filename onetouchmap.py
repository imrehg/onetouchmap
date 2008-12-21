#!/usr/bin/env python


import pygtk
pygtk.require('2.0')
import gtk,gobject

class MainWindow:
    def __init__(self):

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
	self.window.show_all()


    def main(self):
        gtk.main()

    def delete_event(self, widget, event, data=None):
        return False # Allow the window to close

    def destroy(self, widget, data=None):
        gtk.main_quit()

if __name__ == "__main__":
    mainwin = MainWindow()
    mainwin.main()
