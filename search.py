PATH = 'csv/character.csv'


def search():
  word = input("鬼滅の登場人物の名前を入力してください >>> ")

  # CSV読み込み
  source = read_csv()

  if word in source:
    print("{}が見つかりました".format(word))
  else:
    source.append(format(word))
    print("リストに存在しなかったので追加しました。")


def read_csv():
  with open(PATH) as f:
    read_csv_str = f.read()
    return read_csv_str.split(",")


if __name__ == "__main__":
  search()
