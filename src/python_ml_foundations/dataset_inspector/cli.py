import argparse
from pathlib import Path

from python_ml_foundations.dataset_inspector.inspector import inspect_dataset
from python_ml_foundations.dataset_inspector.report import format_report


def validate_directory(value: str) -> Path:
    """CLIから渡された値が有効なディレクトリであることを確認します。"""
    directory = Path(value).expanduser()

    if not directory.exists():
        raise argparse.ArgumentTypeError(f"指定されたパスが存在しません: {directory}")

    if not directory.is_dir():
        raise argparse.ArgumentTypeError(
            f"指定されたパスはディレクトリではありません: {directory}"
        )

    return directory


def build_parser() -> argparse.ArgumentParser:
    """dataset-inspector用のコマンドライン引数パーサーを作成します。"""
    parser = argparse.ArgumentParser(
        prog="dataset-inspector",
        description="指定したディレクトリ内のデータセットを調査します。",
    )

    parser.add_argument(
        "directory",
        type=validate_directory,
        help="調査対象となるディレクトリを指定します。",
    )

    return parser


def main() -> None:
    """コマンドラインアプリケーションのメイン処理を実行します。"""
    parser = build_parser()
    args = parser.parse_args()

    summary = inspect_dataset(args.directory)
    report = format_report(
        summary,
        args.directory,
    )

    print(report)
