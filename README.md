# EX01 Developing a Simple Webserver

# Date: 19-11-2026
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
...
from http.server import HTTPServer,BaseHTTPRequestHandler
content='''
<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body>

    <h1>TCP/IP Protocol Suite</h1>
    <h3>Name: Sanjana Singh</h3>
    <h3>Register Number: 26008903</h3>

    <table border="1">
        <tr>
            <th>Layer</th>
            <th>Protocol</th>
            <th>Function</th>
        </tr>

        <tr>
            <td>Application</td>
            <td>HTTP</td>
            <td>Transfers web pages</td>
        </tr>

        <tr>
            <td>Application</td>
            <td>FTP</td>
            <td>Transfers files</td>
        </tr>

        <tr>
            <td>Application</td>
            <td>DNS</td>
            <td>Converts domain names into IP addresses</td>
        </tr>

        <tr>
            <td>Application</td>
            <td>SMTP</td>
            <td>Sends emails</td>
        </tr>

        <tr>
            <td>Transport</td>
            <td>TCP</td>
            <td>Reliable data transmission</td>
        </tr>

        <tr>
            <td>Transport</td>
            <td>UDP</td>
            <td>Fast data transmission</td>
        </tr>

        <tr>
            <td>Internet</td>
            <td>IP</td>
            <td>Addressing and routing packets</td>
        </tr>

        <tr>
            <td>Network Access</td>
            <td>Ethernet</td>
            <td>Transfers data through a network</td>
        </tr>

    </table>

</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request recieved...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())
print("This is my webserver")
server_address=('',8000)
httpd= HTTPServer(server_address,MyServer)
httpd.serve_forever()
...
 #OUtput
 ![alt text](<Screenshot (18).png>)
 ![alt text](<Screenshot (16).png>)

 #RESULT:
The program for implementing simple webserver is executed successfully.
