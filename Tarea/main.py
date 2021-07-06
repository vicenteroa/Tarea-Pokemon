'''
Creado: Vicente Roa
'''
import math
import time
import random
from moves import get_move


# PRIMER POKEMON
class pokemon:
    def __init__(self, nombre_pokemon):
        self.nombre_pokemon = nombre_pokemon
        self.hp = 0
        self.atk = 0
        self.dfs = 0
        self.atkesp = 0
        self.dfsesp = 0
        self.vlc = 0

    def stats_total(self, nombre_pokemon):
        # ESTADISTICAS DEL POKEMON SELECCIONADO AL NIVEL 50
        self.nombre_pokemon = nombre_pokemon
        self.ev = 0
        self.iv = 0
        self.hp_total = 0
        self.atk_total = 0
        self.dfs_total = 0
        self.atkesp_total = 0
        self.dfsesp_total = 0
        self.vlc_total = 0


nombrepokemon = input("ingresa el nombre del pokemon: ").lower()
libro = open('pokemon_data.csv')
for i in libro:
    linea = i.strip().split(",")
    if nombrepokemon == linea[0]:
        # PKM GUARDARA LOS DATOS DE NOMBRE Y ESTADISTICAS
        tipo = linea[1]
        pkm = pokemon(linea[0])
        pkm.hp = linea[2]
        pkm.atk = (linea[3])
        pkm.dfs = (linea[4])
        pkm.atkesp = (linea[5])
        pkm.dfsesp = (linea[6])
        pkm.vlc = (linea[7])

        time.sleep(0.1)

        print(f'Nombre del pokemon seleccionado: {pkm.nombre_pokemon}')
        print("ESTADISTICAS DEL POKEMON")
        print(" ")
        print(f'-HP= {pkm.hp}')
        print(f'-Ataque= {pkm.atk}')
        print(f'-Defensa= {pkm.dfs}')
        print(f'-Ataque Especial= {pkm.atkesp}')
        print(f'-Defensa Especial= {pkm.dfsesp}')
        print(f'-Velocidad= {pkm.vlc}')
        print(" ")
        time.sleep(1)
        print("Movimientos que puede aprender el pokémon: ")
        print(" ")

        movimientos = linea[8].split(";")
        for g in range(len(movimientos)):
            print(f'{g}.-{movimientos[ g ]}')
            print(" ")
        op_movimiento = linea[8].split(";")

        for e in range(len(op_movimiento)):
            ataque_seleccionado = int(
                input("Seleccione un ataque a ejecutar: "))
            mov = op_movimiento[ataque_seleccionado]
            print(
                f"el ataque seleccionado es: {op_movimiento[ ataque_seleccionado ]}"
            )
            break

        stats_finales = pokemon(linea[0])
        stats_finales.ev = float(250)
        stats_finales.iv = float(31)
        stats_finales.hp_total = float(linea[2])
        stats_finales.atk_total = float(linea[3])
        stats_finales.dfs_total = float(linea[4])
        stats_finales.atkesp_total = float(linea[5])
        stats_finales.dfsesp_total = float(linea[6])
        stats_finales.vlc_total = float(linea[7])

        #SE SACAN LOS RESULTADOS DEL POKEMON ELEGIDO AL NIVEL 50

        resultado_hp = ((
            (((stats_finales.hp_total + stats_finales.iv) * 2) +
             (math.sqrt(stats_finales.ev) / 4)) * 50) / 100) + 50 + 10
        print(f'El hp al nivel 50 de {linea[ 0 ]} es: {resultado_hp}')
        resultado_atk = (((((stats_finales.atk_total + stats_finales.iv) * 2) +
                           (math.sqrt(stats_finales.ev) / 4)) * 50) / 100) + 5
        print(f'El atk al nivel 50 de {linea[ 0 ]} es: {resultado_atk}')
        resultado_dfs = (((((stats_finales.dfs_total + stats_finales.iv) * 2) +
                           (math.sqrt(stats_finales.ev) / 4)) * 50) / 100) + 5
        print(f'La defensa al nivel 50 de {linea[ 0 ]} es: {resultado_dfs}')
        resultado_atkesp = ((
            (((stats_finales.atkesp_total + stats_finales.iv) * 2) +
             (math.sqrt(stats_finales.ev) / 4)) * 50) / 100) + 5
        print(f'El spa al nivel 50 de {linea[ 0 ]} es: {resultado_atkesp}')
        resultado_dfskesp = ((
            (((stats_finales.dfsesp_total + stats_finales.iv) * 2) +
             (math.sqrt(stats_finales.ev) / 4)) * 50) / 100) + 5
        print(f'El spd al nivel 50 de {linea[ 0 ]} es: {resultado_dfskesp}')
        resultado_vlc = (((((stats_finales.vlc_total + stats_finales.iv) * 2) +
                           (math.sqrt(stats_finales.ev) / 4)) * 50) / 100) + 5
        print(f'El spe al nivel 50 de {linea[ 0 ]} es: {resultado_dfskesp}')


