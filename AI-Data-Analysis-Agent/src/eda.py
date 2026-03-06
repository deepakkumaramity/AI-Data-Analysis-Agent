
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True)
    plt.title("Correlation Heatmap")
    plt.show()

def sales_by_region(df):
    df.groupby("Region")["Sales"].sum().plot(kind="bar")
    plt.title("Sales by Region")
    plt.show()
