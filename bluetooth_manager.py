from pytooth import bluetooth_base, bluetooth_device, constants, exceptions


class BluetoothManager(bluetooth_base.Base):
    def __init__(self):
        super(BluetoothManager, self).__init__()

        self.devices = self.get_devices()

    def get_devices(self):
        devices = self.find_interface(constants.DEVICE_IFACE)

        return [bluetooth_device.BluetoothDevice(self.get_device(device)) for
                device in devices]

    def get_connected_devices(self, no_name=False):
        if no_name:
            devices = self.get_devices()
        else:
            devices = self.get_named_devices()

        return [device for device in devices if device.connected]

    def get_named_devices(self):
        named_devices = []
        devices = self.get_devices()

        for device in devices:
            try:
                named_devices.append(device)
            except exceptions.DBusException:
                pass

        return named_devices

    def begin_discovery(self, timeout=10):
        if self.adapter:
            self.adapter.DiscoverableTimeout = timeout
            self.adapter.Discoverable = True
            self.adapter.StartDiscovery()

    def stop_discovery(self):
        self.adapter.StopDiscovery()

    def Forget(self, device):
        try:
            self.adapter.RemoveDevice(device.interface)

            return True
        except exceptions.DBusException:
            return False
