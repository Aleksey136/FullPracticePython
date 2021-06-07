class C32:
    state: str

    def __init__(self):
        self.state = 'A'

    def patch(self):
        if self.state == 'A':
            self.state = 'B'
            return 0

        elif self.state == 'B':
            self.state = 'C'
            return 1

        elif self.state == 'D':
            self.state = 'E'
            return 3

        elif self.state == 'G':
            self.state = 'A'
            return 8

        elif self.state == 'E':
            self.state = 'B'
            return 6

        else:
            return

    def begin(self):
        if self.state == 'C':
            self.state = 'D'
            return 2

        elif self.state == 'E':
            self.state = 'F'
            return 5

        elif self.state == 'F':
            self.state = 'G'
            return 7

        elif self.state == 'G':
            self.state = 'D'
            return 9

        elif self.state == 'D':
            self.state = 'A'
            return 4

        else:
            return
