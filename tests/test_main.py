from unittest.mock import patch

import b
import main1


def test_get_str1():
    # 普通にテスト
    actual = main1.get_str()
    expected = "123_hoge_456"
    assert actual == expected


def test_get_str2():
    # 固定値を上書きしてテスト
    # b.get_hoge関数自体の挙動を確認したい場合
    b.HOGE = "piyo"

    actual = main1.get_str()
    expected = "123_piyo_456"
    assert actual == expected


@patch("main1.b.get_hoge", return_value="piyo")
def test_get_str3(get_hoge_mock):
    # b.get_hoge関数をモック化してテスト
    # b.get_hoge関数は別のユニットテストで確認されている場合

    actual = main1.get_str()
    expected = "123_piyo_456"
    assert actual == expected
    get_hoge_mock.assert_called_once()
