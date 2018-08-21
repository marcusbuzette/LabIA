import json
import time

obj =''' {

	"lista" :[
	{"nome": "Arad",
	"heuristica": 366,
	"arestas": [{"proximo": "Sibiu",
				"custo": 140},
				{"proximo": "Zerind",
				"custo": 75}]},

	{"nome": "Bucharest",
	"heuristica": 0,
	"arestas": ""},

	{"nome": "Craiova",
	"heuristica": 160,
	"arestas": [{"proximo": "Doberta",
				"custo": 120},
				{"proximo": "Pitesti",
				"custo": 138},
				{"proximo": "Rimnicu Vilcea",
				"custo": 145}]},

	{"nome": "Doberta",
	"heuristica": 242,
	"arestas": [{"proximo": "Craiova",
				"custo": 120},
				{"proximo": "Melhadia",
				"custo": 75}]},

	{"nome": "Eforie",
	"heuristica": 161,
	"arestas": [{"proximo": "Hirsova",
				"custo": 86}]},

	{"nome": "Fagaras",
	"heuristica": 176,
	"arestas": [{"proximo": "Sibiu",
				"custo": 99},
				{"proximo": "Bucharest",
				"custo": 211}]},

	{"nome": "Giurgiu",
	"heuristica": 77,
	"arestas": [{"proximo": "Bucharest",
				"custo": 90}]},

	{"nome": "Hirsova",
	"heuristica": 151,
	"arestas": [{"proximo": "Eforie",
				"custo": 85},
				{"proximo": "Urziceni",
				"custo": 98}]},

	{"nome": "Iasi",
	"heuristica": 226,
	"arestas": [{"proximo": "Neamt",
				"custo": 87},
				{"proximo": "Vaslui",
				"custo": 92}]},

	{"nome": "Lugoj",
	"heuristica": 244,
	"arestas": [{"proximo": "Melhadia",
				"custo": 70},
				{"proximo": "Timisoara",
				"custo": 111}]},

	{"nome": "Melhadia",
	"heuristica": 241,
	"arestas": [{"proximo": "Lugoj",
				"custo": 70},
				{"proximo": "Doberta",
				"custo": 75}]},

	{"nome": "Neamt",
	"heuristica": 234,
	"arestas": [{"proximo": "Iasi",
				"custo": 87}]},

	{"nome": "Oradea",
	"heuristica": 380,
	"arestas": [{"proximo": "Sibiu",
				"custo": 151},
				{"proximo": "Zerind",
				"custo": 71}]},

	{"nome": "Pitesti",
	"heuristica": 10,
	"arestas": [{"proximo": "Bucharest",
				"custo": 101},
				{"proximo": "Rimnicu Vilcea",
				"custo": 97}]},

	{"nome": "Rimnicu Vilcea",
	"heuristica": 193,
	"arestas": [{"proximo": "Pitesti",
				"custo": 97},
				{"proximo": "Sibiu",
				"custo": 80},
				{"proximo": "Craiova",
				"custo": 145}]},

	{"nome": "Sibiu",
	"heuristica": 253,
	"arestas": [{"proximo": "Oradea",
				"custo": 151},
				{"proximo": "Arad",
				"custo": 140},
				{"proximo": "Rimnicu Vilcea",
				"custo": 80},
				{"proximo": "Fagaras",
				"custo": 99}]},

	{"nome": "Timisoara",
	"heuristica": 329,
	"arestas": [{"proximo": "Arad",
				"custo": 118},
				{"proximo": "Lugoj",
				"custo": 111}]},

	{"nome": "Urziceni",
	"heuristica": 80,
	"arestas": [{"proximo": "Hirsova",
				"custo": 98},
				{"proximo": "Bucharest",
				"custo": 85},
				{"proximo": "Vaslui",
				"custo": 142}]},

	{"nome": "Vaslui",
	"heuristica": 199,
	"arestas": [{"proximo": "Iasi",
				"custo": 92},
				{"proximo": "Urziceni",
				"custo": 142}]},

	{"nome": "Zerind",
	"heuristica": 374,
	"arestas": [{"proximo": "Arad",
				"custo": 75},
				{"proximo": "Oradea",
				"custo": 71}]}
	
]}
'''

