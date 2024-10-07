import os
import socket
import subprocess
import time
import requests
from flask import Flask, jsonify

app = Flask(__name__)

def get_system_info():
    # Get specs
    ip_address = socket.gethostbyname(socket.gethostname())
    processes = subprocess.getoutput("ps -ax")
    disk_space = subprocess.getoutput("df -h /")
    uptime = subprocess.getoutput("uptime -p")

    return {
        "IP Address": ip_address,
        "Processes": processes,
        "Disk Space": disk_space,
        "Uptime": uptime
    }

@app.route('/')
def get_info():
    service1_info = get_system_info()
    
    # Request to Service2
    service2_response = requests.get("http://service2:5001/system-info")
    service2_info = service2_response.json() if service2_response.ok else {"error": "Could not get data from Service2"}
    
    combined_info = {
        "Service1": service1_info,
        "Service2": service2_info
    }
    return jsonify(combined_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)
