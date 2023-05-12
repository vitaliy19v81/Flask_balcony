class Room:
    def __init__(self):
        self.house = [[0, 1, 0],
                      [2, 3, 4],
                      [5, 6, 7]]

        self.direction = {0: (-1, 0),  # (0, 'Север')
                          1: (0, 1),  # (1, 'Восток')
                          2: (1, 0),  # (2, 'Юг')
                          3: (0, -1)}  # (3, 'Запад')
        self.decode = {1: 'Балконе', 2: 'Спальне', 3: 'Холле', 4: 'Кухне', 5: 'Подземелье', 6: 'Коридоре',
                       7: 'Оружейной'}
        self.code = {'Балконе': 1, 'Спальне': 2, 'Холле': 3, 'Кухне': 4, 'Подземелье': 5, 'Коридоре': 6,
                     'Оружейной': 7}
        self.location = 'Подземелье'
        self.current_location_floor_index = 0
        self.current_location_room_index = 0
        self.wall = False

    def set_location(self):
        """Выставляем текущее расположение"""
        for floor_index in range(len(self.house)):
            for room_index in range(len(self.house[floor_index])):
                if self.house[floor_index][room_index] == self.code[self.location]:
                    self.current_location_floor_index = floor_index
                    self.current_location_room_index = room_index

    def movement(self, path: int = 0, step: int = 1):
        vertical, horizontal = self.direction[path]
        flag = True

        if vertical < 0:  # Движение на СЕВЕР
            while flag:
                if step == 0:
                    break
                if self.current_location_floor_index - 1 < 0:
                    flag = False
                    break
                if flag:
                    if self.house[self.current_location_floor_index - 1][self.current_location_room_index] == 0:
                        flag = False
                        break
                self.current_location_floor_index = self.current_location_floor_index - 1
                step = step - 1

        if vertical > 0:  # Движение на ЮГ
            while flag:
                if step == 0:
                    break
                if self.current_location_floor_index + 1 > len(self.house) - 1:
                    flag = False
                    break
                if flag:
                    if self.house[self.current_location_floor_index + 1][self.current_location_room_index] == 0:
                        flag = False
                        break
                self.current_location_floor_index = self.current_location_floor_index + 1
                step = step - 1

        if horizontal < 0:  # Движение на ЗАПАД
            while flag:
                if step == 0:
                    break
                if self.current_location_room_index - 1 < 0:
                    flag = False
                    break
                if flag:
                    if self.house[self.current_location_floor_index][self.current_location_room_index - 1] == 0:
                        flag = False
                        break
                self.current_location_room_index = self.current_location_room_index - 1
                step = step - 1

        if horizontal > 0:  # Движение на ВОСТОК
            while flag:
                if step == 0:
                    break
                if self.current_location_room_index + 1 > len(self.house[self.current_location_floor_index]) - 1:
                    flag = False
                    break
                if flag:
                    if self.house[self.current_location_floor_index][self.current_location_room_index + 1] == 0:
                        flag = False
                        break
                self.current_location_room_index = self.current_location_room_index + 1
                step = step - 1

        self.location = self.decode[self.house[self.current_location_floor_index][self.current_location_room_index]]
        self.wall = flag


