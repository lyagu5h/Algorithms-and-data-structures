import numpy as np

def solve_transportation_problem():
    # Запасы на складах
    supply = [100, 200]

    # Потребности магазинов
    demand = [50, 100, 75, 75]

    # Стоимость перевозки из складов в магазины
    cost_matrix = [
        [4, 3, 5, 6],  # Склад 1
        [8, 2, 4, 7]   # Склад 2
    ]

    supply_sum = sum(supply)
    demand_sum = sum(demand)

    if supply_sum > demand_sum:
        demand.append(supply_sum - demand_sum)
        for row in cost_matrix:
            row.append(0)
    elif supply_sum < demand_sum:
        supply.append(demand_sum - supply_sum)
        cost_matrix.append([0] * len(demand))

    cost_matrix = np.array(cost_matrix)

    n, m = len(supply), len(demand)
    allocation = np.zeros((n, m), dtype=int)

    i = j = 0
    while i < n and j < m:
        x = min(supply[i], demand[j])
        allocation[i, j] = x
        supply[i] -= x
        demand[j] -= x
        if supply[i] == 0:
            i += 1
        elif demand[j] == 0:
            j += 1

    total_cost = np.sum(allocation * cost_matrix)

    return allocation, total_cost

allocation, min_cost = solve_transportation_problem()

print("Распределение товара:")
print(allocation)
print("Минимальная стоимость перевозки:", min_cost)
