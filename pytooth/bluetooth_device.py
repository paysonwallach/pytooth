import dbus

from pytooth import bluetooth_base, constants


class BluetoothDevice(bluetooth_base.Base):
    def __init__(self, device):
        super(BluetoothDevice, self).__init__()

        self.device = device
        self.props = dbus.Interface(device, constants.PROPERTIES_IFACE)
        self.get = lambda prop: self.props.Get(constants.DEVICE_IFACE, prop)
        self.set = lambda prop, value: self.props.Set(constants.DEVICE_IFACE,
                                                      prop, value)
        self.interface = dbus.Interface(device, constants.DEVICE_IFACE)

    @property
    def connected(self):
        return bool(self.get("Connected"))

    @connected.setter
    def connected(self, value):
        self.Connect(bool(value))

    @property
    def paired(self):
        return bool(self.get("Paired"))

    @property
    def trusted(self):
        return bool(self.get("Trusted"))

    @trusted.setter
    def trusted(self, value):
        self.Trust(bool(value))

    @property
    def name(self):
        return str(self.get("Name"))

    def Connect(self, connect=True):
        if connect:
            try:
                self.interface.Connect()

                return True
            except dbus.exceptions.DBusException:
                return False

        else:
            try:
                self.interface.Disconnect()

                return True
            except dbus.exceptions.DBusException:
                return False

    def Disconnect(self):
        return self.Conect(False)

    def Trust(self, trusted=True):
        self.set("Trusted", trusted)

    def Pair(self):
        if not self.paired:
            self.interface.Pair()
            self.Trust()
