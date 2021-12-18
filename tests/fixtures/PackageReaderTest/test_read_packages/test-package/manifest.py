from rcmt.package import Manifest
from rcmt.package.action import Seed

with Manifest(name="test-package") as manifest:
    manifest.add_action(Seed(target="test.yaml", source="test.yaml"))