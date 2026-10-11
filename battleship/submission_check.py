from pathlib import Path
import subprocess
import sys
if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    source = (root / 'game.py').read_text(encoding='utf-8')
    if 'raise NotImplementedError(' in source:
        print('NOT READY: game.py still contains an unfinished TODO. Find the first NotImplementedError and complete the TODO block directly above it.')
        print('НЕ ГОТОВО: в game.py остался незавершённый TODO. Найдите первый NotImplementedError и выполните блок TODO прямо над ним.')
        raise SystemExit(1)
    for filename in ('practice_checks.py', 'tests.py'):
        result = subprocess.run([sys.executable, str(root / filename)], cwd=root)
        if result.returncode:
            print('Repair the failing behavior before presenting. / Исправьте ошибку до защиты.')
            raise SystemExit(result.returncode)
    print('READY: all three TODOs and full regression tests pass. Be ready to explain why each TODO matters.')
