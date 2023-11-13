import simpy

class Carro:
    def __init__(self, id, destino, env):
        self.id = id
        self.destino = destino
        self.env = env
        self.tempo_inicio = env.now
        self.tempo_viagem = 0
        self.env.process(self.viagem())

    def viagem(self):
        # Tempo de viagem fixo
        tempo_viagem_fixo = 10  # Tempo de viagem fixo para cada carro
        yield self.env.timeout(tempo_viagem_fixo)
        self.tempo_viagem = self.env.now - self.tempo_inicio

class Semaforo:
    def __init__(self, id, env):
        self.id = id
        self.env = env
        self.estado = "vermelho"
        self.fila_carros = 0
        self.env.process(self.run())

    def run(self):
        while True:
            self.estado = "verde"
            print(f"Semaforo {self.id} está agora verde.")
            # Lógica para mudar o estado do semáforo
            yield self.env.timeout(1)  # Timeout representa a duração do estado atual

    def receber_info_trafego(self, carros):
        self.fila_carros = carros

class Cruzamento:
    def __init__(self, id, semaforos):
        self.id = id
        self.semaforos = semaforos

    # Método para sincronizar semáforos, se necessário

class Ambiente:
    def __init__(self):
        self.env = simpy.Environment()
        self.destinos = ["Destino1", "Destino2", "Destino3"]  # Destinos fixos
        self.cruzamentos = self.criar_cruzamentos()
        self.carros = self.criar_carros()

    def criar_cruzamentos(self):
        # Cria cruzamentos e seus semáforos
        return [Cruzamento(id, [Semaforo(i, self.env) for i in range(4)]) for id in range(N)]

    def criar_carros(self):
        # Atribui destinos fixos aos carros
        carros = []
        for id in range(M):
            destino = self.destinos[id % len(self.destinos)]
            carros.append(Carro(id, destino, self.env))
        return carros

    def executar(self):
        self.env.run(until=TEMPO_SIMULACAO)
        self.calcular_tempo_total()

    def calcular_tempo_total(self):
        tempo_total = sum(carro.tempo_viagem for carro in self.carros)
        print(f"Tempo total de viagem de todos os carros: {tempo_total} unidades de tempo.")

# Parâmetros da simulação
N = 5  # Número de cruzamentos
M = 20  # Número de carros
TEMPO_SIMULACAO = 100

# Inicializando e executando a simulação
ambiente = Ambiente()
ambiente.executar()