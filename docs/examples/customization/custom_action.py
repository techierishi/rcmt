import os.path

from rcmt.action import Action
from rcmt.task import Task


class HelloWorld(Action):
    """
    HelloWorld action creates the file "hello-world.txt" in the root of a repository.
    It writes "Hello World" to it.
    """

    def apply(self, repo_path: str, tpl_data: dict) -> None:
        file = os.path.join(repo_path, "hello-world.txt")
        with open(file, "w+") as f:
            f.write("Hello World")
            f.write("\n")


with Task(name="custom-action") as task:
    task.add_action(HelloWorld())
