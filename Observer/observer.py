#!/usr/bin/env python
# encoding: utf-8
# file: observer.py
"""
Patrón observador

Define un tipo de dependencias de uno a muchos, de manera que múltiples objetos observadores monitoreen simultáneamente
 un objeto de tema; si el objeto cambia, notificará a todos los objetos observadores, 
 para que puedan actualizarlo automáticamente

- Aplicable: cuando un objeto cambia necesita cambiar otros objetos al mismo tiempo
- El desacoplamiento permite que ambas partes del acoplamiento dependan de la abstracción en lugar de la dependencia del concreto
"""

from abc import ABCMeta, abstractmethod


class Subject(object):
    """
   Guarde todas las referencias a los objetos del observador en un solo agregado
     Cada sujeto puede tener cualquier número de observadores.

     Los temas abstractos proporcionan interfaces para agregar / eliminar objetos observadores
    """

    def __init__(self):
        self.__observers = []

    def attach(self, observer):
        self.__observers.append(observer)

    def detach(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for o in self.__observers:
            o.update()


class ConcreteSubject(Subject):
    """
	la clase concreta del sujeto, el estado en el objeto observador específico
     Todos los observadores registrados son notificados cuando cambia el estado interno de un tema en particular
    """

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value


class Observer(object):
    """
Los observadores abstractos definen todas las interfaces para observadores específicos y 
se actualizan cuando reciben notificaciones temáticas
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self):
        pass


class ConcreteObserver(Observer):
    """
Observadores concretos, interfaces de actualización que implementan requisitos abstractos de bloqueo del observador
     Para reconciliar su propio estado con el estado del sujeto
    """
    def __init__(self, subject, name):
        self.subject = subject
        self.name = name
        self.objserver_staus = None

    def update(self):
        self.objserver_staus = self.subject.status
        print ('the observer: %s status change to %s' % (self.name , self.objserver_staus))


if __name__ == '__main__':
    s = ConcreteSubject()

    s.attach(ConcreteObserver(s, "X"))
    s.attach(ConcreteObserver(s, "Y"))
    s.attach(ConcreteObserver(s, "Z"))

    s.status = "A"
    s.notify()

    s.status = "B"
    s.notify()

