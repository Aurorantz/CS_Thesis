from itertools import combinations

EPSILON = ''

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states, current_state):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = current_state
        self.Type = 'DFA'

    def transition_to_state_with_input(self, input_value):
        if((self.current_state, input_value) in self.transition_function.keys()):
            self.current_state = self.transition_function[(self.current_state, input_value)]
            return
        self.current_state = None

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list):
        print(self.__dict__)
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
        return self.in_accept_state()

    def __normalize(self):
        normalized_state = [self.start_state]
        normalized_transition_function = {}
        normalized_accept_state = []

        for state in normalized_state:
            for alphabet in self.alphabet:
                key = (state, alphabet)
                tf_key = self.transition_function.get(key)
                if tf_key:
                    next_key = (tf_key, alphabet)
                    if next_key in self.transition_function.keys() or tf_key in self.accept_states:
                        normalized_transition_function[key] = tf_key
                        if tf_key not in normalized_state:
                            normalized_state.append(tf_key)

        self.states = sorted(normalized_state)
        self.transition_function = normalized_transition_function
        for acc_state in self.states:
            if acc_state in self.accept_states:
                normalized_accept_state.append(acc_state)

        self.accept_states = normalized_accept_state
        self.Type = 'Normalized DFA'

    def __simplify(self):
        self.__normalize()
        new_state_index = 65
        new_state_map = {}
        simp_DFA = DFA([], self.alphabet.copy(), {}, None, [], None)

        for state in self.states:
            new_state_map[state] = chr(new_state_index)
            simp_DFA.states.append(new_state_map[state])
            new_state_index += 1

        for state in self.accept_states:
            simp_DFA.accept_states.append(new_state_map[state])

        for state in self.states:
            for alphabet in self.alphabet:
                if (state, alphabet) in self.transition_function.keys():
                    simp_DFA.transition_function[(new_state_map[state], alphabet)] = new_state_map[self.transition_function[(state, alphabet)]]

        simp_DFA.start_state = new_state_map[self.start_state]
        simp_DFA.current_state = new_state_map[self.start_state]
        simp_DFA.Type = 'Simplified DFA'
        return simp_DFA

    def convert_to_RG(self):
        print(self.__dict__)
        new_RG = RG([], list(self.alphabet.copy()), self.start_state, {})
        temp_alphabet = self.alphabet.copy()
        temp_alphabet.append(EPSILON)

        for state in self.states:
            if (state not in new_RG.variables and 
                (set(new_RG.terminal_symbols) & set(state)) == set() and 
                state != EPSILON): 
                new_RG.variables.append(state)

        for state in new_RG.variables:
            if state in self.accept_states:         
                new_RG.production_rules[state] = [(EPSILON)]
            for alphabet in temp_alphabet:
                if (state, alphabet) in self.transition_function.keys():
                    if state not in new_RG.production_rules.keys():
                        new_RG.production_rules[state] = [(alphabet + self.transition_function[(state, alphabet)]).strip(EPSILON)]
                    else:
                        new_RG.production_rules[state].append((alphabet + self.transition_function[(state, alphabet)]).strip(EPSILON))

        if new_RG.start_symbol in self.accept_states:
            new_RG.production_rules['Start'] = [new_RG.start_symbol, EPSILON]
            new_RG.start_symbol = 'Start'

        new_RG.Type = new_RG.check_type()

        return new_RG.to_dict()

class NFA(DFA):
    def __init__(self, states, alphabet, transition_function, start_state, accept_states, current_state):
        super().__init__(states, alphabet, transition_function, start_state, accept_states, current_state)
        self.Type = 'NFA'

    def transition_to_state_with_input(self, input_value):
        new_state = set()
        for i in self.current_state:
            if (i, input_value) in self.transition_function.keys():
                new_state.update(self.transition_function[(i, input_value)])
        self.current_state = new_state.copy()

    def in_accept_state(self):
        return any(i in self.accept_states for i in self.current_state)

    def go_to_initial_state(self):
        self.current_state = {self.start_state}

    def convert_to_DFA(self):
        new_DFA = DFA([], list(self.alphabet.copy()), {}, self.start_state, [], '[' + ','.join(sorted(self.start_state)) + ']')
        subset = set()
        new_state_set = []

        for n in range(len(self.states) + 1):
            subset |= set(combinations(self.states, n))

        for sub in subset:
            new_state_set.append(sorted(sub))

        new_state_set = sorted(new_state_set)

        for state_set in new_state_set:
            new_DFA.states.append('[' + ','.join(state_set) + ']')
            if set(state_set) & set(self.accept_states) != set():
                new_DFA.accept_states.append('[' + ','.join(state_set) + ']')

        for state_set in new_state_set:
            for alphabet in new_DFA.alphabet:
                transition = set()
                for state in state_set:
                    if (state, alphabet) in self.transition_function.keys():
                        transition |= set(self.transition_function[(state, alphabet)])
                if transition:
                    new_DFA.transition_function[('[' + ','.join(state_set) + ']', alphabet)] = '[' + ','.join(sorted(transition)) + ']'

        return new_DFA

    def convert_to_RG(self):
        tempDFA = self.convert_to_DFA()
        return tempDFA.convert_to_RG()

