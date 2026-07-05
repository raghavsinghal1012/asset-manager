from fastapi import FastAPI

from app.init_db import initialize_database
import json

from fastapi import Depends
from fastapi import HTTPException

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from fastapi import Request

from app.database import SessionLocal

from app.services.asset_service import AssetService

initialize_database()

app = FastAPI(
    title="Firm 1 Asset Manager"
)

templates = Jinja2Templates(
    directory="app/templates"
)

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "company": "Firm 1",
        "status": "Running",
        "message": "Asset Manager API"
    }

@app.get(
    "/assets/{company}/{excel_slug}/{sheet_slug}/{uuid}",
    response_class=HTMLResponse
)
def view_asset(
    request: Request,
    company: str,
    excel_slug: str,
    sheet_slug: str,
    uuid: str,
    db=Depends(get_db)
):

    service = AssetService(db)

    asset = service.get_asset(
        company,
        excel_slug,
        sheet_slug,
        uuid
    )

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return templates.TemplateResponse(
    request=request,
    name="asset.html",
    context={
        "asset": json.loads(asset.data)
    }
)  