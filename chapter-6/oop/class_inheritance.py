class Engine:
    def start(self):
        pass
    def stop(self):
        pass

class ElectricEngine(Engine): #Is-A relationship
    pass

class V8Engine(Engine):  #Is-A relationship
    pass

class Car:
    engine_cls = Engine
    def __init__(self) -> None:
        self.engine = self.engine_cls() # Has-A relationship

    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom!'
            .format(
                    self.engine.__class__.__name__,
                    self.__class__.__name__
            )
        )
        self.engine.start()

    def stop(self):
        self.engine.stop()

class RaceCar(Car): # Is-A Car relationship
    engine_cls = V8Engine

class CityCar(Car): # Is-A Car relationship
    engine_cls = ElectricEngine

class F1Car(RaceCar): # Is-A RaceCar relationship Is-A Car
    pass


car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [car, racecar, citycar, f1car] 
for car in cars:
    car.start()