# WISPr Automation

Ansible, Terraform, and NETCONF automation for **WISPr** (Wireless Internet
Service Provider roaming) — the Wi-Fi Alliance / WBA smart-client protocol
(XML over HTTP[S], UAM redirect flows) used for inter-ISP hotspot roaming,
venue hotspot billing handoff, and RADIUS-backed guest/roaming auth.

Companion project to
[9800-wlc-automation](https://github.com/wadegerencser/9800-wlc-automation),
targeting the roaming/auth layer rather than the controller RF layer.

## Business Problem

Engineers configuring RADIUS/WISPr smart-client redirect settings on Cisco
IOS-XE wireless controllers today do it by hand, CLI line by CLI line, per
controller. That's slow and error-prone, and it's the same class of problem
[9800-wlc-automation](https://github.com/wadegerencser/9800-wlc-automation)
already solves for RF/tagging configuration — this project applies the same
approach to the roaming/auth layer.

## Why

Personal portfolio and visibility project — another public automation repo
to build out alongside the 9800 toolkit, same motivation as that project.

## How

Ansible, Terraform, and NETCONF playbooks for the Cisco-side RADIUS/WISPr
redirect plumbing, generated and PR'd using the same daily-automation pattern
as [9800-wlc-automation](https://github.com/wadegerencser/9800-wlc-automation).

## Not This

Not a WISPr smart-client implementation, not a roaming settlement/billing
system, and not production-hardened. This automates the Cisco controller
config side only (RADIUS, AAA, webauth redirect) — it does not implement the
WISPr XML/HTTP protocol itself.

## Impact

Unquantified — this is a portfolio/credit-building project, not a measured
production fix.

## Details

| Facet | Value |
|---|---|
| **Status** | `experimental` |
| **Owner** | mgerencs |
| **Related** | `complements 9800-wlc-automation` |

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
