# =============================================================================
# WISPr Automation
# Repository : wispr-automation
# Author     : Wade Gerencser (mgerencs)
# Copyright  : (c) 2026 Wade Gerencser.
# License    : MIT — see LICENSE
# =============================================================================
"""
Create a RADIUS server entry on a Cisco IOS-XE 9800 via NETCONF, using the
Cisco-IOS-XE-aaa YANG model. Mirrors what playbooks/wispr_radius_vsa.yml does
over the CLI, for environments that require model-driven config instead.
"""

from ncclient import manager

WLC_HOST = "192.0.2.1"
WLC_PORT = 830
WLC_USER = "admin"
WLC_PASS = "replace-me"

RADIUS_SERVER_PAYLOAD = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <radius>
      <server xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-aaa">
        <id>WISPR-AAA</id>
        <address>
          <ipv4>
            <host>192.0.2.10</host>
            <auth-port>1812</auth-port>
            <acct-port>1813</acct-port>
          </ipv4>
        </address>
        <timeout>5</timeout>
        <retransmit>2</retransmit>
      </server>
    </radius>
  </native>
</config>
"""


def main() -> None:
    with manager.connect(
        host=WLC_HOST,
        port=WLC_PORT,
        username=WLC_USER,
        password=WLC_PASS,
        hostkey_verify=False,
        device_params={"name": "iosxe"},
    ) as m:
        response = m.edit_config(target="running", config=RADIUS_SERVER_PAYLOAD)
        print(response)


if __name__ == "__main__":
    main()
