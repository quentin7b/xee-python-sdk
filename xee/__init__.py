#!/usr/bin/env python
# coding: utf8
"""
    This package contains Xee python SDK.
    This SDK maps the request you can send to Xee APIs (see dev.xee.com).
"""

from .sdk import Xee

from enum import Enum

class AuthScope(Enum):
    """Authorization scopes."""
    VEHICLES_MANAGEMENT = "vehicles.management"
    VEHICLES_READ = "vehicles.read"
    VEHICLES_READ_SIGNALS = "vehicles.signals.read"
    VEHICLES_READ_LOCATIONS = "vehicles.locations.read"
    VEHICLES_READ_EVENTS = "vehicles.events.read"
    VEHICLES_READ_ACCELEROMETERS = "vehicles.accelerometers.read"
    VEHICLES_READ_DEVICE_DATA = "vehicles.devices-data.read"
    ACCOUNT_READ = "account.read"
