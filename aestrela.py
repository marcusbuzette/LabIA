import json

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
				"custo": 138,
				"proximo": "Rimnicu Vilcea",
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

print(entrada['lista'][0]['nome']);