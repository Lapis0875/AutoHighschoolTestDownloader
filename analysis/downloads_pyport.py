"""
Port javascript file download functions in ebs page into python. Maybe unnecessary, but... whatever.
"""


def goDownLoadP(imgUrl: str, wl, irecord, catCd, arCnt, subjectId,isEvenNum,fileExt, paperId):
    isPdf: bool = True if fileExt == 'pdf' else False

