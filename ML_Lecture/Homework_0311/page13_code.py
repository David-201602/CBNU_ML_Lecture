import pandas as pd
from pathlib import Path


def load_stock_data():
    # 현재 실행 중인 파이썬 파일 위치를 기준으로 stockdata.csv 탐색
    base_path = Path(__file__).parent
    csv_path = base_path / "stockdata.csv"

    # 절대 경로 방식이 필요하면 아래 주석을 해제 후 사용
    # csv_path = Path(r"C:\path\to\stockdata.csv")

    # 데이터 로드
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    # 1. 데이터 불러오기
    stock = load_stock_data()

    # 2. 데이터 확인 (상위 5개 행)
    print("---- Stock Data Head ----")
    print(stock.head())

    # 3. 데이터 요약 정보 확인
    print("\n--- Stock Data Info ---")
    print(stock.info())
