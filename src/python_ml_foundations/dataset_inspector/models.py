from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict


class DatasetSummaryDict(TypedDict):
    """JSON出力可能なデータセット概要の構造を表します。"""

    total_files: int
    total_size_bytes: int
    total_size_mb: float
    extension_counts: dict[str, int]
    largest_file: str | None


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

    def to_dict(self) -> DatasetSummaryDict:
        """データセット概要をJSON変換可能な辞書として返します。"""
        return {
            "total_files": self.total_files,
            "total_size_bytes": self.total_size_bytes,
            "total_size_mb": self.total_size_mb,
            "extension_counts": self.extension_counts,
            "largest_file": (
                str(self.largest_file) if self.largest_file is not None else None
            ),
        }
