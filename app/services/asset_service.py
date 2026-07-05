from sqlalchemy.orm import Session

from app.models import Asset


class AssetService:

    def __init__(self, db: Session):
        self.db = db

    def get_asset(
        self,
        company: str,
        excel_slug: str,
        sheet_slug: str,
        uuid: str
    ):

        return (
            self.db.query(Asset)
            .filter(
                Asset.company == company,
                Asset.excel_slug == excel_slug,
                Asset.sheet_slug == sheet_slug,
                Asset.uuid == uuid
            )
            .first()
        )