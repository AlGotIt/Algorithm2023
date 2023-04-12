<?
    fscanf(STDIN,"%d",$N);
    $dp = [];
    $dp = array_fill(0, $N, 0); // [돈] = 최소 동전수 
    
    $dp[3] = 1;
    $dp[4] = 0;
    $dp[5] = 1;

    for($i = 6; $i <= $N; $i++){
        if ($dp[$i-3] && $dp[$i-5]) {
            $dp[$i] = min($dp[$i-3], $dp[$i-5]) + 1;
        } else {
            $dp[$i] = ($dp[$i-3] + $dp[$i-5]) ? ($dp[$i-3] + $dp[$i-5]) + 1 : 0; 
        }
    }
    
    echo $dp[$N] ?: -1;
?>
