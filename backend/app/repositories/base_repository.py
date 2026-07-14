from datetime import UTC, datetime
from typing import Generic, Optional, Type, TypeVar

from sqlmodel import Session, SQLModel, select

from datetime import UTC, datetime

ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):

    def __init__(
        self,
        model: Type[ModelType],
        session: Session,
    ):
        self.model = model
        self.session = session

    def create(self, obj: ModelType) -> ModelType:
        try:
            self.session.add(obj)
            self.session.commit()
            self.session.refresh(obj)

            return obj

        except Exception:
            self.session.rollback()
            raise

    def get_by_id(
        self,
        entity_id: int,
    ) -> Optional[ModelType]:

        return self.session.get(
            self.model,
            entity_id,
        )

    def get_all(self) -> list[ModelType]:

        statement = select(self.model)

        return list(
            self.session.exec(statement)
        )


    def update(self, obj: ModelType) -> ModelType:
        try:
            if hasattr(obj, "updated_at"):
                obj.updated_at = datetime.now(UTC)

            self.session.add(obj)
            self.session.commit()
            self.session.refresh(obj)

            return obj

        except Exception:
            self.session.rollback()
            raise

    def delete(self, entity_id: int) -> bool:
        try:
            obj = self.get_by_id(entity_id)

            if obj is None:
                return False

            self.session.delete(obj)
            self.session.commit()

            return True

        except Exception:
            self.session.rollback()
            raise