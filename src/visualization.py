
import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column, title=None, save_path=None):
    """Plots a histogram with KDE."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(title or f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def plot_boxplot(df, x, y, title=None, save_path=None):
    """Plots a boxplot."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x, y=y)
    plt.title(title or f'{y} by {x}')
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def plot_scatter(df, x, y, hue=None, title=None, save_path=None):
    """Plots a scatter plot."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y, hue=hue, alpha=0.6)
    plt.title(title or f'{y} vs {x}')
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def plot_correlation_matrix(df, columns=None, save_path=None):
    """Plots a correlation heatmap."""
    if columns:
        corr_matrix = df[columns].corr()
    else:
        corr_matrix = df.select_dtypes(include=['number']).corr()
        
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()
