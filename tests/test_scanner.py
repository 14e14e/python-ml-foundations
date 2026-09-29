from pathlib import Path

from python_ml_foundations.dataset_inspector.scanner import (
    find_largest_file,
    get_extension_counts,
    get_total_size,
    scan_files,
)


def test_scan_files(tmp_path: Path) -> None:
    (tmp_path / "a.txt").write_text("hello")
    (tmp_path / "b.jpg").write_text("image")

    files = scan_files(tmp_path)

    assert len(files) == 2


def test_get_extension_counts(tmp_path: Path) -> None:
    files = [
        tmp_path / "a.jpg",
        tmp_path / "b.JPG",
        tmp_path / "c.txt",
    ]

    counts = get_extension_counts(files)

    assert counts == {
        ".jpg": 2,
        ".txt": 1,
    }


def test_get_total_size(tmp_path: Path) -> None:
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"

    file1.write_bytes(b"12345")
    file2.write_bytes(b"123")

    files = [file1, file2]

    assert get_total_size(files) == 8


def test_find_largest_file(tmp_path: Path) -> None:
    small_file = tmp_path / "small.txt"
    large_file = tmp_path / "large.txt"

    small_file.write_bytes(b"1")
    large_file.write_bytes(b"123456789")

    largest = find_largest_file([small_file, large_file])

    assert largest == large_file


def test_find_largest_file_when_empty() -> None:
    assert find_largest_file([]) is None
