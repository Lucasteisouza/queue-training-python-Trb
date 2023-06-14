from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def is_empty(self):
        return self.__data == []

    def enqueue(self, value):
        self.__data.append(value)

    def peek(self):
        if not self.is_empty():
            return self.__data[0]
        return None

    def dequeue(self):
        if not self.is_empty():
            return self.__data.pop(0)
        return None

    def search(self, index):
        if index < 0 or index > len(self.__data) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        if not self.is_empty():
            return self.__data[index]
        return None
