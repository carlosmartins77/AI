import random



class Semaforo:
    N_SEMAFORO = 0
    def __init__(self):
        Semaforo.N_SEMAFORO += 1
        self.id = Semaforo.N_SEMAFORO
        self.estado_semaforo = "Vermelho"
        self.tempo_estado = 0

class Rua:
    N_RUA = 0
    def __init__(self, rua, n_carros, semaforo):
        Rua.N_RUA += 1
        self.id = Rua.N_RUA
        self.rua = rua
        self.n_carros = n_carros
        self.semaforo = semaforo

    def __str__(self):
        return f"ID RUA: {self.id} | Rua: {self.rua}, Número de Carros: {self.n_carros}, Semaforo ID: {self.semaforo.id}, Estado do Semaforo: {self.semaforo.estado_semaforo}"


def gerar_nome_rua():
    nomes = ["Machado", "Camões", "Afonso", "Beatriz", "Clara"]
    caracteristicas = ["Monte", "Vale", "Rio", "Lago", "Jardim"]
    plantas = ["Carvalho", "Cedro", "Pinheiro", "Rosa", "Lírio"]
    sufixos = ["Rua", "Avenida", "Travessa", "Largo", "Praça"]

    nome = random.choice(nomes)
    caracteristica = random.choice(caracteristicas)
    planta = random.choice(plantas)
    sufixo = random.choice(sufixos)

    nome_rua = f"{sufixo} {nome} {caracteristica} {planta}"

    return nome_rua

def criar_ambiente():
    
    s1 = Semaforo()
    s2 = Semaforo()
    s3 = Semaforo()
    s4 = Semaforo()

    ruas = [] 

    ruas.append(Rua(gerar_nome_rua(), 5, s1))
    ruas.append(Rua(gerar_nome_rua(), 5, s2))
    ruas.append(Rua(gerar_nome_rua(), 5, s3))
    ruas.append(Rua(gerar_nome_rua(), 5, s4))

    return ruas

def main():
    ruas = criar_ambiente()

    for rua in ruas:
        if rua.id == 1:
            estado_semaforo = rua.semaforo.estado_semaforo
            print(f"Estado do Semaforo da Rua com ID 1: {estado_semaforo}")
            break

    

if __name__ == "__main__":
    main()

