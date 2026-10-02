# =============================================================================
# WISPr Automation
# Repository : sac-mgerencs-wispr-automation
# Author     : Wade Gerencser (mgerencs)
# Copyright  : (c) 2026 Wade Gerencser.
# License    : MIT — see LICENSE
# =============================================================================

output "radius_server_path" {
  description = "RESTCONF path of the configured RADIUS server object"
  value       = restconf_object.radius_server.path
}
