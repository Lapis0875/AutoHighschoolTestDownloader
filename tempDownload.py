import json
import asyncio
import aiohttp
import aiofiles
from typing import Any, Dict, List, Coroutine, Optional

with open('analysis/data.json', mode='rt', encoding='utf-8') as f:
    data: Dict[str, Dict[str, Any]] = json.load(f)

targetSubjects = [
    '국어',
    '수학가형',
    '수학나형',
    '영어',
    '한국사',
    '물리학Ⅰ',
    '물리학Ⅱ',
    '물리Ⅰ',
    '물리Ⅱ',
    '화학Ⅰ',
    '화학Ⅱ',
    '지구과학Ⅰ',
    '지구과학Ⅱ',
    '물리Ⅱ',
    '물리Ⅱ',
]


async def download(url: str, filename: str):
    print(f'Asynchronous downloader : download {url} into file {filename}')
    async with aiohttp.request('get', url) as resp:
        async with aiofiles.open(f'download/{filename}', mode='wb') as f:
            await f.write(await resp.read())


async def sessionDownload(url: str, filename: str, session: aiohttp.ClientSession):
    print(f'Asynchronous session downloader : download {url} into file {filename}')
    async with session.get(url) as resp:
        async with aiofiles.open(f'download/{filename}', mode='wb') as f:
            await f.write(await resp.read())


async def main(session: Optional[aiohttp.ClientSession] = None):
    tasks: List[Coroutine] = []
    for subject, tests in data.items():
        if subject in targetSubjects:
            for testName, testData in tests.items():
                for downloadCategory, downloadData in testData.items():
                    task = download(downloadData['url'], f'{testName}-{downloadCategory}.{downloadData["file_ext"]}')\
                        if session is None\
                        else sessionDownload(downloadData['url'], f'{testName}-{downloadCategory}.{downloadData["file_ext"]}', session)
                    tasks.append(task)

    await asyncio.gather(*tasks)


async def sessionDownloader():
    async with aiohttp.ClientSession() as session:
        await main(session)


async def test():
    subject, tests = tuple(data.items())[0]
    testName, testData = tuple(tests.items())[0]
    print(f'Test download of subject {subject}, test title : {testName}')
    print(f'Url : {testData["문제"]["url"]}')
    async with aiohttp.request('get', testData['문제']['url']) as resp:
        # print(await resp.text())
        async with aiofiles.open(f'download/test.pdf', mode='wb') as f:
            await f.write(await resp.read())

asyncio.get_event_loop().run_until_complete(sessionDownloader())
