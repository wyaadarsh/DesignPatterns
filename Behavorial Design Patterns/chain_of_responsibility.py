# The Chain of Responsibility pattern is
# used when we want to give a chance to multiple objects to satisfy a single request, or
# when we don't know which object (from a chain of objects) should process a specific
# request in advance

#  An example is a purchase system.
# In purchase systems, there are many approval authorities. One approval authority
# might be able to approve orders up to a certain value, let's say $100. If the order is
# more than $100, the order is sent to the next approval authority in the chain that
# can approve orders up to $200, and so forth.

# Another case where Chain of Responsibility is useful is when we know that more
# than one object might need to process a single request. This is what happens in an
# event-based programming. A single event such as a left mouse click can be caught
# by more than one listener


class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        # Widget class "knows" about the Event class
        # but does not have any strict references to it, since an event needs to be passed only as
        # a parameter to handle().
        handler = 'handle_{}'.format(event)

        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)  # Important - Events get handled by parent Main window
    msg = MsgText(sd)   # Important - Events get handled by sd and mw
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == '__main__':
    main()
