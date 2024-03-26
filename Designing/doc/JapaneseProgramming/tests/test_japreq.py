import pytest

#テスト対象コード

def check_botton_press(Arduino上のボタンを, Arduino上のボタンを押された回数が):
    
    Arduino上のボタンを = input('ボタンが押したか押していないかを入力してください（押した/押していない）: ')
    Arduino上のボタンを押された回数が = input('1~5回のどれかを入力してください:')
    Arduino上のLEDは = print

    実際に Arduino上のボタンを == '押した' とき
        Arduino上のLEDは('ボタンを検知する')

        実際に Arduino上のボタンを押された回数が == '1回' とき
#            Arduino上のLEDは('点灯する')
            return '点灯する'
        ではなくて Arduino上のボタンを押された回数が == '2回' とき
#            Arduino上のLEDは(' 遅い速度の点滅する')
            return '遅い速度の点滅する'
        ではなくて Arduino上のボタンを押された回数が == '3回' とき
#            Arduino上のLEDは(' 普通の速度の点滅する')
            return '普通の速度の点滅する'
        ではなくて Arduino上のボタンを押された回数が == '4回' とき
#            Arduino上のLEDは(' 早い速度の点滅する')
            return '早い速度の点滅する'
        ではなくて Arduino上のボタンを押された回数が == '5回' とき
#            Arduino上のLEDは('消灯する')
            return '消灯する'
        でなければ
#            Arduino上のLEDは('何もしない')
            return '何もしない'
        
#テストコード
@pytest.mark.parametrize("Arduino上のボタンを, Arduino上のボタンを押された回数が, expected", [
    ('押した', '1回', '点灯する'),
    ('押した', '2回', '遅い速度の点滅する'),
    ('押した', '3回', '普通の速度の点滅する'),
    ('押した', '4回', '早い速度の点滅する'),
    ('押した', '5回', '消灯する'),
    ('押していない', '1回', 'ボタンを検知しない'),  # ボタンが押されていない場合
    ('押した', '6回', '何もしない'),  # 押された回数が範囲外の場合
])
def test_check_button_press(Arduino上のボタンを, Arduino上のボタンを押された回数が, expected):
    assert check_button_press(bArduino上のボタンを, Arduino上のボタンを押された回数が) == expected