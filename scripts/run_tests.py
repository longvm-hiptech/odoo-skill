import sys
import os

# Add Odoo server to Python path
sys.path.insert(0, r"C:\Program Files\Odoo 19.0.20260531\server")

import odoo
import odoo.addons
import odoo.cli

# Prepend git_repo path to addons namespace path
class CustomNamespacePath(list):
    _path_finder = None

git_repo_path = r"c:\Users\quang\Downloads\claude-marketplace-master\claude-marketplace-master\plugins\odoo-development\git_repo"
odoo.addons.__path__ = CustomNamespacePath([git_repo_path] + list(odoo.addons.__path__))

print("Active addons path search order:", odoo.addons.__path__)

import odoo.addons.qms_sop_management
print("LOADED MODULE FROM PATH:", odoo.addons.qms_sop_management.__file__)

if __name__ == "__main__":
    # If no arguments are provided, use defaults for convenience
    if len(sys.argv) == 1:
        sys.argv = [
            sys.argv[0],
            "-c", r"C:\Program Files\Odoo 19.0.20260531\server\odoo.conf",
            "-d", "qphatt",
            "-u", "qms_sop_management",
            "--test-enable",
            "--stop-after-init"
        ]
    else:
        # Prefill default configuration file if missing
        if "-c" not in sys.argv and "--config" not in sys.argv:
            sys.argv.extend(["-c", r"C:\Program Files\Odoo 19.0.20260531\server\odoo.conf"])
        # Ensure test flags are present
        if "--test-enable" not in sys.argv:
            sys.argv.append("--test-enable")
        if "--stop-after-init" not in sys.argv:
            sys.argv.append("--stop-after-init")

    print("Running Odoo with arguments:", sys.argv)
    odoo.cli.main()
