def print_pages(num_pages):
    pages = list(range(1, num_pages + 1)) + [None] * (4 - num_pages % 4) if num_pages % 4 != 0 else []

    print(f"{'Лист':<10}{'Back':<10}{'Front':<10}")
    print("-" * 30)

    back_right = []
    back_left = []
    front_left = []
    front_right = []

    for k in range(1, len(pages) // 2 + 1, 2):
        back = f"{pages[-k] or ' '}|{pages[k-1] or ' '}"
        front = f"{pages[k] or ' '}|{pages[-(k+1)] or ' '}"
        
        if pages[k-1] is not None:
            back_right.append(pages[k-1])
        if pages[-k] is not None:
            back_left.append(pages[-k])
        if pages[k] is not None:
            front_left.append(pages[k])
        if pages[-(k+1)] is not None:
            front_right.append(pages[-(k+1)])

        print(f"{k//2 + 1:<10}{back:<10}{front:<10}")
    
    back_left.reverse()
    front_right.reverse()

    back_right_str = ','.join(str(p) for p in back_right if p is not None)
    back_left_str = ','.join(str(p) for p in back_left if p is not None)
    front_left_str = ','.join(str(p) for p in front_left if p is not None)
    front_right_str = ','.join(str(p) for p in front_right if p is not None)

    print(f"\nFront left: {front_left_str}\n"\
          f"Front right: {front_right_str}\n"\
          f"Back left: {back_left_str}\n"\
          f"Back right: {back_right_str}\n")
          

def print_sheets(num_sheets):
    pages = list(range(1, num_sheets * 4 + 1))

    print(f"{'Лист':<10}{'Back':<10}{'Front':<10}")
    print("-" * 30)

    back_right = []
    back_left = []
    front_left = []
    front_right = []

    for i in range(1, len(pages) // 2, 2):
        back = f"{pages[-i] or ' '}|{pages[i-1] or ' '}"
        front = f"{pages[i] or ' '}|{pages[-(i+1)] or ' '}"

        if pages[i-1] is not None:
            back_right.append(pages[i-1])
        if pages[-i] is not None:
            back_left.append(pages[-i])
        if pages[i] is not None:
            front_left.append(pages[i])
        if pages[-(i+1)] is not None:
            front_right.append(pages[-(i+1)])

        print(f"{i//2 + 1:<10}{back:<10}{front:<10}")
    
    back_left.reverse()
    front_right.reverse()

    back_right_str = ','.join(str(p) for p in back_right if p is not None)
    back_left_str = ','.join(str(p) for p in back_left if p is not None)
    front_left_str = ','.join(str(p) for p in front_left if p is not None)
    front_right_str = ','.join(str(p) for p in front_right if p is not None)

    print(f"\nFront left: {front_left_str}\n"\
          f"Front right: {front_right_str}\n"\
          f"Back left: {back_left_str}\n"\
          f"Back right: {back_right_str}\n")

def main():
    choice = input("'1' для ввода количества страниц\n'2' для ввода количества листов\nВведите: ").strip()

    if choice == '1':
        num_pages = int(input("Введите количество страниц: "))
        print_pages(num_pages)
    elif choice == '2':
        num_sheets = int(input("Введите количество листов: "))
        print_sheets(num_sheets)
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

# Запуск программы
if __name__ == "__main__":
    main()
