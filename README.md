# 성적관리프로그램

성적 CSV 파일을 읽어서 쓸 수 있는 점수만 골라주는 파이썬 함수입니다.
못 쓰는 줄은 버리지만, 몇 번째 줄을 왜 버렸는지는 따로 남겨줍니다.

## 왜 만들었나
실제 성적 파일을 보면 점수가 비어 있거나, 105점처럼 범위를 벗어났거나, "결석"이라고 글자가 들어간 줄이 있습니다. 이런 파일을 그냥 읽으면 프로그램이 멈추거나, 틀린 점수가 모르는 사이에 섞여 들어갑니다. 그래서 읽다가 죽지 않고, 뭘 버렸는지 알려주는 함수를 만들었습니다.

같은 이름이 두 번 나오면 지우지 않고 둘 다 남깁니다. 동명이인일 수도 있어서, 누구를 남길지는 이 함수를 쓰는 쪽에서 정하게 했습니다.

## 실행
설치할 건 없고 파이썬 3만 있으면 됩니다.

```bash
python load_scores.py scores.csv
```

다른 코드에서 가져다 쓸 때는 이렇게 씁니다.

```python
from load_scores import load_scores
kept, skipped = load_scores("scores.csv")
```

`kept`는 `(이름, 점수)` 목록이고, `skipped`는 `(줄 번호, 원본 줄, 이유)` 목록입니다.

네 가지 상황(없는 파일, 정상 파일, 헤더만 있는 파일, 지저분한 파일)에서 어떻게 동작하는지 한 번에 보고 싶으면 아래처럼 실행합니다.

```bash
python check.py load_scores
```

## 테스트
```bash
pip install pytest pytest-cov
pytest
```

테스트는 11개이고 전부 통과합니다. 커버리지를 재면 76%입니다.

```bash
pytest --cov=load_scores --cov-report=term-missing
```

안 지나간 줄은 파일을 직접 실행할 때 쓰는 맨 아래 부분과, 이름이 빈 줄을 처리하는 부분입니다.

## 파일
- `load_scores.py` : CSV를 읽는 함수
- `test_load_scores.py` : 테스트 (정상, 없는 파일, 헤더만 있는 파일, 점수 경계값 -1·0·1·99·100·101, 빈 줄, 이름 속 쉼표)
- `check.py` : 네 가지 상황을 한 번에 돌려보는 스크립트
- `scores.csv`, `empty.csv`, `weird.csv` : 예시 데이터
- `LICENSE` : MIT

## 만든 사람
이름·학번: 전준호, 2026100719

테스트 초안과 이 README는 Claude Code의 도움을 받아 썼고, 어떤 경우를 테스트할지는 제가 정했습니다.
