import subprocess
from django.shortcuts import render

def socket_list(request):
    # Run the 'ss' command to get socket statistics
    # -t: TCP, -u: UDP, -l: Listening, -n: Numeric, -p: Process
    result = subprocess.check_output(['ss', '-tulnp'], encoding='utf-8')

    context = {
        'sockets_data': result
    }
    return render(request, 'auditor/socket_list.html', context)