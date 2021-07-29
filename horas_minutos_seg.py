if __name__ == "__main__" : 
    print ("Ingresa cantidad de segundos")
    segundos = float(input())
    minutos = round(segundos/60)
    horas = round(segundos/3600)
    print("Horas : ",horas)
    print("Minutos : ", minutos)