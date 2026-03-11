import numpy as np
import pandas as pd
from pathlib import Path


def load_stock_data():
    base_path = Path(__file__).parent
    csv_path = base_path / "stockdata.csv"
    return pd.read_csv(csv_path)


def split_dataframe(dataframe, test_size, random_state):
    rng = np.random.default_rng(random_state)
    shuffled_indices = rng.permutation(len(dataframe))
    test_set_size = int(len(dataframe) * test_size)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    train_set = dataframe.iloc[train_indices].copy()
    test_set = dataframe.iloc[test_indices].copy()
    return train_set, test_set


if __name__ == "__main__":
    # 1. 데이터 로드
    stock = load_stock_data()
    base_path = Path(__file__).parent
    output_dir = base_path  # 저장할 폴더 위치

    # 2. 데이터 분할 (6:2:2)
    # [Step A] 전체 20%를 Test 세트로 분리
    train_valid_set, test_set = split_dataframe(stock, test_size=0.2, random_state=42)

    # [Step B] 남은 80% 중 25%를 Validation 세트로 분리 (전체의 20% 효과)
    train_set, valid_set = split_dataframe(
        train_valid_set, test_size=0.25, random_state=42
    )

    # 3. 분할 결과 출력 (검증)
    print("\nStep 9: Raw Data Splitting Results (6:2:2)")
    print("-" * 50)
    print(f"Total dataset:         {len(stock)} rows")
    print(f"Training set (60%):    {len(train_set)} rows")
    print(f"Validation set (20%):  {len(valid_set)} rows")
    print(f"Test set (20%):        {len(test_set)} rows")

    # 4. 따로 저장 (index=False 옵션으로 불필요한 행 번호 컬럼 저장 방지)
    train_set.to_csv(output_dir / "stock_train.csv", index=False)
    valid_set.to_csv(output_dir / "stock_valid.csv", index=False)
    test_set.to_csv(output_dir / "stock_test.csv", index=False)

    print("\nStep 10: Saving Files Complete")
    print("-" * 50)
    print(f"Files saved in: {output_dir}")
