import SocketServer
import json

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = (self.request.recv(1024).decode('UTF-8')).strip()
            # process the data, i.e. print it:
            #data = self.request.recv(1024)
            print(data)
            # send some 'ok' back
            #self.request.sendall(bytes(json.dumps({'return':'ok'}), 'UTF-8'))
        except Exception as e:
            print("Exception wile receiving message: ", e)

server = MyTCPServer(('127.0.0.1', 6969), MyTCPServerHandler)
server.serve_forever()