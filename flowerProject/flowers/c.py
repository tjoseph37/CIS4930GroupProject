import socket
import sys
import select
import p
import json

BUFSIZ = 1024


class ChatClient(object):
    def __init__(self, name,data, host="tatiana-VirtualBox", port=4000):
        self.name = name
        self.flag = False
        self.port = int(port)
        self.host = host

        try:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.host, self.port))

		pt = bytearray(data)
		cypherkey = [143,194,34,208,145,203,230,143,177,246,97,206,145,92,255,84]
		iv = [103,35,148,239,76,213,47,118,255,222,123,176,106,134,98,92]
		olen, ciph = p.encrypt(pt,cypherkey, p.keySize["SIZE_128"], iv)
		message = dict()
		message['olen']=olen
		message['iv']=iv
		message['ciph']=ciph
		data_string = json.dumps(message)
		#print "done"
		if self.sock.send(data_string):
			pass
		#print "successful"
        except socket.error, e:
          pass

    def cmdloop(self):
        while not self.flag:
            try:
                inputready, outputready,exceptrdy = select.select([self.sock], [],[])
                for i in inputready:
                    if i == self.sock:
                        data = ''
                        temp = self.sock.recv(BUFSIZ)
                        data = data+temp
                        while len(temp)==BUFSIZ:
                            temp = self.sock.recv(BUFSIZ)
                            data = data+temp
                        if not data:
                            print 'Shutting down.'
                            self.flag = True
                            break
                        else:
                            return data
                            
            except KeyboardInterrupt:
                print 'Interrupted.'
                self.sock.close()
                break
            
            
if __name__ == "__main__":
    import sys

    if len(sys.argv)<3:
        sys.exit('Usage: %s chatid host portno' % sys.argv[0])
        
    client = ChatClient(sys.argv[1],None,sys.argv[2], int(sys.argv[3]))
