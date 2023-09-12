import json
from packages.cliente import Cliente


def guardar_clientes(clientes, archivo):
    with open(archivo, 'w') as f:
        data = [cliente.__dict__ for cliente in clientes]
        json.dump(data, f, indent=4)


def cargar_clientes(archivo):
    try:
        with open(archivo, 'r') as f:
            data = json.load(f)
            return [Cliente(**cliente_data) for cliente_data in data]
    except FileNotFoundError:
        return []
