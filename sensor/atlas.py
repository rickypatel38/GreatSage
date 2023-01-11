import pylibftdi

from pylibftdi.device import Device
from pylibftdi.driver import FtdiError
from pylibftdi import Driver

class AtlasDevice(Device):
    def __init__(self, sn):
        Device.__init__(self, mode='t', device_id=sn)
        self.term_string = "\r"

    def read_line(self, size=0):
        """
        taken from the ftdi library and modified to
        use the ezo line separator "\r"
        """
        line_buffer = []
        while True:
            next_char = self.read(1)
            if next_char == self.term_string or (size > 0 and len(line_buffer) > size):
                break
            line_buffer.append(next_char)
        return ''.join(line_buffer)

    def read_lines(self):
        """
        also taken from ftdi lib to work with modified readline function
        """
        lines = []
        try:
            while True:
                line = self.read_line()
                if line == self.term_string:
                    break
                    self.flush_input()
                lines.append(line)
            return lines

        except FtdiError:
            print("Failed to read from the sensor.")
            return ''

    def send_cmd(self, cmd):
        """
        Send command to the Atlas Sensor.
        Before sending, add Carriage Return at the end of the command.
        :param cmd:
        :return:
        """
        buf = cmd + self.term_string
        try:
            self.write(buf)
            return True
        except FtdiError:
            print("Failed to send command to the sensor.")
            return False

def get_ftdi_device_list():
    """
    return a list of lines, each a colon-separated
    vendor:product:serial summary of detected devices
    """
    for vendor, product, serial in Driver().list_devices():
        yield serial

