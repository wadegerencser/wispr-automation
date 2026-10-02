# =============================================================================
# WISPr Automation
# Repository : wispr-automation
# Author     : Wade Gerencser (mgerencs)
# Copyright  : (c) 2026 Wade Gerencser.
# License    : MIT — see LICENSE
# =============================================================================

variable "wlc_host" {
  description = "Management IP or hostname of the 9800 WLC RESTCONF endpoint"
  type        = string
}

variable "wlc_username" {
  description = "RESTCONF username"
  type        = string
}

variable "wlc_password" {
  description = "RESTCONF password"
  type        = string
  sensitive   = true
}

variable "radius_server_ip" {
  description = "IPv4 address of the RADIUS server backing WISPr auth"
  type        = string
}
