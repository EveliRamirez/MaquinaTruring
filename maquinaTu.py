class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)
        self.head = 0
        self.state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

    def step(self):
        if self.state in self.final_states:
            return False  # La máquina se detiene si alcanza un estado final
        tape_symbol = self.tape[self.head]
        key = (self.state, tape_symbol)
        if key in self.transition_function:
            value = self.transition_function[key]
            self.tape[self.head] = value[0]
            self.head += 1 if value[1] == 'R' else -1
            self.state = value[2]
        else:
            return False  # La máquina se detiene si no hay transición definida
        return True

    def run(self):
        while self.step():
            pass

# Configuración de la máquina
tape = '1101+1011='  # Cinta inicial
initial_state = 'q0'
final_states = {'qf'}
transition_function = {
    ('q0', '1'): ('1', 'R', 'q0'),
    ('q0', '0'): ('0', 'R', 'q0'),
    ('q0', '+'): ('+', 'R', 'q1'),
    ('q1', '1'): ('1', 'R', 'q1'),
    ('q1', '0'): ('0', 'R', 'q1'),
    ('q1', '='): ('=', 'L', 'q2'),
    ('q2', '1'): ('0', 'L', 'q3'),
    ('q2', '0'): ('1', 'R', 'qf'),
    ('q3', '1'): ('0', 'L', 'q3'),
    ('q3', '0'): ('1', 'R', 'q2')
}

tm = TuringMachine(tape, initial_state, final_states, transition_function)
tm.run()
print(''.join(tm.tape))
