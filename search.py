csv_path = 'csv/character.csv'


def search():
  word = input("鬼滅の登場人物の名前を入力してください >>> ")

  # CSV読み込み
  source = read_csv()

  if word in source:
    print(f"{word}が見つかりました")
  else:
    source.append(word)
    print("リストに存在しなかったので追加しました。")

    # CSV書き込み
    write_csv(source)


def read_csv():
  with open(csv_path) as f:
    read_csv_str = f.read()
    return read_csv_str.split(",")


def write_csv(source_list):
  with open(csv_path, mode='w') as f:
    f.write(",".join(source_list))


if __name__ == "__main__":
  search()
