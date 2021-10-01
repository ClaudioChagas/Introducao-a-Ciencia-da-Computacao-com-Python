segundos=input("por favor, entre com o número de segundos que deseja converter: ")
dia= segundos // 86400
segundos_rest= segundos % 86400
horas= segundo_rest // 3600
segundos_rest= segundos_rest % 3600
minutos= segundos_rest // 60
segundos_rest= segundos_rest % 60
print(dia, "dias,",horas,"horas,",minutos, "minutos e",segundos_rest,"segundos.")