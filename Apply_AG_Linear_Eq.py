import EGA
import Fitness_linear_eq as fle

### Variables for flexibility of the algorithm
# number of variables for one solution
n_vars = 2
# lenght of bits for each variable
len_v = 32
### Variables what EGA needs
# Number of generations
G = 1000
# Number of individuals
n = 50
# Crossing probability
Pc = 0.9
# Mutation probability
Pm = 0.05

population = EGA.ega(fle.fitness, 2, 32, G=1000, n=50, Pc=0.9, Pm=0.05)

print("Aproaches: ")
print("x= ", fle.bin2float(population[0][0]))
print("y= ", fle.bin2float(population[0][1]))
