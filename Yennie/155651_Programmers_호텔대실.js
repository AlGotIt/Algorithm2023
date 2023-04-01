// 입실 시간 기준으로 sort
// 퇴실 시간 = 퇴실 시간 + 10분
function solution(book_time) {
    let finishT = []; // 끝나는 시간을 담는 배열
    let sortedBT = book_time.sort();

    sortedBT.forEach((t) => {
        let inTime = t[0].split(":");
        let inTimeMin = inTime[0] * 60 + parseInt(inTime[1]);
        let outTime = t[1].split(":");
        let outTimeMin = outTime[0] * 60 + parseInt(outTime[1]) + 10;
        
        if (finishT[0] > 0 && inTimeMin >= finishT[0]) { // 지금 온 사람이 가장 빨리 끝나는 방에 바로 들어갈 수 있는 경우
            finishT.splice(finishT.indexOf(finishT[0]), 1);
        } 
        finishT.push(outTimeMin);
        finishT.sort(function(a, b){ return a-b; }); // 항상 가장 빨리 끝나는 순서로 정렬
    });
    return finishT.length;
}