import statistics

def summarize_data(data):
    mean_val = statistics.mean(data)
    median_val = statistics.median(data)
    stdev_val = statistics.stdev(data)
    print(f"Mean:   {mean_val:.2f}")
    print(f"Median: {median_val:.2f}")
    print(f"StdDev: {stdev_val:.2f}")

def main():
    raw_data = ["12", "45", "7", "33", "21", "19", "50", "8"]
    summarize_data(raw_data)

if __name__ == "__main__":
    main()
