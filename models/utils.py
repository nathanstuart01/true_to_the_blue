from sqlalchemy import event
from sqlalchemy.orm import Mapper
from pendulum import now

from models.base.base import BaseModel


def update_timestamp(mapper: Mapper, connection, target: BaseModel):
    target.updated_at = now()

# Automatically apply to all subclasses of BaseModel
@event.listens_for(BaseModel, "before_update", propagate=True)
def receive_before_update(mapper, connection, target):
    update_timestamp(mapper, connection, target)

@event.listens_for(BaseModel, "before_insert", propagate=True)
def receive_before_insert(mapper, connection, target):
    target.updated_at = target.updated_at or now()