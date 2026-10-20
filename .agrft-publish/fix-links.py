from pathlib import Path
import hashlib
p = Path('content/en/teaching/agrft.md')
s = p.read_text(encoding='utf-8')
a = '](/assets/files/AGRFT_English_ucno_gradivo_v1.2.md)'
b = '](https://damjan-popic.github.io/assets/files/AGRFT_English_ucno_gradivo_v1.2.md)'
assert s.count(a) == 1
p.write_text(s.replace(a, b), encoding='utf-8', newline='\n')
digest = hashlib.sha256(p.read_bytes()).hexdigest()
assert digest == '02a8fc3cd187ba33b2662d6e314664e2696049bef0b2067a9d99e3c1717b3a86'
print('Verified website source after download-link normalisation:', digest)
