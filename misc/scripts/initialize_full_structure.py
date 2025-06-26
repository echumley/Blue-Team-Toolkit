#!/usr/bin/env python3

import os
import getpass

print(f"Running echumley's Blue Team Toolkit initialization script in {os.getcwd()}...\n")

# Category metadata
categories = {
    "1-model": {
        "title": "🧠 Model",
        "description": (
            "This stage focuses on gaining a clear understanding of the environment and "
            "potential threats through asset identification, topology mapping, and threat modeling. "
            "It aligns with MITRE D3FEND's 'Model' category, where defenders build situational "
            "awareness to inform future defensive strategies."
        ),
        "contains": (
            "- Network maps and architecture diagrams\n"
            "- Asset discovery scripts (e.g., Nmap, NetBox dumps)\n"
            "- Threat modeling tools or STRIDE diagrams\n"
            "- Topology documentation and enumeration utilities"
        )
    },
    "2-harden": {
        "title": "🛡️ Harden",
        "description": (
            "Hardening involves proactively securing systems and software to reduce the attack surface. "
            "In D3FEND, this includes configuration management, privilege restriction, patching, and endpoint protection. "
            "This category builds the defensive baseline for all hosts and services."
        ),
        "contains": (
            "- OS and software hardening scripts (e.g., CIS Benchmarks)\n"
            "- Configuration management files\n"
            "- Audit tools like Lynis, OpenSCAP\n"
            "- Local firewall and privilege restriction policies"
        )
    },
    "3-detect": {
        "title": "🔍 Detect",
        "description": (
            "Detection refers to identifying suspicious or malicious behavior across endpoints and the network. "
            "This maps to D3FEND's logging, alerting, and telemetry functions. It supports early warning of active threats."
        ),
        "contains": (
            "- SIEM rules and correlation logic (Elastic, Splunk, Wazuh)\n"
            "- Sysmon config files and log parsers\n"
            "- IDS/IPS rules (Suricata, Zeek)\n"
            "- Behavioral and anomaly detection scripts"
        )
    },
    "4-isolate": {
        "title": "🚧 Isolate",
        "description": (
            "Isolation refers to containment strategies to prevent lateral movement or data exfiltration once a compromise is detected. "
            "D3FEND includes concepts like network segmentation, endpoint isolation, and dynamic access control."
        ),
        "contains": (
            "- Firewall and VLAN configuration examples\n"
            "- Quarantine scripts (e.g., automated iptables or routing rules)\n"
            "- Endpoint isolation playbooks\n"
            "- Access control lists (ACLs) and zero trust policies"
        )
    },
    "5-deceive": {
        "title": "🎭 Deceive",
        "description": (
            "Deception increases adversary cost and visibility by planting traps (honeypots, honeytokens) and monitoring their interaction. "
            "It corresponds to D3FEND's adversary engagement and misdirection techniques."
        ),
        "contains": (
            "- Honeypot deployment scripts (Cowrie, T-Pot, OpenCanary)\n"
            "- Honeytoken creation examples (fake credentials, AWS keys)\n"
            "- Fake infrastructure (e.g., decoy file shares or databases)\n"
            "- Monitoring tools for interaction detection"
        )
    },
    "6-evict": {
        "title": "🧹 Evict",
        "description": (
            "Eviction is the process of removing the adversary from the environment — often through malware removal, account disabling, "
            "and cleaning persistence mechanisms. It reflects D3FEND's containment and remediation techniques."
        ),
        "contains": (
            "- Malware removal and eradication scripts\n"
            "- Account lockdown procedures\n"
            "- Playbooks for adversary eviction\n"
            "- Scripts for forensic triage and cleanup"
        )
    },
    "7-restore": {
        "title": "♻️ Restore",
        "description": (
            "Restoration ensures systems and services return to normal operations securely. "
            "This supports D3FEND's recovery and reconstitution practices, such as restoring from backups and validating system integrity."
        ),
        "contains": (
            "- Backup and recovery scripts (e.g., Borg, Restic)\n"
            "- Reimaging procedures and golden image templates\n"
            "- Integrity validation scripts (e.g., Tripwire, AIDE)\n"
            "- Disaster recovery plans and restoration timelines"
        )
    },
    "misc": {
    "title": "🧰 Miscellaneous",
    "description": (
        "This category includes general tools, glue code, experimental ideas, and supporting resources that don't fit directly "
        "into the MITRE D3FEND framework. It serves as a flexible space for utility scripts, cross-category integrations, "
        "training materials, and documentation."
    ),
    "contains": (
        "- Setup scripts for the toolkit (e.g., `build_toolkit_env.sh`)\n"
        "- Cheatsheets and quick reference guides\n"
        "- Utility scripts and log processing tools\n"
        "- Experimental tools or blue team PoCs\n"
        "- API wrappers and third-party integrations (e.g., VirusTotal, OTX)\n"
        "- Training content, blue team labs, or practice ranges"
        )
    }
}
# Sample tools.md content
tools_md_example = """\
# Open Source Tools

List and links to helpful tools used in this category.

---

Example:

- **Sysmon**: System monitoring tool that logs process creations, network connections, and more  
  🔗 https://docs.microsoft.com/en-us/sysinternals/downloads/sysmon
"""

