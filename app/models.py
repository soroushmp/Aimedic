from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base


class DicomMetadata(Base):
    __tablename__ = "dicom_metadata"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, index=True)
    study_instance_uid = Column(String, index=True)
    series_instance_uid = Column(String, index=True)
    modality = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
