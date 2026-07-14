from pathlib import Path

from app.init_db import initialize_database
from app.database import SessionLocal
from app.services.importer import ExcelImporter
from app.services.excel_writer import ExcelWriter
from app.config import BASE_URL

initialize_database()

db = SessionLocal()

importer = ExcelImporter(db)

excel_path = Path("uploads/Tata_sample.xlsx")

assets = importer.import_workbook(
    company="Tata",
    file_path=excel_path
)

writer = ExcelWriter(
    base_url=BASE_URL
)

writer.create_asset_excel(
    assets,
    Path("generated/Tata_With_UUID.xlsx")
)

writer.create_mapping_excel(
    assets,
    Path("generated/Tata_UUID_Mapping.xlsx")
)

print(f"Imported {len(assets)} assets")

print()

print("First URL")

first = assets[0]

print(
    f"/assets/{first.company}/{first.excel_slug}/{first.sheet_slug}/{first.uuid}"
)