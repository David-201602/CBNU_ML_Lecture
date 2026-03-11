import numpy as np
import pandas as pd
from pathlib import Path


def load_housing_data():
    base_path = Path(__file__).parent
    csv_path = base_path / "datasets" / "housing.csv"
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    # 1. Load Data
    housing = load_housing_data()

    # 2. Preprocessing: Handle Missing Values (Required before scaling)
    median = housing["total_bedrooms"].median()
    housing["total_bedrooms"] = housing["total_bedrooms"].fillna(median)

    # 3. Step 4: Check original statistics before scaling
    print("\nStep 4: Check original statistics before scaling")
    print("-" * 50)
    # Select only numeric features (Drop 'ocean_proximity' for scaling)
    num_housing = housing.drop(labels="ocean_proximity", axis=1)
    print(num_housing.describe())

    # 4. Step 5: Scaling & Normalization
    # Standardization: (x - mean) / std
    housing_std = (num_housing - num_housing.mean()) / num_housing.std()

    # Normalization: (x - min) / (max - min)
    housing_minmax = (num_housing - num_housing.min()) / (
        num_housing.max() - num_housing.min()
    )

    # Use NumPy arrays to keep the slide-style indexing below.
    housing_std = housing_std.to_numpy(dtype=np.float64)
    housing_minmax = housing_minmax.to_numpy(dtype=np.float64)

    print("\nStep 5: Compare results of Scaling (median_income column)")
    print("-" * 50)
    # median_income is at index 7
    print(f"Original value: {num_housing['median_income'].iloc[0]}")
    print(f"Standardized result: {housing_std[0, 7]:.4f}")
    print(f"Normalized result: {housing_minmax[0, 7]:.4f}")

    # 5. Step 6: Min/Max verification
    print("\nStep 6: Min/Max values after Normalization")
    print("-" * 50)
    print(f"Min value (All features): {housing_minmax.min()}")
    print(f"Max value (All features): {housing_minmax.max()}")
