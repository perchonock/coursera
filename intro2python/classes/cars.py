from os.path import splitext
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        ext = splitext(self.photo_file_name)[1]
        return ext


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = "car"


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self._body_whl = body_whl
        self.car_type = "truck"
        if body_whl == "":
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0
        else:
            params = [float(n) for n in body_whl.split('x')]

            self.body_length = params[0]
            self.body_width = params[1]
            self.body_height = params[2]

    # @property
    # def body_whl(self):
    #     print('im here!!!')
    #     if self._body_whl == "":
    #         #pass
    #         self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
    #     else:
    #         params = [float(n) for n in self.body_whl.split('x')]
    #         self.body_length, self.body_width, self.body_height = params[0], params[1], params[2]
    #     return self._body_whl


    # @property
    # def body_length(self):
    #     if self.body_whl == "":
    #         return 0.0
    #     else:
    #         params = [float(n) for n in self.body_whl.split('x')]
    #         return params[0]
    #
    # @property
    # def body_width(self):
    #     if self._body_whl == "":
    #         return 0.0
    #     else:
    #         params = [float(n) for n in self.body_whl.split('x')]
    #         return params[1]
    #
    # @property
    # def body_height(self):
    #     if self._body_whl == "":
    #         return 0.0
    #     else:
    #         params = [float(n) for n in self.body_whl.split('x')]
    #         return params[2]

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    with open(csv_filename) as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)

        car_list = []

        for row in reader:
            try:
                #print(row)
                type = row[0]
                brand = row[1]
                passenger_seats_count = row[2]
                photo = row[3]
                body = row[4]
                carrying = row[5]
                extra = row[6]

                if type == 'car':
                    obj = Car(brand, photo, carrying, int(passenger_seats_count))
                elif type == 'truck':
                    obj = Truck(brand, photo, carrying, body)
                elif type == 'spec_machine':
                    obj = SpecMachine(brand, photo, float(carrying), extra)

                car_list.append(obj)
                #print("i added", row)
            except:
                pass


    return car_list


#print(get_car_list("coursera_week3_cars.csv"))
#truck = Truck("brand", "photo.jpg", 4, "2x3x4")
#print(truck.__dict__)