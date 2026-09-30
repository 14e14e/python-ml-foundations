from pathlib import Path

from python_ml_foundations.dataset_inspector.models import DatasetSummary
from python_ml_foundations.dataset_inspector.scanner import (
    find_largest_file,
    get_extension_counts,
    get_total_size,
    scan_files,
)


def inspect_dataset(directory: Path) -> DatasetSummary:
    """指定されたディレクトリを調査し、データセットの概要情報を返します。"""
    files = scan_files(directory)

    return DatasetSummary(
        total_files=len(files),
        total_size_bytes=get_total_size(files),
        extension_counts=get_extension_counts(files),
        largest_file=find_largest_file(files),
    )
