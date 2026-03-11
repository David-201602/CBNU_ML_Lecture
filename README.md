# CBNU_ML_Lecture

2026년 3월 11일 머신러닝 프로그래밍 수업 실습 내용을 정리한 저장소입니다.

현재 실습 파일은 `ML_Lecture/My_project_0311` 폴더 아래에 정리되어 있습니다.

## 폴더 구조

```text
CBNU_ML_Lecture/
├── README.md
└── ML_Lecture/
    └── My_project_0311/
        ├── datasets/
        │   ├── housing.csv
        │   ├── housing_train.csv
        │   ├── housing_valid.csv
        │   └── housing_test.csv
        ├── page13_code.py
        ├── page14_code.py
        ├── page16_code.py
        └── page19_code.py
```

## 실습 파일 설명

### `page13_code.py`
- `housing.csv` 파일을 불러옵니다.
- 데이터 상위 5개 행을 확인합니다.
- 데이터프레임의 기본 정보를 출력합니다.

### `page14_code.py`
- 결측치 개수를 확인합니다.
- `total_bedrooms` 컬럼의 결측치를 중앙값으로 채웁니다.
- 결측치 처리 결과를 다시 확인합니다.

### `page16_code.py`
- 수치형 데이터만 선택합니다.
- 표준화와 Min-Max 정규화를 수행합니다.
- `median_income` 컬럼을 기준으로 변환 결과를 비교합니다.

참고:
- 이 파일은 `scikit-learn` 없이도 실행되도록 `pandas`와 `numpy`만 사용하도록 작성했습니다.

### `page19_code.py`
- 전체 데이터를 학습/검증/테스트 세트로 6:2:2 비율로 분할합니다.
- 분할 결과를 출력합니다.
- 분할된 데이터를 CSV 파일로 저장합니다.

## 실행 방법

저장소 루트에서 아래처럼 실행하면 됩니다.

```bash
python3.14 ML_Lecture/My_project_0311/page13_code.py
python3.14 ML_Lecture/My_project_0311/page14_code.py
python3.14 ML_Lecture/My_project_0311/page16_code.py
python3.14 ML_Lecture/My_project_0311/page19_code.py
```

## 사용 라이브러리

- `pandas`
- `numpy`
- `pathlib`

## 비고

- 데이터 파일 경로는 각 파이썬 파일의 현재 위치를 기준으로 상대 경로로 처리했습니다.
- 따라서 폴더 구조를 유지하면 다른 환경에서도 같은 방식으로 실행할 수 있습니다.
