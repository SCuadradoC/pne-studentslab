import http.client
import json
import termcolor

PORT = 80
SERVER = 'rest.ensembl.org'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/info/ping?content-type=application/json")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

#print(data1)

# -- Create a variable with the data,
# -- form the JSON received
rj1 = json.loads(data1)

if rj1["ping"] == 1:
    print("PING OK, the database is running")