import subprocess
import re # Añade esta importación arriba
from django.shortcuts import render

def socket_list(request):
    result = subprocess.check_output(['ss', '-tulnp'], encoding='utf-8')
    lines = result.strip().split('\n')
    socket_data_list = []

    for line in lines[1:]:
        parts = line.split()
        if len(parts) >= 6:
            # Usamos regex para sacar el nombre del proceso y el PID
            process_raw = parts[6] if len(parts) > 6 else "-"
            process_match = re.search(r'"([^"]+)"', process_raw)
            pid_match = re.search(r'pid=(\d+)', process_raw)

            process_name = process_match.group(1) if process_match else "-"
            pid = pid_match.group(1) if pid_match else ""

            socket_data_list.append({
                'netid': parts[0],
                'state': parts[1],
                'local': parts[4],
                'peer': parts[5],
                'process': f"{process_name} (PID: {pid})" if pid else process_name
            })

    return render(request, 'auditor/socket_list.html', {'sockets': socket_data_list})