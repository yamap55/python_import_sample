import b
import define


def get_str():
    define.HOGE = "piyo"  # define の値を変更
    return f"123_{b.get_hoge()}_456"  # 変更されない！ -> 123_hoge_456


if __name__ == "__main__":
    print(get_str())
