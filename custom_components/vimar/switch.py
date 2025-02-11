"""Platform for switch integration."""

import logging

from homeassistant.helpers.entity import ToggleEntity

from .vimar_entity import VimarEntity, vimar_setup_platform

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Vimar Switch platform."""
    vimar_setup_platform(VimarSwitch, hass, async_add_entities, discovery_info)


class VimarSwitch(VimarEntity, ToggleEntity):
    """Provide Vimar switches and scenes."""

    _platform = "switch"

    def __init__(self, device_id, vimarconnection, vimarproject, coordinator):
        """Initialize the switch."""
        VimarEntity.__init__(self, device_id, vimarconnection, vimarproject, coordinator)

        # self.entity_id = "switch." + self._name.lower() + "_" + self._device_id

    # switch properties
    @property
    def is_on(self):
        """Return True if the device is on."""
        if self.has_state("on/off"):
            return self.get_state("on/off") == "1"
        # elif self.has_state('comando'):
        #     return self.get_state('comando') == '1'
        return None

    @property
    def is_default_state(self):
        """Return True of in default state - resulting in default icon."""
        return (self.is_on, True)[self.is_on is None]

    # async getter and setter

    async def async_turn_on(self, **kwargs):
        """Turn the Vimar switch on."""
        if self.has_state("on/off"):
            self.change_state("on/off", "1")

        # moved scenes into scene.py
        # elif self.has_state('comando'):
        #     self.change_state('comando', '1')

    async def async_turn_off(self, **kwargs):
        """Turn the Vimar switch off."""
        if self.has_state("on/off"):
            self.change_state("on/off", "0")

        # no turn off for scenes


# end class VimarSwitch
