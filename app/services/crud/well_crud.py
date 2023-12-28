from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
import logging
from app.core.database import get_session
from app.models.well_models import WelleModel
from app.schemas.wells_schemas import WelleSchema, WelleUpdateSchema

logger = logging.getLogger(__name__)

async def create_well(well_data: WelleSchema) -> WelleModel:
    async with get_session() as session:
        new_well = WelleModel(**well_data.model_dump())
        session.add(new_well)
        await session.commit()
        return new_well


async def get_wells() -> List[WelleModel]:
    async with get_session() as session:
        try:
            query = select(WelleModel)
            result = await session.execute(query)
            return result.scalars().all()
        except SQLAlchemyError as e:
            logger.error(f"Error fetching all wells: {e}")
            return []


async def get_well(well_id: str) -> Optional[WelleModel]:
    async with get_session() as session:
        try:
            query = select(WelleModel).filter(WelleModel.well_id == well_id)
            result = await session.execute(query)
            return result.scalar_one()
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error fetching well with ID {well_id}: {e}")
            return None


async def get_well_by_number(number: str) -> Optional[WelleModel]:
    async with get_session() as session:
        try:
            query = select(WelleModel).filter(WelleModel.number == number)
            result = await session.execute(query)
            return result.scalar_one()
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error fetching well with number {number}: {e}")
            return None


async def update_well(
    well_id: str, update_well_data: WelleUpdateSchema
) -> Optional[WelleModel]:
    update_data_dict = update_well_data.dict()  # Convert Pydantic model to dictionary
    async with get_session() as session:
        try:
            query = select(WelleModel).filter(WelleModel.id == well_id)
            result = await session.execute(query)
            well_to_update = result.scalar_one()
            for (
                key,
                value,
            ) in update_data_dict.items():  # Now iterate over the dictionary
                if value is not None:
                    setattr(well_to_update, key, value)
            await session.commit()
            await session.refresh(well_to_update)
            return well_to_update
        except NoResultFound:
            return None
        except SQLAlchemyError as e:
            logger.error(f"Error updating well with ID {well_id}: {e}")
            return None

async def delete_well(well_id: str) -> bool:
    async with get_session() as session:
        try:
            query = select(WelleModel).filter(WelleModel.id == well_id)
            result = await session.execute(query)
            well_to_delete = result.scalar_one()
            await session.delete(well_to_delete)
            await session.commit()
            return True
        except NoResultFound:
            return False
