## Dataset Inspector

指定したディレクトリを再帰的に調査し、以下の情報を表示します。

- ファイル総数
- 合計ファイルサイズ
- 拡張子別ファイル数
- 最大ファイル

### 実行方法

```bash
uv run dataset-inspector ./sample_data
```

### JSON形式で表示

```bash
uv run dataset-inspector ./sample_data --json
```

### 詳細ログの表示

処理の詳細や実行時間を確認する場合は、`--verbose`を指定します。

```bash
uv run dataset-inspector ./sample_data --verbose
```

### テスト

```bash
uv run pytest
```

### コード品質チェック
```bash
uv run ruff check .
uv run ruff format --check .
```

