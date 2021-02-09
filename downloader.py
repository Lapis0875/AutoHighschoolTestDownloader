from __future__ import annotations
from typing import Protocol, Dict, Any, Optional
from enum import Enum
import asyncio
import aiohttp
import aiofiles
import os
from .models import JSON, SubjectCode


class RunResult(Enum):
    SUCCESS = 0
    FAILED = -1


class Runnable(Protocol):
    def run(self) -> RunResult:  ...


class AsyncDownloader:
    """

    """
    @classmethod
    def fromJson(cls, data: JSON) -> AsyncDownloader:
        data


    def __init__(self, info: JSON):
        self._loop = asyncio.get_event_loop()

    @property
    def loop(self) -> asyncio.AbstractEventLoop:
        return self._loop

    def run(self) -> RunResult:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(
            asyncio.gather(
                *map(

                )
            )
        )
        return RunResult.SUCCESS

    async def download(self, year: int, month: int, subject: str, filename: Optional[str] = None) -> None:
        """
        Download test file on url.
        Args:
            year (int) : 기출문제의 연도.
            month (int) : 기출문제의 달.
            subject (str) : 기출문제의 과목.
            filename (Optional[str]) : 저장할 파일 이름. 지정하지 않는다면, year-month-subject 형태로 저장된다.
        """
        if filename is None:
            filename = f'{year:4d}-{month:02d}-{subject}'
        url = f'{}'
        async with aiohttp.request('get', url) as resp:
            path: str = os.path.join(os.getcwd(), 'downloads', filename)
            async with aiofiles.open(path, mode='wb') as f:
                await f.write(await resp.read())

    async def download_test(self, ):


