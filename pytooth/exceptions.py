"""
pytooth.exceptions

A module of PyTooth's exceptions.
"""

from dbus.exceptions import DBusException


class PyToothException(Exception):
    """An exception occurred in PyTooth."""


class DBusException(PyToothException, DBusException):
    """A dbus exception occurred."""
