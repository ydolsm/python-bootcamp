class Door:
    def __init__(self, closed, locked):
        self.closed = closed
        self.locked = locked

    def open(self):
        if self.closed:
            self.closed = False
        else:
            print("The door is already open")

    def close(self):
        if self.closed:
            print("The door is already closed.")
        else:
            self.closed = True

    def lock(self):
        if self.locked:
            print("The door is already locked.")
        elif self.locked

    def unlock(self):
        if self.locked:
