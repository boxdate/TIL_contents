Arduino上のボタンを = input('ボタンが押したか押していないかを入力してください（押した/押していない）: ')
Arduino上のボタンを押された回数が = input('1~5回のどれかを入力してください:')
Arduino上のLEDは = print

実際に Arduino上のボタンを == '押した' とき
    Arduino上のLEDは('ボタンを検知する')
    
    実際に Arduino上のボタンを押された回数が == '1回' とき
        Arduino上のLEDは('点灯する')
    ではなくて Arduino上のボタンを押された回数が == '2回' とき
        Arduino上のLEDは(' 遅い速度の点滅する')
    ではなくて Arduino上のボタンを押された回数が == '3回' とき
        Arduino上のLEDは(' 普通の速度の点滅する')
    ではなくて Arduino上のボタンを押された回数が == '4回' とき
        Arduino上のLEDは(' 早い速度の点滅する')
    ではなくて Arduino上のボタンを押された回数が == '5回' とき
        Arduino上のLEDは('消灯する')
    でなければ
        Arduino上のLEDは('何もしない')