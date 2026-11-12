# 성적관리프로그램 (load_scores)

## 무엇을 하나요 (What)
성적 CSV 파일을 읽어 유효한 `(이름, 점수)`만 골라내고, 건너뛴 줄은 줄 번호·원본·이유와 함께 기록합니다.

## 왜 만들었나요 (Why)
실제 성적 파일에는 빈칸, 0~100 범위 밖 점수, 글자로 된 점수, 열 개수가 틀린 줄, 이름이 같은 사람이 섞여 있습니다.
그냥 읽으면 프로그램이 죽거나 잘못된 점수가 조용히 통계에 섞입니다.
그래서 "죽지 않고, 무엇을 왜 버렸는지 알려 주는" 읽기 함수가 필요했습니다.
(동명이인일 수 있으므로 같은 이름은 지우지 않고 둘 다 남깁니다. 누구를 남길지는 쓰는 쪽이 정합니다.)

## 어떻게 쓰나요 (How)
Python 3 이 필요하고, 별도 설치할 패키지는 없습니다.

```bash
python load_scores.py scores.csv
```

코드에서 쓸 때:

```python
from load_scores import load_scores
kept, skipped = load_scores("scores.csv")
```

## 상황별 확인 (check.py)
없는 파일·정상·헤더만·지저분한 파일 네 상황에 함수를 돌려 결과를 눈으로 봅니다.

```bash
python check.py load_scores
```

## 어떻게 테스트하나요
```bash
pip install pytest pytest-cov
pytest
pytest --cov=load_scores --cov-report=term-missing
```

현재 11개 테스트가 모두 통과하고 커버리지는 76%입니다.
(안 지나간 줄은 `__main__` 실행부와 이름이 빈 줄 처리입니다.)

## 파일 구성
| 파일 | 역할 |
|---|---|
| `load_scores.py` | 성적 CSV를 읽는 `load_scores(path)` 함수 |
| `test_load_scores.py` | 정상·예외·경계값 테스트 (pytest) |
| `check.py` | 여러 상황(없는 파일, 헤더만, 지저분한 파일)에 함수를 돌려 보는 확인 스크립트 |
| `scores.csv` `empty.csv` `weird.csv` | 테스트와 실행에 쓰는 샘플 데이터 |
| `LICENSE` | MIT 라이선스 |

## 만든 사람
- 이름·학번: (직접 입력)
- AI 사용: 테스트·README 초안 작성과 커밋 정리에 Claude Code 를 사용했습니다. 명세와 케이스 설계는 직접 했습니다.
