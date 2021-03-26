import b


def get_str():
    b.HOGE = "piyo"  # bでimportしたHOGEの値を変更
    return f"123_{b.get_hoge()}_456"  # 123_piyo_456


if __name__ == "__main__":
    print(get_str())
