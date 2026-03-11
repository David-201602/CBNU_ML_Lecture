import pandas as pd
from pathlib import Path


def load_stock_data():
    base_path = Path(__file__).parent
    csv_path = base_path / "stockdata.csv"
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    # Load data
    stock = load_stock_data()
    base_path = Path(__file__).parent
    output_path = base_path / "stockdata_processed.csv"

    # Step 1: Initial check
    print("\nStep 1: Checking for missing values")
    print(stock.isnull().sum())

    # Step 2: Processing
    print("\nStep 2: Selecting Missing Data Strategy")

    # [Option 1] Drop rows with missing values
    # stock = stock.dropna(subset=["MSFT"])
    # print("Result: Dropped rows containing missing values.")

    # [Option 2] Drop the entire column
    # stock = stock.drop("MSFT", axis=1)
    # print("Result: Dropped the 'MSFT' column.")

    # [Option 3] Impute with median (Recommended)
    median = stock["MSFT"].median()
    stock["MSFT"] = stock["MSFT"].fillna(median)
    print(f"Result: Imputed missing values in MSFT with median ({median}).")

    # Step 3: Final verification
    print("\nStep 3: Verification after processing")
    print(stock.isnull().sum())

    # Save processed data
    stock.to_csv(output_path, index=False)
    print(f"\nSaved processed data to: {output_path}")
