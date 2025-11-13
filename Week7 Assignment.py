import panda as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

def main():
    print("Task 1: Load and Explore the Dataset\n")

    try:
        # Load Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

        # Display first 5 rows
        print("First 5 rows:")
        print(df.head(), "\n")

        # Data info
        print("Data Info:")
        print(df.info(), "\n")

        # Check for missing values
        print("Missing values in each column:")
        print(df.isnull().sum(), "\n")

        # Fill missing values (just in case)
        df.fillna(df.mean(), inplace=True)

    except Exception as e:
        print("Error loading dataset:", e)
        return

    # --------------------------
    # Task 2: Basic Data Analysis
    # --------------------------
    print("\nTask 2: Basic Data Analysis\n")

    # Summary statistics
    print("Summary statistics:")
    print(df.describe(), "\n")

    # Group by species
    grouped = df.groupby('species').mean()
    print("Mean values per species:")
    print(grouped, "\n")

    # Observations
    print("Observations:")
    print("- Setosa has the smallest petal length and width on average.")
    print("- Virginica has the largest sepal and petal measurements.\n")

    # --------------------------
    # Task 3: Data Visualization
    # --------------------------
    print("Task 3: Data Visualization\n")

    # 1. Line chart: petal length trend
    plt.figure(figsize=(6,4))
    plt.plot(df['petal length (cm)'], marker='o', linestyle='-')
    plt.title("Petal Length Trend")
    plt.xlabel("Sample Index")
    plt.ylabel("Petal Length (cm)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: average petal length per species
    plt.figure(figsize=(6,4))
    species = grouped.index
    petal_avg = grouped['petal length (cm)']
    plt.bar(species, petal_avg, color=['lightblue', 'lightgreen', 'lightcoral'])
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.tight_layout()
    plt.show()

    # 3. Histogram: sepal length distribution
    plt.figure(figsize=(6,4))
    plt.hist(df['sepal length (cm)'], bins=10, color='lightgray', edgecolor='black')
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot: sepal length vs petal length
    plt.figure(figsize=(6,4))
    colors = {'setosa':'red', 'versicolor':'blue', 'virginica':'green'}
    for sp in df['species'].unique():
        subset = df[df['species'] == sp]
        plt.scatter(subset['sepal length (cm)'], subset['petal length (cm)'],
                    label=sp, color=colors[sp])
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.show()


if _name_ == "_main_":
    main()