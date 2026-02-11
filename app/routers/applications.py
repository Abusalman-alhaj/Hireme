from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, auth

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/{job_id}", response_model=schemas.ApplicationResponse)
def apply_to_job(
    job_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):

    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    existing_application = db.query(models.Application).filter(
        models.Application.user_id == current_user.id,
        models.Application.job_id == job_id
    ).first()

    if existing_application:
        raise HTTPException(status_code=400, detail="Already applied")

    new_application = models.Application(
        user_id=current_user.id,
        job_id=job_id
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application


@router.get("/me", response_model=list[schemas.ApplicationResponse])
def my_applications(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    return db.query(models.Application).filter(
        models.Application.user_id == current_user.id
    ).all()


@router.get("/", response_model=list[schemas.ApplicationResponse])
def all_applications(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(auth.get_current_user)
):

    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return db.query(models.Application).all()
