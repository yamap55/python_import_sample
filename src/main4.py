import define

define.HOGE = "piyo"  # bがimportされる前にdefineの値を変更
import b  # noqa E402


def get_str():
    return f"123_{b.get_hoge()}_456"  # 123_piyo_456


if __name__ == "__main__":
    print(get_str())
