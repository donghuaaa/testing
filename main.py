import json
import sys
from check_proxy import process_proxy  # Import fungsi dari `check_proxy.py`

if len(sys.argv) < 2:
    print("Usage: python main.py <ip:port>")
    sys.exit(1)

ip_port = sys.argv[1]
ip, port = ip_port.split(":")

status, message, country, asn, country_name, _, protocol, org, latency, lat, lon = process_proxy(ip, int(port))

result = {
    "ip": ip,
    "port": port,
    "status": message,
    "country": country_name,
    "asn": asn,
    "protocol": protocol,
    "organization": org,
    "latency_ms": latency,
    "latitude": lat,
    "longitude": lon
}

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

print(json.dumps(result, indent=4))