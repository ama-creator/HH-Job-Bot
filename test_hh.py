import asyncio

from app.integrations.hh.client import HHClient


async def main() -> None:
    client = HHClient()

    try:
        result = await client.search_vacancies(
            text="Python developer",
            per_page=5,
        )

        print("Найдено:", result["found"])
        print("Получено:", len(result["items"]))

        for vacancy in result["items"]:
            print(
                vacancy["id"],
                "|",
                vacancy["name"],
                "|",
                vacancy.get("employer", {}).get("name"),
            )

    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())