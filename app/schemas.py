from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class DicomMetadataBase(BaseModel):
    patient_id: str
    study_instance_uid: str
    series_instance_uid: str
    modality: str


class DicomMetadataCreate(DicomMetadataBase):
    pass


class DicomMetadata(DicomMetadataBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class DicomMetadataQuery(BaseModel):
    patient_id: Optional[str] = None
    study_instance_uid: Optional[str] = None
    series_instance_uid: Optional[str] = None
    modality: Optional[str] = None
