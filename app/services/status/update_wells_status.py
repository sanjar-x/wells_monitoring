from datetime import datetime, timedelta
from sqlalchemy.future import select
from app.core.database import get_session
from app.models.well_models import WelleModel, MessageModel

async def update_well_status():
    async with get_session() as session:
        wells = await session.execute(select(WelleModel))  # type: ignore
        wells = wells.scalars().all()

        for well in wells:
            last_message_query = (session.query(MessageModel)
                                         .filter(MessageModel.number == well.number)
                                         .order_by(MessageModel.time.desc()))
            last_message = await session.execute(last_message_query)  # type: ignore
            last_message = last_message.scalars().first()

            if last_message and (datetime.utcnow() - last_message.time <= timedelta(days=1)):
                well.status = True
            else:
                well.status = False

        await session.commit() # type: ignore