# SEGUNDO POKEMON
class pokemon_2:
    def __init__(self, nombre_pokemon2):
        self.nombre_pokemon2 = nombre_pokemon2
        self.hp_pkm2 = 0
        self.def_pkm2 = 0
        self.defesp_pkm2 = 0


nombrepokemon2 = input('Nombre del Segundo Pokémon seleccionado: ').lower()
libro = open('pokemon_data.csv')
for l in libro:
    line = l.strip().split(",")
    if nombrepokemon2 == line[0]:
        pkm2_tipo = line[1]
        pkm2 = pokemon_2(line[0])
        pkm2.ev = float(250)
        pkm2.iv = float(31)
        pkm2.hp_pkm2 = float(line[2])
        pkm2.def_pkm2 = float(line[4])
        pkm2.defesp_pkm2 = float(line[6])
        print(" ")

        hp_pkm2 = (((((pkm2.hp_pkm2 + pkm2.iv) * 2) +
                     (math.sqrt(pkm2.ev) / 4)) * 50) / 100) + 50 + 10
        print(f"El hp de {pkm2.nombre_pokemon2} es de: {hp_pkm2}")
        print("")
        time.sleep(2)

        defs_pkm2 = (((((pkm2.def_pkm2 + pkm2.iv) * 2) +
                       (math.sqrt(pkm2.ev) / 4)) * 50) / 100) + 5

        defsesp_pkm2 = (((((pkm2.defesp_pkm2 + pkm2.iv) * 2) +
                          (math.sqrt(pkm2.ev) / 4)) * 50) / 100) + 5


def calculo_ataque():  # FORMULA DEMAGE

    movimiento_seleccionado = get_move(mov)

    #SE ABRE LA TABLA DE EFECTIVIDAD
    tabla = open('tabla_efectividad.csv', 'r')
    tabla_efectividad = tabla.readlines()
    tabla.close()

    #VARIABLES A UTILIZAR PARA EL ATAQUE Y MODIFIER
    rnd = random.uniform(0.85, 1.0)
    tipo_pkm = tipo
    tipo_pkm2 = pkm2_tipo
    atk_tipo = movimiento_seleccionado[2]

    for i in tabla_efectividad:
        i = i.split(',')
        if tipo_pkm == atk_tipo:
            stab = 1.2
        else:
            stab = 1.0

    efectividad = tabla_efectividad[0].split(',')
    for r in efectividad:
        if r == tipo_pkm:
            selec_atk_efect = efectividad.index(r)
    for e in tabla_efectividad:
        e = e.split(',')
        if e[0] == tipo_pkm2:
            type = float(e[selec_atk_efect])

    modifier = type * stab * rnd * 1  #FORMULA PARA SACAR EL MODIFIER SE GUARADARA EN UNA VARIABLE PARA USARLA EN EL DAÑO TOTAL

    for i in range(len(movimiento_seleccionado)):
        estadisticas_ataque = float(movimiento_seleccionado[1])
        categoria = movimiento_seleccionado[3]

        #EN ESTA PARTE SE HACE UNA CONDICI0NAL PARA SABER SI EL ATAQUE ES ESPECIAL O NO PARA ASI DETERMINAR QUE
        #CATEGORIA USARA PARA CALCULAR EL DAÑO DEL POKEMON
        if categoria == 'special':
            a = resultado_atkesp
            d = defsesp_pkm2
        else:
            a = resultado_atk
            d = defs_pkm2

        #DAÑO TOTAL QUE LE HARA EL POKEMON ATACANTE AL POKEMON RIVAL

        daño_total = ((((2 * 50) / 5 + 2) * estadisticas_ataque * a / d) / 50 +
                      2) * modifier

        if categoria == 'special':
            resto = (defsesp_pkm2 - daño_total)
        else:
            resto = (defs_pkm2 - daño_total)

        return f'{nombrepokemon2} quedo con un HP de:{resto}'


print(calculo_ataque())
