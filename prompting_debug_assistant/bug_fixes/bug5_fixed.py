import statistics

def summarize_data(data):
    data = [int(x) for x in data]
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)
    if len(data) > 1:
        stdev_val = statistics.stdev(data)
    else:
        stdev_val = 0
    print(f"Mean: {mean_val:.2f}")
    print(f"Median: {median_val:.2f}")
    print(f"StdDev: {stdev_val:.2f}")

def main():
    raw_data = ["12", "45", "7", "33", "21", "19", "50", "8"]
    summarize_data(raw_data)

if __name__ == "__main__":
    main()
