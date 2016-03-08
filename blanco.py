class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):

        #TODO: completar con la inicializacion de los parametros del objeto
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final

        pass

    def reflejar(self, senal, tiempo_inicial, tiempo_final):

        
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo

        import math
        
        import numpy

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo

        muestras = range(cantidad_muestras)
        
        ret = senal + [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]
        pass
        
