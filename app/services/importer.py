import json

from sqlalchemy.orm import Session

from app.models import Asset
from app.services.uuid_service import UUIDService
from app.services.slug_service import SlugService
from pathlib import Path
import pandas as pd


class ExcelImporter:

    def __init__(self, db: Session):

        self.db = db

    def load_workbook(self, file_path: Path):
        return pd.ExcelFile(file_path)

    def read_sheet(self, workbook, sheet_name):

        df = pd.read_excel(
            workbook,
            sheet_name=sheet_name,
            dtype=str
        )

        # Replace NaN with empty string
        df = df.fillna("")

        return df

    def get_rows(self, dataframe):

        rows = []

        for _, row in dataframe.iterrows():

            row_dict = {}

            is_empty = True

            for column in dataframe.columns:

                value = str(row[column]).strip()

                if value == "":
                    value = "-"
                else:
                    is_empty = False

                row_dict[column] = value

            # Skip completely empty rows
            if is_empty:
                continue

            rows.append(row_dict)

        return rows
    
    
    def import_workbook(self,company, file_path: Path):

        self.validate_file(company,file_path)

        workbook = self.load_workbook(file_path)

        excel_slug = SlugService.generate(
            file_path.stem
        )

        imported = []

        try:

            for sheet in workbook.sheet_names:

                sheet_slug = SlugService.generate(sheet)

                df = self.read_sheet(
                    workbook,
                    sheet
                )

                rows = self.get_rows(df)

                for row_number, row in enumerate(rows, start=2):

                    asset = self.save_asset(

                        company=company,

                        excel_file=file_path.name,

                        excel_slug=excel_slug,

                        sheet_name=sheet,

                        sheet_slug=sheet_slug,

                        row_number=row_number,

                        row_data=row

                    )

                    imported.append(asset)

            self.db.commit()

            return imported

        except Exception:

            self.db.rollback()

            raise

    def validate_file(self,company, file_path: Path):

        existing = (
            self.db.query(Asset)
            .filter(
                Asset.company == company,
                Asset.excel_file == file_path.name
            )
            .first()
        )

        if existing:

            raise Exception(
                f"{file_path.name} has already been imported."
            )

    def save_asset(
        self,
        company,
        excel_file,
        excel_slug,
        sheet_name,
        sheet_slug,
        row_number,
        row_data
    ):

        asset = Asset(

            company=company,

            uuid=UUIDService.generate(),

            excel_file=excel_file,

            excel_slug=excel_slug,

            sheet_name=sheet_name,

            sheet_slug=sheet_slug,

            row_number=row_number,

            data=json.dumps(row_data)

        )

        self.db.add(asset)

        return asset