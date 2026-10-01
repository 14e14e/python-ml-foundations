from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class OutputFormat(str, Enum):
    """データセット調査結果の出力形式を表します。"""

    TEXT = "text"
    JSON = "json"


@dataclass(frozen=True)
class AppConfig:
    """dataset-inspectorの実行設定を保持します。"""

    directory: Path
    output_format: OutputFormat
    verbose: bool
