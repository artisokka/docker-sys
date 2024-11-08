import socket
import subprocess
import docker
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/request-data')
def request_data():
    ip_address = socket.gethostbyname(socket.gethostname())
    processes = subprocess.getoutput("ps -ax")
    disk_space = subprocess.getoutput("df -h /")
    uptime = subprocess.getoutput("uptime -p")
    
    data = {
        "IP Address": ip_address,
        "Processes": processes,
        "Disk Space": disk_space,
        "Uptime": uptime
    }
    return jsonify(data)

@app.route('/stop', methods=['POST'])
def stop_service():
    try:
        client = docker.from_env()
        containers = client.containers.list()
        
        for container in containers:
            if "service1-" in container.name:
                container.stop()
            elif "service2-" in container.name:
                container.stop()
            elif "nginx-" in container.name:
                container.stop()

    except subprocess.CalledProcessError as e:
        return f"Error stopping containers: {e}", 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)
