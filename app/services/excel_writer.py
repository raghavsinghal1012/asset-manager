from pathlib import Path
import json

import pandas as pd


class ExcelWriter:

    def __init__(self, base_url: str):

        self.base_url = base_url.rstrip("/")

    def build_url(self, asset):

        return (
            f"{self.base_url}"
            f"/assets/"
            f"{asset.company}/"
            f"{asset.excel_slug}/"
            f"{asset.sheet_slug}/"
            f"{asset.uuid}"
        )

    def create_mapping_excel(
        self,
        assets,
        output_file: Path
    ):

        rows = []

        for asset in assets:

            rows.append({

                "UUID": asset.uuid,

                "QR URL": self.build_url(asset),

                "Excel File": asset.excel_file,

                "Sheet": asset.sheet_name,

                "Original Row": asset.row_number

            })

        df = pd.DataFrame(rows)

        df.to_excel(
            output_file,
            index=False
        )

    def create_asset_excel(
        self,
        assets,
        output_file: Path
    ):

        rows = []

        for asset in assets:

            data = json.loads(asset.data)

            data["UUID"] = asset.uuid

            data["QR URL"] = self.build_url(asset)

            rows.append(data)

        df = pd.DataFrame(rows)

        df.to_excel(
            output_file,
            index=False
        )