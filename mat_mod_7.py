
def solve_diophantine_equation():
    solutions = []
    for a in range(1, 31):
        for b in range(1, 16):
            for c in range(1, 11):
                for d in range(1, 8):
                    if a + 2 * b + 3 * c + 4 * d == 30:
                        solutions.append((a, b, c, d))
    return solutions


solutions = solve_diophantine_equation()
print("Решения диофантова уравнения a + 2b + 3c + 4d = 30, где a, b, c, d - целые положительные числа:")
for solution in solutions:
    print(solution)
print(len(solutions))
