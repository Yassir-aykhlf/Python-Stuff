"""Module demonstrating context manager usage with ExitStack for managing multiple file handles."""

import contextlib

files: list[str] = ["file1.txt", "file2.txt", "file3.txt"]

with contextlib.ExitStack() as stack:
    open_files = [stack.enter_context(open(file, "w", encoding="utf-8")) for file in files]
    for f in open_files:
        f.write("Hello, World!\n")
