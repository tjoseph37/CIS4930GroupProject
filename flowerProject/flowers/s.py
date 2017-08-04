import select
import socket
import sys
import signal
import p
import json
import tensorflow as tf
import sys
import os

BUFSIZ = 1024
counter = 0

def classify(name):
	return "hey mom"

class ChatServer(object):
    def __init__(self, port=4000, backlog=5):
        self.clients = 0
        self.clientmap = {}

        self.outputs = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((socket.gethostname(),port))
	print socket.gethostname()
        self.server.listen(backlog)
        signal.signal(signal.SIGINT, self.sighandler)
    
    def decrypt(self,sock, olen,ciph,iv):
        key = [143,194,34,208,145,203,230,143,177,246,97,206,145,92,255,84]
        decr = p.decrypt(ciph,olen,key,p.keySize["SIZE_128"],iv)
        name = "given_flower.png"
        f = open(name,"w")
        f.write(decr)
        f.close()
        result = classify(name)
        for socket in self.outputs:
            if socket == sock :
                try :
                    socket.send(result)
                except :
                    socket.close()
                    self.outputs.remove(socket)
        print "done"

    def sighandler(self, signum, frame):
        print 'Shutting down server...'
        for o in self.outputs:
            o.close()
        self.server.close()

    def getname(self, client):
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def serve(self):
        inputs = [self.server,sys.stdin]
        self.outputs = []
        running = 1
        while running:
            try:
                inputready,outputready,exceptready = select.select(inputs, self.outputs, [])
            except select.error, e:
                break
            except socket.error, e:
                break
            
            for s in inputready:
                if s == self.server:
                    client, address = self.server.accept()
                    self.clients += 1
                    inputs.append(client)
                    self.outputs.append(client)
                else:
                    try:
                        data = ''
                        temp = s.recv(BUFSIZ)
                        data = data+temp
                        while len(temp)==BUFSIZ:
                            temp = s.recv(BUFSIZ)
                            data = data+temp
                        data_loaded = json.loads(data)
                        olen = data_loaded['olen']
                        ciph = data_loaded['ciph']
                        iv = data_loaded['iv']
                        if olen and ciph and iv:
                            print iv
                            self.decrypt(s,olen,ciph,iv)
                        else:
                            print 'chatserver: %d hung up' % s.fileno()
                            self.clients -= 1
                            s.close()
                            inputs.remove(s)
                            self.outputs.remove(s)            
                    except socket.error, e:
                        inputs.remove(s)
                        self.outputs.remove(s)
        self.server.close()

if __name__ == "__main__":
    ChatServer().serve()

