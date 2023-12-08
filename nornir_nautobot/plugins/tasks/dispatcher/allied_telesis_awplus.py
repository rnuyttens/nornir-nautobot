"""nornir dispatcher for Allied Telesis Awplus."""

from nornir_nautobot.plugins.tasks.dispatcher.default import NetmikoDefault


class NetmikoAlliedTelesisAwplus(NetmikoDefault):
    """Collection of Netmiko Nornir Tasks specific to Allied Telesis Awplus devices."""

    config_command = "show run"
