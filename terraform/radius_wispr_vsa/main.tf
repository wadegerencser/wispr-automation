# =============================================================================
# WISPr Automation
# Repository : wispr-automation
# Author     : Wade Gerencser (mgerencs)
# Copyright  : (c) 2026 Wade Gerencser.
# License    : MIT — see LICENSE
# =============================================================================

terraform {
  required_version = ">= 1.5"
  required_providers {
    restconf = {
      source  = "CiscoDevNet/iosxe"
      version = "~> 0.1"
    }
  }
}

provider "restconf" {
  hostname = var.wlc_host
  username = var.wlc_username
  password = var.wlc_password
}

resource "restconf_object" "radius_server" {
  path = "Cisco-IOS-XE-native:native/radius/Cisco-IOS-XE-aaa:server=WISPR-AAA"
  data = jsonencode({
    "id" = "WISPR-AAA"
    "address" = {
      "ipv4" = {
        "host"      = var.radius_server_ip
        "auth-port" = 1812
        "acct-port" = 1813
      }
    }
    "timeout"    = 5
    "retransmit" = 2
  })
}
