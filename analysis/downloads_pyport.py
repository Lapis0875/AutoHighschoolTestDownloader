"""
Port javascript file download functions in ebs page into python. Maybe unnecessary, but... whatever.
"""
import inspect
from typing import Dict, Tuple, Any, List
import re

functionPattern = re.compile(r"(?P<funcName>\w+)\((?P<args>\S+,?)*\)")


def parseFunctionTemp(js_func: str) -> Dict[str, Any]:
    func = js_func.strip('javascript:')
    firstBracketIndex: int = func.find('(')
    lastBracketIndex: int = func.rfind(')')
    funcName: str = func[:firstBracketIndex]
    rawArgs: str = func[firstBracketIndex+1: lastBracketIndex]
    args = rawArgs.split(',')
    namedFuncInfo: Dict[str, Any] = getJSFunctionInfo(funcName, args)
    return namedFuncInfo


# 문제
def goDownLoadP(imgUrl: str, wl, irecord, catCd, arCnt, subjectId, isEvenNum: bool, fileExt, paperId):
    isPdf: bool = True if fileExt == 'pdf' else False
    url: str = 'http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl


# 듣기
def goDownLoadR(imgUrl: str, wl, irecord, catCd, arCnt, subjectId, isEvenNum: bool, fileExt):
    pass


# 대본
def goDownLoadD(imgUrl: str, wl, irecord, catCd, arCnt, subjectId, isEvenNum: bool, fileExt):
    pass


# Ported function from `lib.es5.d.ts`
def escape(param) -> str:
    # Computes a new string in which certain characters have been replaced by a hexadecimal escape sequence.
    # Args:
    #   param (string) : A string value
    return ''


# 정답오픈 1
def goDownLoadJ(imgUrl: str, wl, irecord, catCd, arCnt, subjectId, isEvenNum: bool, fileExt, subjectNm, paperId):
    url: str = f'/ebs/xip/xipa/retrieveCorrectAnswerImagePop.ebs?imageSrc={imgUrl}&subjectNm={escape(subjectNm)}'


# 정답오픈 2
def goDownLoadJ2(imgUrl: str, wl, irecord, catCd, arCnt, subjectId, isEvenNum: bool, fileExt):
    pass


# 해설오픈
def goDownLoadH(imgUrl: str, wl, irecord, catCd, arCnt, subjectId, isEvenNum: bool, fileExt, paperId):
    pass


def parseJSFunc(js_func: str) -> Dict[str, Any]:
    """
    Example:
        javascript:goDownLoadH('/20201203/go3/s_easta_hsj_JV3J3A55.pdf','/fullserv_down/202012033/sat_mun','202012033','304','9','63001','0','pdf')
        -> goDownLoadH, ('/20201203/go3/s_easta_hsj_JV3J3A55.pdf', '/fullserv_down/202012033/sat_mun', '202012033', '304', '9','63001','0','pdf')
    Args:
        js_func (str) : string value containing js function call expression.
    Returns:
        Parsed JS Function as str, Tuple[str] (str for function name, Tuple[str, ...]  for arguments.)
    """
    print('debug : regexp matching start')
    match = functionPattern.match(js_func.strip('javascript:'))
    print('debug : regexp matching ended with object :', match)
    if match is None:
        raise ValueError('Invalid javascript function call expression!')
    print('debug : parsed function expression :')
    parsed = match.groupdict()
    print(parsed)
    namedFuncInfo: Dict[str, Any] = getJSFunctionInfo(parsed['funcName'], parsed['args'].split(','))
    return namedFuncInfo


def getJSFunctionInfo(funcName: str, args: List[str]):
    paramLength = len(args)
    if paramLength == 8:
        argSpec = inspect.getfullargspec(goDownLoadR)
    elif paramLength == 9:
        argSpec = inspect.getfullargspec(goDownLoadP)
    elif paramLength == 10:
        argSpec = inspect.getfullargspec(goDownLoadJ)
    else:
        raise ValueError('Unexpected params!')
    argInfo = {
        argSpec.args[i]: args[i]
        for i
        in range(paramLength)
    }
    return {
        'function': funcName,
        'args': argInfo
    }


def callPortFunction(js_func: str) -> Any:
    func_name, func_args = parseJSFunc(js_func)
    return locals().get(func_name)(*func_args)
