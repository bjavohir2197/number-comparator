def solishtiruv_sonlar(a, b):
    if a > b:
        return f"{a} katta, {b} kichik"
    elif a < b:
        return f"{a} kichik, {b} katta"
    else:
        return f"{a} teng, {b} teng"

def solishtiruv_sonlar2(a, b):
    if a > b:
        return f"{a} katta, {b} kichik"
    elif a < b:
        return f"{a} kichik, {b} katta"
    else:
        return f"{a} teng, {b} teng"

print(solishtiruv_sonlar(10, 20))
print(solishtiruv_sonlar2(30, 30))
print(solishtiruv_sonlar(40, 30))
```

```python
def solishtiruv_sonlar(a, b):
    return f"{a} {('katta' if a > b else 'kichik' if a < b else 'teng')} {b}"

print(solishtiruv_sonlar(10, 20))
print(solishtiruv_sonlar(30, 30))
print(solishtiruv_sonlar(40, 30))
