def last_n_items(items, n):
    if n == 0:
        return []
    result = []
    for i in range(len(items) - n, len(items) + 1):
        result.append(items[i])
    return result

def main():
    data = [10, 20, 30, 40, 50]
    print(last_n_items(data, 3))
    print(last_n_items(data, 5))

if __name__ == "__main__":
    main()
