import numpy as np
import pandas as pd
from pathlib import Path


def load_stock_data():
    base_path = Path(__file__).parent
    csv_path = base_path / "stockdata.csv"
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    # 1. Load Data
    stock = load_stock_data()
    base_path = Path(__file__).parent

    # 2. Preprocessing: Handle Missing Values (Required before scaling)
    numeric_columns = stock.select_dtypes(include="number").columns
    stock[numeric_columns] = stock[numeric_columns].fillna(
        stock[numeric_columns].median()
    )

    # 3. Step 4: Check original statistics before scaling
    print("\nStep 4: Check original statistics before scaling")
    print("-" * 50)
    # Select only numeric features (Drop 'Date' for scaling)
    num_stock = stock[numeric_columns]
    print(num_stock.describe())

    # 4. Step 5: Scaling & Normalization
    # Standardization: (x - mean) / std
    stock_std = (num_stock - num_stock.mean()) / num_stock.std()

    # Normalization: (x - min) / (max - min)
    stock_minmax = (num_stock - num_stock.min()) / (num_stock.max() - num_stock.min())

    # Use NumPy arrays to keep the slide-style indexing below.
    stock_std_array = stock_std.to_numpy(dtype=np.float64)
    stock_minmax_array = stock_minmax.to_numpy(dtype=np.float64)

    print("\nStep 5: Compare results of Scaling (MSFT column)")
    print("-" * 50)
    # MSFT is at index 0
    print(f"Original value: {num_stock['MSFT'].iloc[0]}")
    print(f"Standardized result: {stock_std_array[0, 0]:.4f}")
    print(f"Normalized result: {stock_minmax_array[0, 0]:.4f}")

    # 5. Step 6: Min/Max verification
    print("\nStep 6: Min/Max values after Normalization")
    print("-" * 50)
    print(f"Min value (All features): {stock_minmax_array.min()}")
    print(f"Max value (All features): {stock_minmax_array.max()}")

    # Save processed data
    stock_std_output = stock.copy()
    stock_minmax_output = stock.copy()
    stock_std_output[numeric_columns] = stock_std
    stock_minmax_output[numeric_columns] = stock_minmax

    stock_std_output.to_csv(base_path / "stockdata_standardized.csv", index=False)
    stock_minmax_output.to_csv(base_path / "stockdata_normalized.csv", index=False)

    print(f"\nSaved standardized data to: {base_path / 'stockdata_standardized.csv'}")
    print(f"Saved normalized data to: {base_path / 'stockdata_normalized.csv'}")
