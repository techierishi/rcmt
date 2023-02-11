from rcmt import Run
from rcmt.action import Own

with Run("unit-test", enabled=False) as run:
    run.add_action(Own(content="This is a unit test", target="test.txt"))
