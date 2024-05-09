# builtins
import os
import pathlib
import glob


# constants
PACKAGE_DIR: str = "container_maker_spec/"
PROTO_PATH: str = "spec/"
PACKAGE_NAME: str = "container_maker_spec"


SPEC_BUILD_COMMAND: str = (
    f"python -m grpc_tools.protoc"
    f" --proto_path={PROTO_PATH} "
    f" --python_out={PACKAGE_DIR} "
    f" --grpc_python_out={PACKAGE_DIR} "
    f"{PROTO_PATH}*.proto"
)


def execute_command(command: str) -> None:
    """
    Execute the linux command.
    
    Author: Namah Shrestha
    """
    try:
        os.system(command)
    except Exception as e:
        print(e)


def replace_import() -> None:
    """
    All imports will be made in service_pb2.py and service_pb2_grpc.py
    Find _pb2 imports, add PACKAGE_NAME.*_pb2 in the imports.

    Author: Namah Shrestha
    """
    file_paths: map = map(lambda x: pathlib.Path(x),
                     glob.glob(f'{PACKAGE_DIR}service_*.py', recursive=True))
    type_modules: list = [
        "types_pb2"
    ]
    for file in file_paths:
        text: str = file.read_text()
        for type_module in type_modules:
            text = text.replace(f'\nimport {type_module}',
                                f'\nimport {PACKAGE_NAME}.{type_module}')
        file.write_text(text)


def build() -> None:
    """
    > Execute the command
    > Replace the import

    Author: Namah Shrestha
    """
    execute_command(SPEC_BUILD_COMMAND)
    replace_import()


if __name__ == "__main__":
    build()