# Subfolders to create
subdirs = ["scripts", "custom"]

# Run from Blue-Team-Toolkit root
for folder, meta in categories.items():
    # Create the main category folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Create subdirectories
    scripts_path = os.path.join(folder, "scripts")
    custom_path = os.path.join(folder, "custom")
    os.makedirs(scripts_path, exist_ok=True)
    os.makedirs(custom_path, exist_ok=True)

    # Write README.md
    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {meta['title']}\n\n")
            f.write(f"## Purpose\n\n{meta['description']}\n\n")
            f.write("## Folder Layout\n\n")
            f.write("- `README.md`: Overview of this category and tools used\n")
            f.write("- `scripts/`: General-purpose automation and utilities (Shell scripts, PowerShell, Python, etc.)\n")
            f.write("- `custom/`: My own created tools or configurations (original or heavily adapted tools/configs I've built or forked)\n")
            f.write("- `tools.md`: Links and descriptions of open-source tools\n\n")
            f.write("## Expected Contents\n\n")
            f.write(f"{meta['contains']}\n")
        print(f"✅ Created: {readme_path}")
    else:
        print(f"⚠️  Exists: {readme_path} (skipped)")

    # Write tools.md
    tools_path = os.path.join(folder, "tools.md")
    if not os.path.exists(tools_path):
        with open(tools_path, "w") as f:
            f.write(tools_md_example)
        print(f"✅ Created: {tools_path}")
    else:
        print(f"⚠️  Exists: {tools_path} (skipped)")

# Create root README.md
root_readme = "README.md"
if not os.path.exists(root_readme):
    with open(root_readme, "w") as f:
        f.write("# 🧰 Blue Team Toolkit\n\n")
        f.write(
            "This repository is a toolkit of blue team tools, commands, scripts, and utilities for use in CTFs, labs, and real-world blue team operations.\n\n"
            "The structure mirrors the [MITRE D3FEND](https://d3fend.mitre.org/) framework, with each directory corresponding to a specific category of defensive action. "
            "Each category contains curated tools, open-source utilities, and custom-built resources created by me to assist defenders in that area.\n\n"
        )
        f.write("## 📂 Categories\n\n")
        for folder, meta in categories.items():
            f.write(f"- {meta['title']} → [`{folder}/`](./{folder})\n")
    print(f"✅ Created: {root_readme}")
else:
    print(f"⚠️  Exists: {root_readme} (skipped)")

# Get system username
author_name = getpass.getuser()

# Create MIT LICENSE file
license_text = f"""\
MIT License

Copyright (c) 2025 {author_name}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

license_path = "LICENSE"
if not os.path.exists(license_path):
    with open(license_path, "w") as f:
        f.write(license_text)
    print(f"✅ Created: {license_path}")
else:
    print(f"⚠️  Exists: {license_path} (skipped)")


print("\n🎉 Toolkit folder structure and base contents fully initialized!")