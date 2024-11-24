import asyncio
import time
from prefect import flow, task
from tasks.extract_task import extract_task
from tasks.load_task import load_task

@flow(name='ETL OFERTAS LABORALES')
async def main_flow():
    skills = ["python", "react"]

    for skill in skills:
        offers = await extract_task(skill)
        print(offers)
        await load_task(offers)
        time.sleep(5)
    
    
if __name__ == '__main__':
    asyncio.run(main_flow())