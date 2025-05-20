import os

playbooks = [
    "configure_interfaces.yml",
    "configure_ospf.yml",
    "configure_mpls.yml",
    "configure_ldp.yml",
    "configure_firewall.yml",
    "verify_connectivity.yml"
]

for pb in playbooks:
    print(f"🔧 Running: {pb}")
    os.system(f"ansible-playbook -i inventory/hosts.yml playbooks/{pb}")
