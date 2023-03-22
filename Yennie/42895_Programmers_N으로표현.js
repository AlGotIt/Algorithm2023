const calcFuncs = [(a, b) => a + b, 
                    (a, b) => a * b, 
                    (a, b) => a - b,
                    (a, b) => b - a,
                    (a, b) => Math.floor(a / b),
                    (a, b) => Math.floor(b / a)
                ];

function getCalcRes(nth, dp, N) {
    let dpNth = new Set(); // dp[nth]
    dpNth.add(Number(String(N).repeat(nth))); // 55, 555, 5555

    for (let i = 1; i <= parseInt(nth/2); i++) {
        for (const num1 of dp[i].values()) {
            for (const num2 of dp[nth - i].values()) {
                for (const cf of calcFuncs) {
                    const result = cf(num1, num2);
                    dpNth.add(result);
                }
            }
        }
    }
    return dpNth;
}

function solution(N, number) {
    if (N === number) {
        return 1;
    }

    const dp = [];
    dp[1] = new Set([N]);

    for (let i = 2; i <= 8; i++) {
        dp[i] = getCalcRes(i, dp, N);

        if (dp[i].has(number)) {
            return i;
        }
    }

    return -1;
}