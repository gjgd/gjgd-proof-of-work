# GJGD proof of work

A simple python script to generate a proof of work for my Github's username.

## Usage

```bash
python mine.py
```

And wait until desired difficulty is reached.

## Result

Found proof of work "gjgd 10495463960" with 34 bits of difficulty.

To verify, run:

```python
import hashlib

print(hashlib.sha256(b"gjgd 10495463960").hexdigest())
# outputs  '00000000221eded872d7260ab228b4228460f621c925c811007c00a1c4df152e'
```
