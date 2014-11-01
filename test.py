import SocketServer
import json
import gensim
import nltk
from gensim import corpora, models, similarities

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            data = (self.request.recv(1024).decode('UTF-8'))
            # process the data, i.e. print it:
            #data = (self.request.recv(1024).decode('UTF-8')).strip()
            json_data = json.loads(data);
            #print(json_data['content']);
            #print (data);
            #tokens = nltk.word_tokenize(json_data["content"])
            #print(tokens);
            #Send back the results
            self.request.sendall("str");
        except Exception as e:
            print("Exception wile receiving message: ", e)

#Implement client here

if __name__ == '__main__':
	corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
	[(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
	[(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
	[(0, 1.0), (4, 2.0), (7, 1.0)],
	[(3, 1.0), (5, 1.0), (6, 1.0)],
	[(9, 1.0)],
	[(9, 1.0), (10, 1.0)],
	[(9, 1.0), (10, 1.0), (11, 1.0)],
	[(8, 1.0), (10, 1.0), (11, 1.0)]]

	tfidf = models.TfidfModel(corpus)
	vec = [(0, 1), (4, 1)]
	print(tfidf[vec])
	
	index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)
	sims = index[tfidf[vec]]

	print sims
	print(list(enumerate(sims)))
	
	server = MyTCPServer(('127.0.0.1', 6969), MyTCPServerHandler)
	server.serve_forever()
