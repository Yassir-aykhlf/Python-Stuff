"""
This module provides a context manager that
creates a temporary directory and deletes it
and its contents upon exit.
"""

import os
import contextlib
from typing import Generator

# postorder traversal to delete directory and its contents recursively
def dfs_delete(path: str) -> None:
    """delete directory and its contents recursively"""
    if os.path.isdir(path):
        for file in os.listdir(path):
            dfs_delete(os.path.join(path, file))
        os.rmdir(path)
    else:
        os.remove(path)

@contextlib.contextmanager
def temp_directory(path: str | None = None) -> Generator[str, None, None]:
    """create temporary directory and deletes it"""
    dir_path = path if path else f"./tmp_dir_{os.getpid()}"
    os.mkdir(dir_path)
    try:
        yield dir_path
    finally:
        # shutil.rmtree(dir_path)
        dfs_delete(dir_path)

with temp_directory() as temp_dir:
    file_path = os.path.join(temp_dir, "test.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Hello, World!")
