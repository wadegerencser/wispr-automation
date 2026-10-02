# WISPr Automation

Ansible, Terraform, and NETCONF automation for **WISPr** (Wireless Internet
Service Provider roaming) — the Wi-Fi Alliance / WBA smart-client protocol
(XML over HTTP[S], UAM redirect flows) used for inter-ISP hotspot roaming,
venue hotspot billing handoff, and RADIUS-backed guest/roaming auth.

Companion project to
[9800-wlc-automation](https://github.com/wadegerencser/9800-wlc-automation),
targeting the roaming/auth layer rather than the controller RF layer.

## What's in here

| Directory | Contents |
|---|---|
| `playbooks/` | Ansible playbooks (`cisco.ios`/`cisco.iosxe`) for WISPr-relevant RADIUS, ACL, and redirect config on Cisco gear |
| `vars/` | YAML variable files paired 1:1 with playbooks |
| `terraform/radius_wispr_vsa/` | Terraform module for RADIUS vendor-specific attribute (VSA) policy supporting WISPr smart-client redirect |
| `netconf/` | Python NETCONF scripts (`ncclient`) for IOS-XE YANG-based config |
| `inventory/` | Ansible inventory templates |

## Platform support

- **macOS / Linux** — native `ansible-playbook`, `terraform`, `python3`
- **Windows** — run via WSL2, or the GitHub-hosted `ubuntu-latest` CI runners below
- **CI** — `.github/workflows/validate.yml` runs YAML lint, `ansible-lint`,
  and `terraform validate` on every PR

## Quick start

```bash
pip install -r requirements.txt
ansible-galaxy collection install cisco.ios cisco.iosxe
ansible-playbook -i inventory/hosts.yml playbooks/wispr_radius_vsa.yml
```

## License

MIT — see `LICENSE`.
