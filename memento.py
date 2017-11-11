#!/usr/bin/env python
# encoding: utf-8
# file: memento.py
"""
Memento

Captura el estado interno de un objeto sin destruir la encapsulación y lo guárda en el objeto

Luego restaurará el objeto a su estado original de preservación

- Guardará los detalles del objeto
- Es adecuado para funciones complejas, necesitan mantener o registrar el historial de la propiedad, o 
  necesita guardar algunos atributos
- Por ejemplo: guardar el comando de historial y realizar la operación de deshacer
- La nota borra la información interna del objeto complicado a otros objetos
"""


class Originator(object):
    """
    Esta Clase:
	1. Crea un Memento para registrar el estado interno del estado actual (create_memento) y 
	2. para restablecer el estado interno del objeto Memeno
    """

    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value

    def create_memento(self):
        return Memento(self.__state)

    def set_memento(self, memento):
        self.__state = memento.state

    def show(self):
        print ('Estado: {}'.format(self.__state))


class Memento(object):
    """
    Es responsable de almacenar el estado interno enviado desde el Originator e 
	impedir el acceso a objetos distintos de Originator
    """
    def __init__(self, state):
        self.__state = state

    @property
    def state(self):
        return self.__state


class Caretaker(object):
    """
   Responsable de mantener el memorándum Memento
    """
    def __init__(self):
        self.__memento = None

    @property
    def memento(self):
        return self.__memento

    @memento.setter
    def memento(self, value):
        self.__memento = value


if __name__ == '__main__':
    o = Originator("init")
    o.show()
    o.state = "begin"
    o.show()

    mem = o.create_memento()

    # save it
    c = Caretaker()
    c.memento = mem

    o.state = "change"
    o.show()

    # recover
    o.set_memento(c.memento)
    o.show()
