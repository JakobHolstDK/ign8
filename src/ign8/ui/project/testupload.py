import requests
import json

def upload_selinux_data(selinux_api, inventory_hostname, values):
    url = f"{selinux_api}/selinux/upload_selinux_data/"

    data = {
        "hostname": inventory_hostname,
        "status": values.get("status", ""),
        "mount": values.get("mount", ""),
        "rootdir": values.get("rootdir", ""),
        "policyname": values.get("policyname", ""),
        "current_mode": values.get("currentmode", ""),
        "configured_mode": values.get("modefromfile", ""),
        "mslstatus": values.get("mlsstatus", ""),
        "memprotect": values.get("memprotect", ""),
        "maxkernel": values.get("maxkernel", ""),
        "total": values.get("total", ""),
        "success": values.get("success", ""),
        "failed": values.get("failed", ""),
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=data, headers=headers, verify=False)
        response.raise_for_status()
        print(f"HTTP Status Code: {response.status_code}")
        print(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example values
    selinux_api = "https://example.com/api"
    inventory_hostname = "example-host"
    values = {
        "status": "enabled",
        "mount": "/mnt/data",
        # Add other values as needed
    }

    upload_selinux_data(selinux_api, inventory_hostname, values)
