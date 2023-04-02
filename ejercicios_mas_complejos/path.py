from pathlib import Path
Path('ejercicios_mas_complejos').mkdir(parents=True, exist_ok=True)
path = Path('ejercicios_mas_complejos')
p = path.with_name('path.py')
print(p)