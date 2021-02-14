import json

from typing import Dict, Any
from analysis.downloads_pyport import parseFunctionTemp

with open('raw_data.json', mode='rt', encoding='utf-8') as f:
    rawData: Dict[str, Any] = json.load(f)

parsedData = {}


for subject, tests in rawData.items():
    print(f'Analyzing tests of subject {subject}')
    parsedData[subject] = {}
    for test in tests:
        testTitle: str = test["title"]
        print(f'[{subject}] test - {testTitle}')
        parsedData[subject][testTitle] = {}
        downloads = test['download']
        for category, downloadInfo in downloads.items():
            parsedData[subject][testTitle] = {}
            funcSpec: Dict[str, str] = parseFunctionTemp(downloadInfo['href'])
            print(f'[{subject}] - {testTitle} - parsed javascript function call :')
            print(funcSpec)
            url = funcSpec['args']['imgUrl']
            parsedData[subject][testTitle]['url'] = url
            file = url.strip('http://').split('/')[-1]
            fileName, fileExt = file.split('.')
            code = fileName.split('_')[-1]
            parsedData[subject][testTitle]['file'] = file
            parsedData[subject][testTitle]['file_ext'] = fileExt
            parsedData[subject][testTitle]['code'] = code

with open('data.json', mode='wt', encoding='utf-8') as f:
    json.dump(parsedData, f, ensure_ascii=False, indent=4)
