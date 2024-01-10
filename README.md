# Pytest + Robot demo

Dependency: [`pytest-robotframework`](https://github.com/detachhead/pytest-robotframework)

Run the tests with Robot to get the report:
```bash
ROBOT_OPTIONS="--outputdir=out" pytest tests/test\ _mylib.py
```

Run it without Robot for best performance:
```bash
pytest -p no:robotframework tests/test\ _mylib.py
```
