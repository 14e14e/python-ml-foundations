from dataclasses import dataclass
from pathlib import Path


@dataclass
class DatasetSummary:
    """データセットを調査した結果を保持するクラスです。"""

    total_files: int
    total_size_bytes: int
    extension_counts: dict[str, int]
    largest_file: Path | None

    @property
    def total_size_mb(self) -> float:
        """データセット全体のサイズをMB単位で返します。"""
        return self.total_size_bytes / (1024**2)
