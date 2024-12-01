def calculate_expectation_variance(data):
    """
    Рассчитывает математическое ожидание и дисперсию на основе данных.
    
    data: список кортежей (x, p), где x - значение случайной величины, p - вероятность.
    """
    expectation = sum(x * p for x, p in data)
    
    variance = sum(((x - expectation) ** 2) * p for x, p in data)
    
    return expectation, variance

def process_input(input_type="file", file_path=None):
    """
    Читает данные из файла или консоли, возвращает список кортежей (x, p).
    
    input_type: "file" для чтения из файла, "console" для ручного ввода.
    file_path: путь к файлу, если выбран режим "file".
    """
    data = []
    if input_type == "file" and file_path:
        with open(file_path, 'r') as f:
            for line in f:
                x, p = map(float, line.strip().split())
                data.append((x, p))
    elif input_type == "console":
        n = int(input("Введите количество строк в таблице: "))
        print("Введите строки в формате: x p")
        for _ in range(n):
            x, p = map(float, input().split())
            data.append((x, p))
    else:
        raise ValueError("Неподдерживаемый тип ввода.")
    return data


def main():
    print("Выберите способ ввода данных:")
    print("1. Считать данные из файла")
    print("2. Ввести данные вручную")
    print("3. Вывести примеры")
    choice = input().strip()
    
    if choice == "1":
        file_path = input("Введите путь к файлу: ").strip()
        try:
            data = process_input(input_type="file", file_path=file_path)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return
    elif choice == "2":
        data = process_input(input_type="console")
    elif choice == "3":
        data = [(-1, 0.2), (0, 0.1), (1, 0.3), (2, 0.4)]
        print('Вводные данные: \n -1 0.2 \n 0 0.1 \n 1 0.3 \n 2 0.4')
        m_x, d_x = calculate_expectation_variance(data)
    else:
        print("Некорректный выбор.")
        return
    
    print(f'M[X] = {m_x:.2f}, D[X] = {d_x:.2f}')
    return

main()

