import json
from functools import partial
from typing import Dict, Any
from analysis.markdown import MarkdownSyntax, Markdown

with open('data.json', mode='rt', encoding='utf-8') as f:
    parsedData = json.load(f)


def entireViewer(data: Dict[str, Any]) -> int:
    md = Markdown()
    md.writeLine(MarkdownSyntax.H1, 'Viewing entire parsed data')
    return 0


def subjectViewer(subjectData: Dict[str, Any]) -> int:
    md = Markdown()
    md.writeLine(MarkdownSyntax.H1, f'Viewing parsed data of subject {subjectData}')
    return 0


def main():
    while True:
        subject_name = input("과목명 입력 > ")
        if subject_name == 'all':
            viewer = partial(entireViewer, parsedData)
        else:
            subject_data = parsedData[subject_name]
            viewer = partial(subjectViewer, subject_data)
        if viewer() != 0: break


if __name__ == '__main__':
    main()