from load_csv import load
import matplotlib.pyplot as plt

YEAR_COLUMN = '1900'
NAN_CSV_PIB = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
NAN_CSV_LIFE = "life_expectancy_years.csv"

def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files. It focuses on data from
    the year 1900 and visualizes the correlation between GNP and life
    expectancy through a scatter plot.

    Create a new figure to visualize the scatter plot

    Generate a scatter plot with GNP on
    the x-axis and life expectancy on the y-axis
    """
    try:
        income_data = load(NAN_CSV_PIB)
        life_expectancy_data = load(NAN_CSV_LIFE)
    except ValueError as e:
        print("Error loading data:", e)
        return
    gnp_year = income_data[YEAR_COLUMN]
    life_expectancy_year = life_expectancy_data[YEAR_COLUMN]

    plt.figure(figsize=(10, 6))
    plt.scatter(gnp_year, life_expectancy_year)
    plt.title(f"Life expectancy vs Gross domestic product (Year {YEAR_COLUMN})")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy (Years)")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.savefig("output.png")
    plt.show()


if __name__ == "__main__":
    main()