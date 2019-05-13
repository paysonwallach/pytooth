import dbus

from dbus.mainloop import glib
from pytooth import constants


class Base(object):
    def __init__(self):
        glib.DBusGMainLoop(set_as_default=True)

        self.bus = dbus.SystemBus()
        self.adapter = self.find_adapter()

    def get_device(self, path):
        return self.bus.get_object(constants.SERVICE_NAME, path)

    def get_interface(self, interface, path):
        return self.get_interface(constants.PROPERTIES_IFACE, path)

    def get_managed_objects(self):
        manager = dbus.Interface(self.bus.get_object(
            constants.SERVICE_NAME, "/"),
                       constants.OBJECT_IFACE)

        return manager.GetManagedObjects()

    def find_interface(self, interface):
        paths = []
        objects = self.get_managed_objects()

        for path, ifaces in objects.items():
            device = ifaces.get(interface)

            if device is None:
                continue

            paths.append(path)

        return paths

    def find_adapter(self):
        adapters = self.find_interface(constants.ADAPTER_IFACE)

        if adapters:
            device = self.get_device(adapters[0])

            return dbus.Interface(device, constants.ADAPTER_IFACE)
        else:
            return None