entrada = json.loads(obj);
lista = entrada['lista'];




resposta = {
	"nos": [
	]
}

estado_inicial = 'Lugoj'
estado_final = 'Bucharest'
no_inicial = ''
estado_atual = ''
estado_anterior = ''

f_total = 0;
g = 0;
h = 0;

#Buscar no estados

def buscarEstado(nome):
	for no in lista:
		if no['nome'] == nome:
			#print('No Inicial: ' + no['nome'])
			return no;
	

	return ''

def verifica_prox_estado(nome_estado): #verifica se o proximo estado e valido
	#verifica se a o estadoja esta no array resposta
	for no in resposta['nos']:
		if no['nome'] == nome_estado:
			return False;




	return True;


def verifica_final(nome):


	if nome == estado_final:
		return False;

	else:
		return True;


def get_heuristica_proximo_estado(nome):
	estado = buscarEstado(nome);
	heuristica = estado['heuristica']
	return heuristica;




no_inicial = buscarEstado(estado_inicial)

print('--------------')
estado_atual = no_inicial;

#(no_inicial)
#print(resposta['nos'][0]['nome']);
resposta['nos'].append(estado_atual);
aux_h = 0
aux_e = ''
aresta = 0;


#Busca em A*

while verifica_final(estado_atual['nome']):
	
	#print('Estado Atual: '+estado_atual['nome']);
	for proximo in estado_atual['arestas']:
		
		
		#print('Proximo Aresta:  ' +proximo['proximo'])
		
		#se for primeira aresta
		if aresta == 0:

			#print('Primeira aresta Verificada: '+ proximo['proximo'])
			if  verifica_prox_estado(proximo['proximo']) :

				print('\n\n\n')
				print('Estado Atual: ' +  estado_atual['nome'])
				print('Proximo Analisado: ' + proximo['proximo'])
				print('G(n) = ' + str(proximo['custo']))
				print('H(n) = ' + str(get_heuristica_proximo_estado(proximo['proximo'])))
				
				
				aux_h = f_total+ get_heuristica_proximo_estado(proximo['proximo'])+ proximo['custo'];
				aux_e = proximo;
				print('F(n) = ' + str(aux_h))
				#print("Aresta aceita")
				aresta+=1;
			

		# se nao verifica se a nova aresta tem heuristica melhor
		else:

			#print("ELSE:   "+proximo['proximo'])

			if f_total+ get_heuristica_proximo_estado(proximo['proximo']) + proximo['custo'] < aux_h and verifica_prox_estado(proximo['proximo']) :
				

				print('\n\n\n')
				print('Estado Atual: ' +  estado_atual['nome'])
				print('Proximo Analisado: ' + proximo['proximo'])
				print('G(n) = ' + str(proximo['custo']))
				print('H(n) = ' + str(get_heuristica_proximo_estado(proximo['proximo'])))
				
				#print("Aresta aceita")
				#print('Antes: ' + aux_h);
				aux_h = f_total+ estado_atual['heuristica'] + proximo['custo'];
				aux_e = proximo;
				print('F(n) = ' + str(aux_h))
				#print('Depois' + aux_h);
				aresta+=1;

		
		time.sleep(2);


	#print(estado_atual['nome'])
	#print(aux_h)
	#print(aux_e)

	#(resposta['nos']['nome'])


	prox_estado = buscarEstado(aux_e['proximo']);

	

	resposta['nos'].append(estado_atual);
	estado_atual = prox_estado;
	#print('Estado Atual: ' + estado_atual['nome']);
	aux_h = 0
	aux_e = ''
	aresta = 0
	print('\n ----------------------- \n' )


if estado_atual['nome'] == estado_final:
	print('Voce chegou a '+ estado_atual['nome'])


			
					



			
			
				

		
			

	



	