class NFA_epsilon(NFA):
    def __init__(self, states, alphabet, transition_function, start_state, accept_states, current_state):
        super().__init__(states, alphabet, transition_function, start_state, accept_states, current_state)
        self.Type = 'NFA_epsilon'

    def epsilon_closure(self, state):
        epsilon_closure = {state}
        for ecs in list(epsilon_closure):
            if (ecs, EPSILON) in self.transition_function.keys():
                epsilon_closure.update(self.transition_function[(ecs, EPSILON)])
        return epsilon_closure

    def in_accept_state(self):
        return any(j in self.accept_states for i in self.current_state for j in self.epsilon_closure(i))

    def transition_to_state_with_input(self, input_value):
        current_epsilon_closure = set()
        for i in self.current_state:
            current_epsilon_closure |= self.epsilon_closure(i)
        new_state = set()
        for i in current_epsilon_closure:
            if (i, input_value) in self.transition_function.keys():
                new_state.update(self.transition_function[(i, input_value)])
        self.current_state = new_state.copy()

    def convert_to_NFA(self):
        if self.Type != 'NFA_epsilon':
            return self
        
        new_NFA = NFA(self.states.copy(), self.alphabet.copy(), {}, self.epsilon_closure(self.start_state), self.accept_states.copy(), self.epsilon_closure(self.start_state))
        if self.epsilon_closure(self.start_state) & set(self.accept_states) != set():
            new_NFA.accept_states.append(self.start_state)

        for state in self.states:
            for alphabet in self.alphabet:
                NFA_TF = (state, alphabet)
                Transition_output = set()
                Closure_transition = set()
                for closure in self.epsilon_closure(state):
                    if (closure, alphabet) in self.transition_function.keys():
                        Closure_transition |= set(self.transition_function[(closure, alphabet)])
                for closure_trans in Closure_transition:
                    Transition_output |= self.epsilon_closure(closure_trans)
                if Transition_output:
                    new_NFA.transition_function[NFA_TF] = Transition_output.copy()
        
        return new_NFA

    def convert_to_DFA(self):
        return self.convert_to_NFA().convert_to_DFA()

    def convert_to_RG(self):
        temp = self.convert_to_NFA()
        temp = temp.convert_to_DFA()
        return temp.convert_to_RG()

class RG:
    def __init__(self, variables, terminal_symbols, start_symbol, production_rules):
        self.variables = variables
        self.terminal_symbols = terminal_symbols
        self.start_symbol = start_symbol
        self.production_rules = production_rules
        self.Type = self.check_type()

    def check_type(self):
        isRl_R = True
        isLl_R = True
        for var in self.production_rules.keys():
            for prod in self.production_rules[var]:
                for i in range(len(prod) - 1):
                    if prod[i] in self.production_rules.keys() and prod[i + 1] in self.terminal_symbols:
                        isRl_R = False
                    if prod[i + 1] in self.production_rules.keys() and prod[i] in self.terminal_symbols:
                        isLl_R = False

        if isRl_R and isLl_R:
            return "Regular Grammar"
        if isRl_R and not isLl_R:
            return "Right Regular Grammar"
        if not isRl_R and isLl_R:
            return "Left Regular Grammar"
        return "Context-Free Grammar"

    def to_dict(self):
        """Convert RG object to a serializable dictionary."""
        return {
            "variables": self.variables,
            "terminal_symbols": self.terminal_symbols,
            "start_symbol": self.start_symbol,
            "production_rules": self.production_rules,
            "Type": self.check_type()
        }