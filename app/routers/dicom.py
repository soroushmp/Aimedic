import io
import pydicom
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import models, schemas
from ..database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.DicomMetadata)
async def upload_dicom(
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    contents = await file.read()

    try:
        dicom_data = pydicom.dcmread(io.BytesIO(contents))

        patient_id = str(getattr(dicom_data, "PatientID", "Unknown"))
        study_instance_uid = str(getattr(dicom_data, "StudyInstanceUID", "Unknown"))
        series_instance_uid = str(getattr(dicom_data, "SeriesInstanceUID", "Unknown"))
        modality = str(getattr(dicom_data, "Modality", "Unknown"))

        db_metadata = models.DicomMetadata(
            patient_id=patient_id,
            study_instance_uid=study_instance_uid,
            series_instance_uid=series_instance_uid,
            modality=modality
        )

        db.add(db_metadata)
        db.commit()
        db.refresh(db_metadata)

        return db_metadata

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Could not process DICOM file: {str(e)}"
        )


@router.get("/", response_model=List[schemas.DicomMetadataQuery])
def get_dicom_metadata(
        patient_id: Optional[str] = Query(None),
        study_instance_uid: Optional[str] = Query(None),
        series_instance_uid: Optional[str] = Query(None),
        modality: Optional[str] = Query(None),
        db: Session = Depends(get_db)
):
    query = db.query(models.DicomMetadata)

    if patient_id:
        query = query.filter(models.DicomMetadata.patient_id == patient_id)
    if study_instance_uid:
        query = query.filter(models.DicomMetadata.study_instance_uid == study_instance_uid)
    if series_instance_uid:
        query = query.filter(models.DicomMetadata.series_instance_uid == series_instance_uid)
    if modality:
        query = query.filter(models.DicomMetadata.modality == modality)

    return query.all()
