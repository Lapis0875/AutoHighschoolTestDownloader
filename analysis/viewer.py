import json
from functools import partial
from typing import Dict, Any
from analysis.markdown import MarkdownSyntax, Markdown

with open('data.json', mode='rt', encoding='utf-8') as f:
    parsedData = json.load(f)


def writeTestsInfo(md: Markdown, subjectData: Dict[str, Any]):
    md.writeLine(MarkdownSyntax.Plain, '코드      \t| 시험 이름')
    for testName, info in subjectData.items():
        md.writeLine(MarkdownSyntax.Plain, f'{info["code"]}\t| {testName}')


def entireViewer(data: Dict[str, Any]) -> int:
    md = Markdown('ebs_기출문제_code_분석_전과목')
    # Append title
    md.writeLine(MarkdownSyntax.H1, 'EBS 기출문제 파일 코드 분석 - 전과목')
    # Append explanation about code rule
    md.writeLine(MarkdownSyntax.H2, '암호 규칙 - 구성')
    md.writeLine(MarkdownSyntax.Plain, '총 8자의 문자열이다.')
    md.writeLine(MarkdownSyntax.Plain, '알파벳 대소문자, 숫자로 구성된다.')
    # Append tests data to analyzing code rules
    md.writeLine(MarkdownSyntax.H2, '여러 시험지들과 그 코드')
    for subject, subjectData in data.items():
        md.writeLine(MarkdownSyntax.Bold, subject)
        writeTestsInfo(md, subjectData)
    return 0


def subjectViewer(subjectName: str, subjectData: Dict[str, Any]) -> int:
    md = Markdown(f'ebs_기출문제_code_분석_{subjectName}')
    # Append title
    md.writeLine(MarkdownSyntax.H1, f'EBS 기출문제 파일 코드 분석 - {subjectName} 과목')
    # Append explanation about code rule
    md.writeLine(MarkdownSyntax.H2, '암호 규칙 - 구성')
    md.writeLine(MarkdownSyntax.Plain, '총 8자의 문자열이다.')
    md.writeLine(MarkdownSyntax.Plain, '알파벳 대소문자, 숫자로 구성된다.')
    # Append tests data to analyzing code rules
    md.writeLine(MarkdownSyntax.H2, '여러 시험지들과 그 코드')
    writeTestsInfo(md, subjectData)
    return 0


def main():
    entireViewer(parsedData)
    for subject, subjectData in parsedData.items():
        subjectViewer(subject, subjectData)


if __name__ == '__main__':
    main()
