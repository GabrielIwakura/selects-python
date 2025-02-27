import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootroot",
  database="cpu_maquina2"
)

mycursor = mydb.cursor()

print("Número do ATM  - Nome do ATM")
mycursor.execute("SELECT * from atms")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

maquina = int(input("Digite do ATM que deseja monitorar: "))

continuar = True

while continuar:
    opcao = input('Selecione uma opção: 1 - CPU | 2 - MEMÓRIA | 3 - DISCO ')
    match opcao:
        case '1':
            metrica = input("Qual tipo de medida deseja visualizar: 1 - Byte | 2 - Percentual ")
            
            if metrica == '1':
                mycursor.execute(f"SELECT idATM, cpuByte FROM atms JOIN metricas on idATM = fkATM WHERE idATM = {maquina}")
                myresult = mycursor.fetchall() 

                for x in myresult:
                    print(x)

            elif metrica == '2':
                mycursor.execute(f"SELECT idATM, cpuPercentual FROM atms JOIN metricas on idATM = fkATM WHERE idATM = {maquina}")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)
        
        case '2':
            metrica = input("Qual tipo de medida deseja visualizar: 1 - Byte | 2 - Percentual ")

            if metrica == '1':
                mycursor.execute(f"SELECT idATM, ramByte FROM atms JOIN metricas on idATM = fkATM WHERE idATM = {maquina}")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

            elif metrica == '2':
                mycursor.execute(f"SELECT idATM, ramPercentual FROM atms JOIN metricas on idATM = fkATM WHERE idATM = {maquina}")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

        case '3':
            metrica = input("Qual tipo de medida deseja visualizar: 1 - Byte | 2 - Percentual ")

            if metrica == '1':
                mycursor.execute(f"SELECT idATM, discoByte FROM atms JOIN metricas on idATM = fkATM WHERE idATM = {maquina}")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

            elif metrica == '2':
                mycursor.execute(f"SELECT idATM, discoPercentual FROM atms JOIN metricas on idATM = fkATM WHERE idATM = {maquina}")
                myresult = mycursor.fetchall()

                for x in myresult:
                    print(x)

    rodar = input("Deseja continuar vendo outras métricas? S/N ").lower()
    if rodar != 's':
        continuar = False

visualizar_outra_maquina = input("Deseja visualizar outra máquina? S/N ").lower()
if visualizar_outra_maquina == 's':
    maquina = int(input("Digite a máquina que deseja monitorar: "))
else:
    print("Encerrando o programa.")
