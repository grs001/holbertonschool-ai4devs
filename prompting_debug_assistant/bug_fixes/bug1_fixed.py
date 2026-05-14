def last_n_items(items, n):
    if n <= 0:
        return []
    return items[-n:]

def main():
    data = [10, 20, 30, 40, 50]
    print(last_n_items(data, 3))
    print(last_n_items(data, 5))

if __name__ == "__main__":
    main()
