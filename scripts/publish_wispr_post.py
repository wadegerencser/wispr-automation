# =============================================================================
# WISPr Automation
# Repository : wispr-automation
# Author     : Wade Gerencser (mgerencs)
# Copyright  : (c) 2026 Wade Gerencser.
# License    : MIT — see LICENSE
# =============================================================================
"""
Publish blog/wispr-automation-post.html to wirelesswithwade.com as a draft
via the WordPress REST API. Credentials are read from ~/.wirelesswithwade_env
(gitignored) and never passed as command-line arguments.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

ENV_FILE = Path.home() / ".wirelesswithwade_env"
POST_FILE = Path(__file__).parent.parent / "blog" / "wispr-automation-post.html"
POST_TITLE = "WISPr Automation: Bringing the 9800 Toolkit to the Roaming and Auth Layer"
EXISTING_POST_ID = 780  # set by the first successful publish; update() if present


def load_env() -> dict:
    if not ENV_FILE.exists():
        sys.exit(f"Missing {ENV_FILE} — create it with WP_USER, WP_APP_PASSWORD, WP_API_BASE")
    env = {}
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        env[key.strip()] = value.strip().strip('"')
    return env


def main() -> None:
    env = load_env()
    user = env["WP_USER"]
    app_password = env["WP_APP_PASSWORD"]
    api_base = env["WP_API_BASE"]

    content = POST_FILE.read_text()

    payload = {
        "title": POST_TITLE,
        "content": content,
        "status": "draft",
    }

    host = api_base.split("://", 1)[1].split("/", 1)[0]
    netrc_fd = tempfile.NamedTemporaryFile(mode="w", suffix=".netrc", delete=False)
    netrc_fd.write(f"machine {host}\nlogin {user}\npassword {app_password.replace(' ', '')}\n")
    netrc_fd.close()
    netrc_path = netrc_fd.name
    import os
    os.chmod(netrc_path, 0o600)

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        payload_path = f.name

    url = f"{api_base}/posts/{EXISTING_POST_ID}" if EXISTING_POST_ID else f"{api_base}/posts"

    try:
        result = subprocess.run(
            [
                "curl", "-s", "--netrc",
                "--netrc-file", netrc_path,
                "-X", "POST", url,
                "-H", "Content-Type: application/json",
                "-d", f"@{payload_path}",
            ],
            capture_output=True, text=True, check=True,
        )
    finally:
        Path(payload_path).unlink(missing_ok=True)
        Path(netrc_path).unlink(missing_ok=True)

    data = json.loads(result.stdout)
    if "id" not in data:
        sys.exit(f"Publish failed: {data}")

    print(f"id: {data.get('id')}")
    print(f"status: {data.get('status')}")
    print(f"link: {data.get('link')}")
    print(f"edit in WP admin: https://wordpress.com/post/wirelesswithwade.com/{data.get('id')}")


if __name__ == "__main__":
    main()
