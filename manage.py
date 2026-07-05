from pathlib import Path
import sys

from app.init_db import initialize_database
from app.database import SessionLocal
from app.services.importer import ExcelImporter
from app.services.excel_writer import ExcelWriter
from app.config import BASE_URL

initialize_database()


def import_excel(company, excel_path):

    db = SessionLocal()

    try:

        importer = ExcelImporter(db)

        assets = importer.import_workbook(
            company=company,
            file_path=Path(excel_path)
        )

        company_folder = Path("generated") / company

        company_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        writer = ExcelWriter(
            base_url=BASE_URL
        )

        writer.create_asset_excel(
            assets,
            company_folder / f"{Path(excel_path).stem}_With_UUID.xlsx"
        )

        writer.create_mapping_excel(
            assets,
            company_folder / f"{Path(excel_path).stem}_UUID_Mapping.xlsx"
        )

        print()
        print("Import completed")
        print(f"Company : {company}")
        print(f"Assets   : {len(assets)}")

    finally:
        db.close()


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("Usage:")
        print("python manage.py import <company> <excel_path>")
        sys.exit()

    command = sys.argv[1]

    if command == "import":

        company = sys.argv[2]

        excel = sys.argv[3]

        import_excel(company, excel)

    else:

        print("Unknown command")