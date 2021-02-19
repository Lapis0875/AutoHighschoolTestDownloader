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
        testTitle: str = test['title']
        print(f'[{subject}] test - {testTitle}')
        parsedData[subject][testTitle] = {}
        downloads = test['download']
        parsedData[subject][testTitle] = {}
        for category, downloadInfo in downloads.items():
            funcSpec: Dict[str, str] = parseFunctionTemp(downloadInfo['href'])
            print(f'[{subject}] - {testTitle} - parsed javascript function call :')
            print(funcSpec)
            url = funcSpec['args']['imgUrl'].strip("'")

            file = url.replace('http://', '').split('/')[-1]
            fileName, fileExt = file.split('.')

            parsed = fileName.split('_')
            if len(parsed) == 3 or len(parsed) == 5:
                code = parsed[-1]
            elif len(parsed) == 4 or len(parsed) == 6 or len(parsed) == 7:
                code = ''.join(parsed[-2:])
            else:
                raise ValueError(f'Unexpected code in filename {fileName}')
            parsedData[subject][testTitle][category] = {
                'url': f'http://wdown.ebsi.co.kr/W61001/01exam{url}' if not url.startswith('http') else url,
                'file': file,
                'file_ext': fileExt,
                'code': code
            }

with open('data.json', mode='wt', encoding='utf-8') as f:
    json.dump(parsedData, f, ensure_ascii=False, indent=4)
