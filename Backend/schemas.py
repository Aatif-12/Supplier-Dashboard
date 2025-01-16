from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class SupplierCreate(BaseModel):
    name: str
    country: Optional[str] = None
    compliance_score: Optional[float] = None
    contract_terms: Optional[str] = None
    last_audit: Optional[date] = None


class Supplier(SupplierCreate):
    supplier_id: int  # Automatically generated by the database


class Supplier(BaseModel):
    supplier_id: int
    name: str
    country: Optional[str] = None
    compliance_score: Optional[float] = None
    contract_terms: Optional[str] = None
    last_audit: Optional[date] = None

    class Config:
        from_attributes = True


class ComplianceCheck(BaseModel):
    supplier_id: int
    metric: str
    date_recorded: date
    result: str
    status: str


class ComplianceRecord(BaseModel):
    compliance_record_id: int
    supplier_id: int
    metric: str
    date_recorded: date
    result: str
    status: str


class ComplianceRecord(ComplianceRecord):
    compliance_record_id: int

    class Config:
        from_attributes = True


class InsightsResponse(BaseModel):
    insights: str
