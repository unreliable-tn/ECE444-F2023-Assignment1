from typing import Union


class utils:
    def __init__(self, int_in):
        self.int_in = int_in

    def reversed(self):
        if type(self.int_in) != int:
            raise TypeError

        input_num = self.int_in
        rev = 0

        while input_num != 0:
            digit = input_num % 10

            rev = 10 * rev
            rev = rev + digit

            input_num = input_num // 10

        return rev

    def formatter(self):
        if type(self.int_in) != int:
            raise TypeError

        return [bin(self.int_in), oct(self.int_in)]
