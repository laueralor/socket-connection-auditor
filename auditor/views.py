import platform
import re
import subprocess
from django.shortcuts import render


def get_mock_socket_data():
    return [
        {
            "netid": "tcp",
            "state": "LISTEN",
            "local": "127.0.0.1:8000",
            "peer": "0.0.0.0:*",
            "process": "python (PID: 1234)"
        },
        {
            "netid": "tcp",
            "state": "LISTEN",
            "local": "0.0.0.0:22",
            "peer": "0.0.0.0:*",
            "process": "sshd (PID: 845)"
        },
        {
            "netid": "udp",
            "state": "UNCONN",
            "local": "0.0.0.0:5353",
            "peer": "0.0.0.0:*",
            "process": "mdns (PID: 936)"
        },
        {
            "netid": "tcp",
            "state": "ESTAB",
            "local": "192.168.1.40:54231",
            "peer": "142.250.200.14:443",
            "process": "chrome (PID: 3456)"
        },
    ]


def get_linux_socket_data():
    result = subprocess.check_output(["ss", "-tulnp"], encoding="utf-8")
    lines = result.strip().split("\n")
    socket_data_list = []

    for line in lines[1:]:
        parts = line.split()

        if len(parts) >= 6:
            process_raw = parts[6] if len(parts) > 6 else "-"

            process_match = re.search(r'"([^"]+)"', process_raw)
            pid_match = re.search(r"pid=(\d+)", process_raw)

            process_name = process_match.group(1) if process_match else "-"
            pid = pid_match.group(1) if pid_match else ""

            socket_data_list.append({
                "netid": parts[0],
                "state": parts[1],
                "local": parts[4],
                "peer": parts[5],
                "process": f"{process_name} (PID: {pid})" if pid else process_name,
            })

    return socket_data_list


def socket_list(request):
    if platform.system() == "Windows":
        socket_data_list = get_mock_socket_data()
    else:
        socket_data_list = get_linux_socket_data()

    return render(request, "auditor/socket_list.html", {"sockets": socket_data_list})