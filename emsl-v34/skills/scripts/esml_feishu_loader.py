#!/usr/bin/env python3
"""ESML Feishu/Sheets Loader — reads MCP sheet tabs into DuckDB tables."""
# Copyright (c) 2026 [YOUR LEGAL ENTITY]
# Licensed under the Apache License, Version 2.0
# This file is an original work and is NOT derived from
# the Open Semantic Interchange (OSI) specification.
#
# Knowledge sources:
# - DuckDB in-process SQL engine (duckdb.org, MIT license, public)
# - Feishu/Lark Open API documentation (open.feishu.cn, public)
# - ETL-to-memory patterns (pandas documentation, BSD license, public)
# - CSV parsing (Python standard library, PSF license, public)
#
# This file contains NO proprietary information from any employer or client.

import json
import sys

try:
    import duckdb
except ImportError:
    print("pip install duckdb", file=sys.stderr)
    sys.exit(1)


class FeishuLoader:
    """Load spreadsheet data into in-process DuckDB for ESML demo queries."""

    def __init__(self, db_path=":memory:"):
        self.conn = duckdb.connect(db_path)
        self.tables_loaded = []

    def load_from_mcp(self, mcp_client, spreadsheet_id: str):
        """Read all sheet tabs via Feishu/Sheets MCP and create DuckDB tables."""
        sheets = mcp_client.call("list_sheets", {"spreadsheet_id": spreadsheet_id})
        for sheet in sheets:
            name = sheet["title"].lower().replace(" ", "_")
            rows = mcp_client.call("read_sheet", {
                "spreadsheet_id": spreadsheet_id,
                "sheet_name": sheet["title"]
            })
            if not rows:
                continue
            headers = rows[0]
            data = rows[1:]
            col_defs = ", ".join(f'"{h}" VARCHAR' for h in headers)
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {name} ({col_defs})")
            for row in data:
                placeholders = ", ".join(["?"] * len(row))
                self.conn.execute(f"INSERT INTO {name} VALUES ({placeholders})", row)
            self.tables_loaded.append(name)
        return self.tables_loaded

    def load_from_csv(self, csv_dir: str):
        """Fallback: load CSV files from a directory."""
        import os
        import csv as csv_mod
        for fname in os.listdir(csv_dir):
            if not fname.endswith(".csv"):
                continue
            table_name = fname[:-4]
            with open(os.path.join(csv_dir, fname)) as f:
                reader = csv_mod.DictReader(f)
                rows = list(reader)
            if not rows:
                continue
            cols = list(rows[0].keys())
            col_defs = ", ".join(f'"{c}" VARCHAR' for c in cols)
            self.conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({col_defs})")
            for row in rows:
                vals = [row[c] for c in cols]
                placeholders = ", ".join(["?"] * len(vals))
                self.conn.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", vals)
            self.tables_loaded.append(table_name)
        return self.tables_loaded

    def execute(self, sql: str):
        """Execute SQL and return results as list of dicts."""
        result = self.conn.execute(sql)
        cols = [d[0] for d in result.description]
        return [dict(zip(cols, row)) for row in result.fetchall()]


if __name__ == "__main__":
    loader = FeishuLoader()
    if len(sys.argv) > 1:
        tables = loader.load_from_csv(sys.argv[1])
        print(json.dumps({"status": "ok", "tables": tables}, indent=2))
    else:
        print(json.dumps({"status": "no_input", "usage": "python esml_feishu_loader.py <csv_dir>"}))
