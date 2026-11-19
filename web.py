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