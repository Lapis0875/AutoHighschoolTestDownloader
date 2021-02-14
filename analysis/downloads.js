//다운로드
/* 사용 예시
* goDownLoadP(
*   &#39;/20201203/go3/eng_mun_8JGC8T6P.pdf&#39;,
*   &#39;/fullserv_down/202012033/eng_mun&#39;,
*   &#39;202012033&#39;,
*   &#39;303&#39;,
*   &#39;2&#39;,
*   &#39;80003&#39;,
*   &#39;0&#39;,
*   &#39;pdf&#39;,
*   &#39;14043689&#39;
* )
*/
function goDownLoadP(imgUrl, wl, irecord, catCd, arCnt, subjectId,isEvenNum,fileExt, paperId) {

    AiServerSubmit('P_S_B_Q_DOW', paperId, 'C'); //AI 로그 스크립트

    var isPdf = 0;
    if(fileExt == 'pdf') isPdf = 1;

    if (loginCheck()) {
        if (imgUrl != '') {
            goDwonCount(irecord  , catCd ,arCnt   ,1,0        ,subjectId );
            webLogXip(wl);
            if(fileExt == 'pdf'){

                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                return;

                try{
                    if ( !! window.ActiveXObject && document.execCommand)     {
                        //익스
                        var _window = window.open("http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl, "_blank");
                        _window.document.close();
                        _window.document.execCommand('SaveAs', true, irecord+'_'+subjectId+'_'+isEvenNum+'.pdf' || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl);
                        _window.close();

                    }else if (!window.ActiveXObject) {
                        var save = document.createElement('a');
                        save.href = "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        save.target = '_blank';

                        /*
                        save.download = irecord+subjectId+isEvenNum || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        var evt = document.createEvent('MouseEvents');
                        evt.initMouseEvent('click', true, true, window, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
                         */

                        save.download = irecord+subjectId+isEvenNum || 'unknown';
                        var evt = document.createEvent('Event');
                        evt.initEvent('click', true, true);

                        save.dispatchEvent(evt);
                        (window.URL || window.webkitURL).revokeObjectURL(save.href);
                    }else{
                        window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                    }
                }catch(e){
                    window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                }

            }else{
                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
            }
        } else {
            alert("준비 중입니다.");
        }
    }
}

//듣기
/* 사용 예시
* 
*/
function goDownLoadR(imgUrl, wl, irecord, catCd, arCnt, subjectId,isEvenNum,fileExt) {

    var isPdf = 0;
    if(fileExt == 'pdf') isPdf = 1;

    if (loginCheck()) {
        if (imgUrl != '') {
            goDwonCount(irecord, catCd, arCnt, 1, 4, subjectId);
            webLogXip(wl);
            if(fileExt == 'pdf'){

                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                return;

                try{
                    if ( !! window.ActiveXObject && document.execCommand)     {
                        //익스
                        var _window = window.open("http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl, "_blank");
                        _window.document.close();
                        _window.document.execCommand('SaveAs', true, irecord+'_'+subjectId+'_'+isEvenNum+'.pdf' || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl);
                        _window.close();

                    }else if (!window.ActiveXObject) {
                        var save = document.createElement('a');
                        save.href = "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        save.target = '_blank';

                        /*
                        save.download = irecord+subjectId+isEvenNum || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        var evt = document.createEvent('MouseEvents');
                        evt.initMouseEvent('click', true, true, window, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
                         */

                        save.download = irecord+subjectId+isEvenNum || 'unknown';
                        var evt = document.createEvent('Event');
                        evt.initEvent('click', true, true);

                        save.dispatchEvent(evt);
                        (window.URL || window.webkitURL).revokeObjectURL(save.href);
                    }else{
                        window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                    }
                }catch(e){
                    window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                }

            }else{
                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
            }
        } else {
            alert("준비 중입니다.");
        }
    }
}

//대본
function goDownLoadD(imgUrl, wl, irecord, catCd, arCnt, subjectId, isEvenNum, fileExt) {

    var isPdf = 0;
    if(fileExt == 'pdf') isPdf = 1;

    if (loginCheck()) {
        if (imgUrl != '') {
            goDwonCount(irecord, catCd, arCnt, 1, 3, subjectId);
            webLogXip(wl);
            if(fileExt == 'pdf'){

                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                return;

                try{
                    if ( !! window.ActiveXObject && document.execCommand)     {
                        //익스
                        var _window = window.open("http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl, "_blank");
                        _window.document.close();
                        _window.document.execCommand('SaveAs', true, irecord+'_'+subjectId+'_'+isEvenNum+'.pdf' || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl);
                        _window.close();

                    }else if (!window.ActiveXObject) {
                        var save = document.createElement('a');
                        save.href = "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        save.target = '_blank';

                        /*
                        save.download = irecord+subjectId+isEvenNum || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        var evt = document.createEvent('MouseEvents');
                        evt.initMouseEvent('click', true, true, window, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
                         */

                        save.download = irecord+subjectId+isEvenNum || 'unknown';
                        var evt = document.createEvent('Event');
                        evt.initEvent('click', true, true);

                        save.dispatchEvent(evt);
                        (window.URL || window.webkitURL).revokeObjectURL(save.href);
                    }else{
                        window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                    }
                }catch(e){
                    window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                }

            }else{
                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
            }
        } else {
            alert("준비 중입니다.");
        }
    }
}

//정답오픈
/* 사용 예시
* goDownLoadJ(
*   &#39;http://wdown.ebsi.co.kr/W61001/01exam/20201203/mobile/h3_m_eng_ans_A2117MYA.png&#39;,
*   &#39;/fullserv_down/202012033/eng_mun&#39;,
*   &#39;202012033&#39;,
*   &#39;303&#39;,
*   &#39;2&#39;,
*   &#39;80003&#39;,
*   &#39;0&#39;,
*   &#39;png&#39;,
*   &#39;2020년 2021 대학수학능력시험 영어 홀수형&#39;,
*   &#39;14043689&#39;
* )
*/
function goDownLoadJ(imgUrl,wl, irecord, catCd, arCnt, subjectId,isEvenNum,fileExt,subjectNm, paperId){

    AiServerSubmit('P_S_B_A_DOW', paperId, 'C'); //AI 로그 스크립트

    setSubjectNm = '';

    if(subjectNm != undefined && subjectNm != 'subjectNm'){
        setSubjectNm = escape(subjectNm);
    }

    var isPdf = 0;
    if(fileExt == 'pdf') isPdf = 1;

    if(loginCheck()){
        if (imgUrl != ''){
            goDwonCount(irecord, catCd, arCnt, 1,     2, subjectId);
            webLogXip(wl);
            window.open('/ebs/xip/xipa/retrieveCorrectAnswerImagePop.ebs?imageSrc=' + imgUrl + '&subjectNm=' + setSubjectNm, 'img', 'width=800,height=500,location=no,resizable=no');
        }else{
            alert("준비 중입니다.");
        }
    }
}

//정답오픈
function goDownLoadJ2(imgUrl, wl, irecord, catCd, arCnt, subjectId,isEvenNum,fileExt) {

    var isPdf = 0;
    if(fileExt == 'pdf') isPdf = 1;

    if (loginCheck()) {
        if (imgUrl != '') {
            goDwonCount(irecord, catCd, arCnt, 1, 2, subjectId);
            webLogXip(wl);

            if(fileExt == 'pdf'){

                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                return;

                try{
                    if ( !! window.ActiveXObject && document.execCommand)     {
                        //익스
                        var _window = window.open("http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl, "_blank");
                        _window.document.close();
                        _window.document.execCommand('SaveAs', true, irecord+'_'+subjectId+'_'+isEvenNum+'.pdf' || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl);
                        _window.close();

                    }else if (!window.ActiveXObject) {
                        var save = document.createElement('a');
                        save.href = "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        save.target = '_blank';

                        /*
                        save.download = irecord+subjectId+isEvenNum || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        var evt = document.createEvent('MouseEvents');
                        evt.initMouseEvent('click', true, true, window, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
                         */

                        save.download = irecord+subjectId+isEvenNum || 'unknown';
                        var evt = document.createEvent('Event');
                        evt.initEvent('click', true, true);

                        save.dispatchEvent(evt);
                        (window.URL || window.webkitURL).revokeObjectURL(save.href);
                    }else{
                        window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                    }
                }catch(e){
                    window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                }

            }else{
                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
            }
        } else {
            alert("준비 중입니다.");
        }
    }
}

//해설오픈
function goDownLoadH(imgUrl, wl, irecord, catCd, arCnt, subjectId,isEvenNum,fileExt, paperId) {

    AiServerSubmit('P_S_B_E_DOW', paperId, 'C'); //AI 로그 스크립트

    var isPdf = 0;
    if(fileExt == 'pdf') isPdf = 1;

    if (loginCheck()) {
        if (imgUrl != '') {
            goDwonCount(irecord, catCd, arCnt, 1,     1, subjectId);
            webLogXip(wl);

            if(fileExt == 'pdf'){

                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                return;

                try{
                    if ( !! window.ActiveXObject && document.execCommand)     {
                        //익스
                        var _window = window.open("http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl, "_blank");
                        _window.document.close();
                        _window.document.execCommand('SaveAs', true, irecord+'_'+subjectId+'_'+isEvenNum+'.pdf' || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl);
                        _window.close();

                    }else if (!window.ActiveXObject) {
                        var save = document.createElement('a');
                        save.href = "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        save.target = '_blank';

                        /*
                        save.download = irecord+subjectId+isEvenNum || "http://wdown.ebsi.co.kr/W61001/01exam"+imgUrl;
                        var evt = document.createEvent('MouseEvents');
                        evt.initMouseEvent('click', true, true, window, 1, 0, 0, 0, 0, false, false, false, false, 0, null);
                         */

                        save.download = irecord+subjectId+isEvenNum || 'unknown';
                        var evt = document.createEvent('Event');
                        evt.initEvent('click', true, true);

                        save.dispatchEvent(evt);
                        (window.URL || window.webkitURL).revokeObjectURL(save.href);
                    }else{
                        window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                    }
                }catch(e){
                    window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
                }

            }else{
                window.open('http://wdown.ebsi.co.kr/W61001/01exam' + imgUrl,'pdf', 'location=no, resizable=no');
            }
        } else {
            alert("준비 중입니다.");
        }
    }
}