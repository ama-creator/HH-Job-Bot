import httpx


class HHClient:
    BASE_URL = "https://api.hh.ru"

    def __init__(self) -> None:
        self.client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=30.0,
            headers={"User-Agent": "HH-Job-Bot/0.1 (your-current@gmail.com)"},
        )

    async def close(self) -> None:
        await self.client.aclose()

    async def search_vacancies(self, text: str, page: int = 0, per_page: int = 20) -> dict:
        response = await self.client.get(
            "/vacancies", params={"text": text, "page": page, "per_page": per_page}
        )

        if response.status_code >= 400:
            print("STATUS:", response.status_code)
            print("BODY:", response.text)

        response.raise_for_status()
        return response.json()
