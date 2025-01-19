import random

class hill_climbing:
    def __init__(self, text_clause, deep_log = False):
        self.text_clause = text_clause
        self.state = {}
        self.sep_clause = []
        self.current_neighbors = []
        self.score = 0
        self.best_state = []
        self.deep_log = deep_log
        

    def parse_input_to_CNF(self):
        input_str = text_clause.upper()
        input_str = input_str.split('AND')
        
        for c in input_str:
            c = c.replace("(", "")
            c= c.replace(")", "")
            cs = c.split('OR') if "OR" in c else [c]
        
            li = []
            for var in cs:
                var_neg = False
                if "NOT" in var:
                    var_neg = True
                    var = var.replace('NOT', "")
                var = var.strip()
                self.state[var] = False
                li.append({'char': var, 'neg': var_neg })
            self.sep_clause.append(li)
        
        if self.deep_log: 
            print("Equation:", self.text_clause)
            print("Clause Model:")
            print( *self.sep_clause, sep=" & \n")
        
             
    def random_init_state(self):
        for var in list(self.state.keys()):
            self.state[var] = random.choice([True, False])

    def gen_state_neighbors(self):
        self.current_neighbors = []
        for i in range(len(self.state)):
            v1 = self.state.copy()
            keys = list(self.state.keys())
            v1[keys[i]] = not v1[keys[i]]
            self.current_neighbors.append({'state': v1})
            
        # state_score = self.score_of(self.state)
        # self.current_neighbors = list(filter(lambda x: x['score'] >= state_score , self.current_neighbors))
        
        if self.deep_log: print("\ncurrent variables", {"state":self.state , "score": self.score_of(self.state)}, sep="\n")
        if self.deep_log: print("\nGenerate neighbors", *self.current_neighbors, sep="\n")
   
    def score_of(self, variables, allow_log=False):
        if len(variables) == 0: return 0
        pos_count = 0    
        for clause in self.sep_clause:
            if self.deep_log and allow_log: print("\n\t(", " ∨ ".join([str("¬" if c['neg'] else "") + str(c['char']) for c in clause]), ")", end='\t=> evaluate FALSE')
            for v in clause:
                res = variables[v['char']] if not v['neg'] else not variables[v['char']]
                if res:
                    if self.deep_log and allow_log: print('\b\b\b\b\bTRUE ', end="")
                    pos_count += 1
                    break
        
        if self.deep_log and allow_log: print(f'\n\n▌ {pos_count} clause evaluated True.')
        return pos_count 

    def solution(self, state):
        return self.score_of(state, allow_log=True) == len(self.sep_clause)
        
    def there_exists_an_untried_operation_on_state(self):
        return len(self.current_neighbors) > 0
    
    def apply_next_valid_operation_on_state(self):
        return self.current_neighbors.pop(0)['state']
        
    def compare_states(self, state1, state2):
        return self.score_of(state1) > self.score_of(state2)
   
    def hill_climbing_satisfiability(self, limit):
        self.parse_input_to_CNF()
        self.random_init_state()
        self.gen_state_neighbors()

        self.hill_climbing(limit=limit)
  
    def hill_climbing(self, limit):
        if self.deep_log: print(f'apply operation on {self.state}')
        if self.solution(self.state):
            print("\n", "=" * 100, "\n","Solution Found\n\t▌ Variables:", self.state, "\n\t▌ Solution Found At Iteration:", 0)
            return

        iteration = 0
        while True:  
            while self.there_exists_an_untried_operation_on_state() and iteration <= limit:
                iteration += 1
                if self.deep_log: print(f'{"────" * 25}\niteration {iteration} result:')
                
                child_state = self.apply_next_valid_operation_on_state()
                if self.deep_log: print(f'apply operation on {child_state}')
                
                if self.solution(child_state):
                    print("\n", "=" * 100, "\n", "Solution Found","\n\t▌ Variables:", child_state, "\n\t▌ Solution Found At Iteration:", iteration)
                    return 
                elif self.compare_states(child_state, self.state):
                    if self.deep_log: print(f'\nchild score: {self.score_of(child_state)}\t better than current state({self.score_of(self.state)})')
                    
                    self.state = child_state
                    self.gen_state_neighbors()
                else: continue
            
            if iteration > limit: break
            
            if self.compare_states(self.state, self.best_state): 
                self.best_state = self.state.copy()
            
            # if stock in local minimum, randomly start from another point
            print("#" * 80, "\t\t Stock in local minimum, start from another point ...", "#" * 80, sep="\n")
            self.random_init_state()
            self.gen_state_neighbors()
        
        if len(self.best_state) == 0: self.best_state = self.state
        print("\n", "=" * 100, "\n",f"time limit expired({iteration - 1}) \n\t best state = {self.best_state}, score: {self.score_of(self.best_state)} \n\t last state = {self.state}, score: {self.score_of(self.state)}")


def print_info(): 
    print("\n\n================================ Ferdowsi University Of Mashhad(FUM) ================================")
    print("\t\t\t\t\t\t\t\tAdvance Design Of Algorithm")
    print("\t\t\t\t\t\t\t\tDr.Naghibzadeh")
    print("Students: \n\t- Mohsen Gholami Golkhatmi - 4032330028 \n\t- Behnam Akbari - 4031330022")


if __name__ == "__main__":

    text_clause = "(a OR b OR not u) AND (not a OR u) AND (b OR u) AND (u OR not g) AND (c OR not g) AND (not u OR not c OR g) AND (a OR not e) AND (not b OR e) AND (not a OR b OR e) AND (v OR d OR not w) AND (not v OR w) AND (not d OR w) AND (e OR g OR not v) AND (not e OR v) AND (not g OR v)"
    
    # how to write input: 
    #   inputs are case-insensitive and clause split by "AND". example: (A Or Not B) And (not A Or C)
    #   you can use parenthesis for clauses. example: (a or b) and (not a or c)
    #   literals are case-insensitive too, you can use A or a
    
    # input examples - all possible
    # text_clause = "a or not b and b"
    # text_clause = "(a or not b) and (b)"
    # text_clause = "a OR NOT b AnD (b)"
    # text_clause = "(A or not B or C) and (not A or C) and (not C or A)"

    # todo: if you need to get input in command line uncomment bellow line
    # text_clause = input("Please enter SAT in CNF(not A OR B OR C) AND (A OR not B OR D):\n")
    
    deep_log = True
    hill_climbing_limit = 50

    hill_climbing = hill_climbing(text_clause=text_clause, deep_log=deep_log)
    hill_climbing.hill_climbing_satisfiability(limit=hill_climbing_limit)

    print_info()

# =================================================
# Ferdowsi University Of Mashhad(FUM)
# Advance Design Of Algorithms - Project
# Prof.Naghibzadeh

# Mohsen Gholami Golkhatmi - 4032330028
# Behnam Akbari - 4031330022
# =================================================