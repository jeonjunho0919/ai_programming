
import pytest  # type: ignore[import-not-found]
from load_scores import load_scores

def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5

# def test_일부러_틀린_테스트():
#     kept, skipped = load_scores("scores.csv")
#     assert len(kept) == 99

def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")

def test_헤더만_있으면_빈_결과가_나온다():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []

@pytest.mark.parametrize("점수, 유효한가", [
    (-1,  False),   # 경계바로아래
    (0,   True),    # ★아래쪽경계
    (1,   True),
    (99,  True),
    (100, True),    # ★위쪽경계
    (101, False),   # 경계바로위
])

def test_점수_경계값(점수, 유효한가, tmp_path):
    임시_파일 = tmp_path / "임시.csv"
    임시_파일.write_text(f"name,score\nStudent,{점수}\n", encoding="utf-8")
    kept, _ = load_scores(str(임시_파일))
    assert (len(kept) == 1) == 유효한가

def test_빈_줄은_건너뛴다():
    kept, skipped = load_scores("scores.csv")
    # 빈 줄 때문에 멈추거나 죽지 않고, 그 뒤 줄까지 읽어야 한다
    assert ("윤보람", 64) in kept
    assert ("서한별", 95) in kept


def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    # 이름이 "최" 와 "네번"으로 쪼개지면 안 된다
    assert ("최,네번", 77) in kept