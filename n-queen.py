__author__ = 'Selim Docquir'
__wsuid__ = 'C798Y776'
__class__ = 'CS771 - Spring 2016 - Sinha'
__progassign__ = '2'

import random
import conflict3

class NQueen(object):

    def __init__(self, n_value, start_state):
        # start_state is in the form of the position of the queen for each column
        self.n = n_value
        self.positions = start_state
        self.iterations = 0

    def __str__(self):
        return_string = str()
        for i in range(self.n):
            row = ['o'] * self.n
            for col in range(self.n):
                if self.positions[col] == self.n - 1 - i:
                    row[col] = 'x'
            return_string += str(' '.join(row)) + '\n'
        return return_string

    def conflicts_at_pos(self, col, row):
        # returns the number of conflicts for the specified col and row
        conflicts = 0
        for i in range(self.n):
            if i == col:
                continue
            if (self.positions[i] == row or         # if there's another queen on the same row
                    abs(i - col) == abs(self.positions[i] - row)):  # or a diagonal adjacent queen
                conflicts += 1
        return conflicts

    def find_conflicts(self):
        col_conflicts = list()
        for col in range(self.n):
            col_conflicts.append(self.conflicts_at_pos(col, self.positions[col]))
        return col_conflicts

    def random_pos(self, col_list, filt):
        return random.choice([i for i in range(self.n) if filt(col_list[i])])

    def solve(self):
        while True:
            self.iterations += 1
            conflicts = self.find_conflicts()
            if sum(conflicts) == 0:
                break
            col = self.random_pos(conflicts, lambda foo: foo > 0)
            vert_conflicts = [self.conflicts_at_pos(col, row) for row in range(self.n)]
            self.positions[col] = self.random_pos(vert_conflicts, lambda foo: foo == min(vert_conflicts))


def prompt_for_state(n):
    available_numbers = range(n)
    print "---------------------------------"
    print "Possible values :", available_numbers
    start_list = list()
    for x in range(n):
        invalid_int_value = True
        while invalid_int_value:
            try:
                user_inp = int(raw_input('Queen Position for column {0} : '.format(x)))
                if user_inp in available_numbers:
                    invalid_int_value = False
                    start_list.append(user_inp)
                else:
                    print "That value is not available. Please try again."
            except ValueError:
                print 'You entered an incorrect value. Only integer value are accepted.'

    print "\nThe start state you selected is the following :"
    print start_list
    return start_list


def main():
    # Disclaimer with quick how to
    disclaimer = str()
    disclaimer += "This is a N-queen problem solver.\n"
    disclaimer += "First, let's choose a 'n' value. (n>=4)\n"
    print disclaimer

    print "This is a change added to CS580-work working directory"

    invalid_n_value = True
    n_value = int()
    while invalid_n_value:
        try:
            n_value = int(raw_input("Enter your n value: "))
            if n_value < 4:
                print "You entered a value lower than 4. Try again"
            else:
                invalid_n_value = False
        except ValueError:
            print 'You entered an incorrect value. Only integer values are accepted.'
            continue

    print "This is a change added to /CS580 working copy"


    print "You selected a n value of {0}.".format(n_value)
    print "Now, let's decide on a start state."
    print "Rows and colums are numbered from left to right, top to bottom, starting at 0."
    print "For each column, indicate which row you'd like the queen to start on."
    start_state = prompt_for_state(n_value)
    problem = NQueen(n_value, start_state)
    problem.solve()
    print "\nThe solution to this problem, found in {0} iterations,  is :\n".format(problem.iterations)
    print problem


if __name__ == "__main__":
    main()
