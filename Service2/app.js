const express = require('express');
const { execSync } = require('child_process');
const os = require('os');

const app = express();
function getSystemInfo() {
    // Get specs
    const ipAddress = execSync("hostname -I").toString().trim();
    const processes = execSync("ps -ax").toString();
    const diskSpace = execSync("df -h /").toString();
    const uptime = execSync("uptime -p").toString();

    return {
        "IP Address": ipAddress,
        "Processes": processes,
        "Disk Space": diskSpace,
        "Uptime": uptime
    };
}

app.get('/system-info', (req, res) => {
    const info = getSystemInfo();
    res.json(info);
});

app.get('/', (req, res) => {
    res.send('Hello! This is Service2.');
});

app.listen(5001, () => {
    console.log('Service2 is running on port 5001');
});
