from GraphCreator import GraphCreator
from DjikstraAlgorithm import DjikstraAlgorithm


if __name__ == '__main__':
    graph = GraphCreator(".\\rutas.txt")

    while True:
        print("\nBienvenido al asistente de mapa para la región.")
        region = input("¿Dónde te encuentras actualmente? (Ingresa la aldea): ")

        destination = input("\nIngresa la aldea de destino: ")

        distancia, path = DjikstraAlgorithm(graph.createGraph()).distanceDjikstra("Aldea Fuego", "Aldea Azalea")
        print("\nLa mejor trayectoria desde", region, "hasta", destination, "es:")
        print("Distancia:", distancia)
        print("Trayectoria en orden:", path)

        res = input("\n¿Quieres observar el mapa? (Sí = 1, No = 0): ")
        if res == "1":
            graph.graphicGraph()
        else:
            pass

        res = input("\n¿Quieres continuar? (Sí = 1, No = 0): ")
        if res == "0":
            print("Aqui estamos para cualquier consulta!")
            break

