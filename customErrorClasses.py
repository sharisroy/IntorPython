class TooManyPagesPrintingError(ValueError):
    pass
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnected(self):
        self.connected = False
        print("Disconnected!")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}, ({self.remaining_pages} page remaining)"

    def print(self, pages):
        if self.capacity < pages:
            raise TooManyPagesPrintingError(
                f"You try to print more that capacity"
            )
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

try:
    printer = Printer("Printer HP", "USB", 200)
    printer.print(220)
    print(printer)
except TooManyPagesPrintingError as e:
    print(e)
