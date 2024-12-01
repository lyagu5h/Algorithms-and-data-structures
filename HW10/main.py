def calculate_expectation_variance(data):

    expectation = sum(x * p for x, p in data)
    
    variance = sum(((x - expectation) ** 2) * p for x, p in data)
    
    return expectation, variance

def process_input():
    data = []
    n = int(input("Введите количество строк в таблице: "))
    print("Введите строки в формате: x p")
    for _ in range(n):
        x, p = map(float, input().split())
        data.append((x, p))
    return data


def main():    
    data = process_input()

    m_x, d_x = calculate_expectation_variance(data)
    
    print(f'M[X] = {m_x:.2f}, D[X] = {d_x:.2f}')
    return

main()

