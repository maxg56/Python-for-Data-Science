from load_csv import load


def main():
    """
    Test the load_csv function by loading a sample CSV file
        and printing its contents.
    """
    try:
        df = load("life_expectancy_years.csv")
        print(df)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
