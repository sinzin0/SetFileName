from pathlib import Path

DIR = Path(r'.\crops\test')  # 바꿀 폴더 경로
# 2025로 시작하는 것만: files = sorted(DIR.glob('2025*'))
files = sorted([p for p in DIR.iterdir() if p.is_file()], key=lambda p: p.name.lower())

# 1차: 임시 이름
for i, p in enumerate(files, 1):
    p.rename(p.with_name(f"__tmp_{i}{p.suffix.lower()}"))

# 2차: 최종 이름 (1.jpg, 2.jpg, ...)
for i, p in enumerate(sorted(DIR.glob('__tmp_*'), key=lambda p: p.name.lower()), 1):
    p.rename(p.with_name(f"{i}{p.suffix.lower()}"))