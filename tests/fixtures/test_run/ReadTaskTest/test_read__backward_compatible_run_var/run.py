from rcmt import Run
from rcmt.action import Own

with Run("unit-test") as run:
    run.add_action(Own(content="test", target="test.txt"))
