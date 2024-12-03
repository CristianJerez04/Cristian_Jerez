from datetime import datetime, timedelta

def calcular_diferencia_horas(fecha_hora_entrada, fecha_hora_salida):
    formato = "%Y-%m-%d %H:%M:%S"
    entrada = datetime.strptime(fecha_hora_entrada, formato)
    salida = datetime.strptime(fecha_hora_salida, formato)
    diferencia = salida - entrada
    return diferencia.total_seconds()

def calcular_importe(fecha_hora_entrada, fecha_hora_salida):
    segundos_totales = calcular_diferencia_horas(fecha_hora_entrada, fecha_hora_salida)
    horas_completas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) / 60
    
    dias_completos = horas_completas // 24
    horas_restantes = horas_completas % 24

    importe_dia = 3.40 + (23 * 1.80) + 1.80 * (horas_restantes > 0) + (horas_restantes - 1) * 1.80 * (horas_restantes > 0) + 1.80 * (minutos > 0)

    importe_total = dias_completos * (3.40 + 23 * 1.80) + importe_dia
    
    return round(importe_total, 2), segundos_totales

def format_tiempo(segundos_totales):
    dias = segundos_totales // (24 * 3600)
    segundos_totales %= (24 * 3600)
    horas = segundos_totales // 3600
    segundos_totales %= 3600
    minutos = segundos_totales // 60
    segundos = segundos_totales % 60
    return f"{int(dias)} dias, {int(horas)} horas, {int(minutos)} minutos y {int(segundos)} segundos"


#print
fecha_hora_entrada = "2023-04-05 16:34:30"
fecha_hora_salida = "2023-04-08 16:45:30"
importe_total, segundos_totales = calcular_importe(fecha_hora_entrada, fecha_hora_salida)
tiempo_estacionamiento = format_tiempo(segundos_totales)
print(f"El importe total a pagar es: {importe_total} €")
print(f"Tiempo total de estacionamiento: {tiempo_estacionamiento}")

