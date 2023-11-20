import pandas as pd

class Semaforo:
    def __init__(self, frente, direita, esquerda):
        self.frente = frente
        self.direita = direita
        self.esquerda = esquerda

    def change_light(self, direction, color):
        setattr(self, direction, color)

def can_car_move(street, direction, semaforos):
    if street == 1:
        if direction == 'Right':
            return semaforos[3].frente == "Vermelho" and semaforos[2].esquerda == "Vermelho"
        elif direction == 'Front':
            return semaforos[3].frente == "Vermelho" and semaforos[3].esquerda == "Vermelho" and \
                   semaforos[2].esquerda == "Vermelho" and semaforos[1].frente == "Vermelho" and \
                   semaforos[1].esquerda == "Vermelho" and semaforos[1].direita == "Vermelho"
        elif direction == 'Left':
            return semaforos[3].esquerda == "Vermelho" and semaforos[3].frente == "Vermelho" and \
                   semaforos[2].frente == "Vermelho" and semaforos[2].esquerda == "Vermelho" and \
                   semaforos[2].direita == "Vermelho" and semaforos[1].frente == "Vermelho" and \
                   semaforos[1].esquerda == "Vermelho"

    elif street == 2:
        if direction == 'Right':
            return semaforos[0].frente == "Vermelho" and semaforos[3].esquerda == "Vermelho"
        elif direction == 'Front':
            return semaforos[0].frente == "Vermelho" and semaforos[0].esquerda == "Vermelho" and \
                   semaforos[3].esquerda == "Vermelho" and semaforos[2].frente == "Vermelho" and \
                   semaforos[2].esquerda == "Vermelho" and semaforos[2].direita == "Vermelho"
        elif direction == 'Left':
            return semaforos[0].esquerda == "Vermelho" and semaforos[0].frente == "Vermelho" and \
                   semaforos[3].frente == "Vermelho" and semaforos[3].esquerda == "Vermelho" and \
                   semaforos[3].direita == "Vermelho" and semaforos[2].frente == "Vermelho" and \
                   semaforos[2].esquerda == "Vermelho"

    elif street == 3:
        if direction == 'Right':
            return semaforos[1].frente == "Vermelho" and semaforos[0].esquerda == "Vermelho"
        elif direction == 'Front':
            return semaforos[1].frente == "Vermelho" and semaforos[1].esquerda == "Vermelho" and \
                   semaforos[0].esquerda == "Vermelho" and semaforos[3].frente == "Vermelho" and \
                   semaforos[3].esquerda == "Vermelho" and semaforos[3].direita == "Vermelho"
        elif direction == 'Left':
            return semaforos[1].esquerda == "Vermelho" and semaforos[1].frente == "Vermelho" and \
                   semaforos[0].frente == "Vermelho" and semaforos[0].esquerda == "Vermelho" and \
                   semaforos[0].direita == "Vermelho" and semaforos[3].frente == "Vermelho" and \
                   semaforos[3].esquerda == "Vermelho"

    elif street == 4:
        if direction == 'Right':
            return semaforos[2].frente == "Vermelho" and semaforos[1].esquerda == "Vermelho"
        elif direction == 'Front':
            return semaforos[2].frente == "Vermelho" and semaforos[2].esquerda == "Vermelho" and \
                   semaforos[1].esquerda == "Vermelho" and semaforos[0].frente == "Vermelho" and \
                   semaforos[0].esquerda == "Vermelho" and semaforos[0].direita == "Vermelho"
        elif direction == 'Left':
            return semaforos[2].esquerda == "Vermelho" and semaforos[2].frente == "Vermelho" and \
                   semaforos[1].frente == "Vermelho" and semaforos[1].esquerda == "Vermelho" and \
                   semaforos[1].direita == "Vermelho" and semaforos[0].frente == "Vermelho" and \
                   semaforos[0].esquerda == "Vermelho"

    return False






def next_semaphore_state(data, semaforos):
    # Count the number of unresolved cars in each direction
    street_counts = data[data['Resolvido'] == 'N']['Street'].value_counts()
    # Find the street with the maximum unresolved cars
    if not street_counts.empty:
        next_street = street_counts.idxmax()
        # Set all semaphores to red
        for semaforo in semaforos:
            semaforo.change_light('frente', "Vermelho")
            semaforo.change_light('direita', "Vermelho")
            semaforo.change_light('esquerda', "Vermelho")
        # Set the selected street's semaphores to green
        semaforos[next_street - 1].change_light('frente', "Verde")
        semaforos[next_street - 1].change_light('direita', "Verde")
        semaforos[next_street - 1].change_light('esquerda', "Verde")
        return True
    return False

# Initialize DataFrame and semaphores
data = pd.read_csv('dataset1.csv', sep=';')
data['Resolvido'] = 'N'
data['PassTime'] = None

semaforo1 = Semaforo("Verde", "Verde", "Verde")
semaforo2 = Semaforo("Vermelho", "Vermelho", "Vermelho")
semaforo3 = Semaforo("Vermelho", "Vermelho", "Vermelho")
semaforo4 = Semaforo("Vermelho", "Vermelho", "Vermelho")
semaforos = [semaforo1, semaforo2, semaforo3, semaforo4]

# Simulate each second of the traffic control
total_seconds = 0
while data['Resolvido'].eq('N').any():
    for index, row in data.iterrows():
        if row['Resolvido'] == 'N':
            street = row['Street']
            direction = row['Direction']
            if can_car_move(street, direction, semaforos):
                data.at[index, 'Resolvido'] = 'Y'
                data.at[index, 'PassTime'] = total_seconds

    total_seconds += 10  # Increment time

    # Update semaphore state if all cars in current green street have passed
    if not next_semaphore_state(data, semaforos):
        break  # Exit if no more cars to process

# print(data)

#Output the results
print(data[data.PassTime == 0])
print("###################################")
print(data[data.PassTime == 10])
print("###################################")
print(data[data.PassTime == 20])

