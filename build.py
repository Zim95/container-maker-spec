# builtins
import os


PACKAGE_DIR: str = "container_maker_spec/"
PROTO_PATH: str = "spec/"


SPEC_BUILD_COMMAND: str = (
    f"python -m grpc_tools.protoc"
    f" --proto_path={PROTO_PATH} "
    f" --python_out={PACKAGE_DIR} "
    f" --grpc_python_out={PACKAGE_DIR} "
    f"{PROTO_PATH}*.proto"
)


def build(command: str) -> None:
    try:
        os.system(command)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    build(SPEC_BUILD_COMMAND)
