from os import path
import pandas as pd
csv_path = './csv/character.csv'


def search():
  word = input("鬼滅の登場人物の名前を入力してください >>> ")

  # 読み込み
  source = pd.read_csv(csv_path, header=None).values.tolist()

  if word in source[0]:
    print(f"{word}が見つかりました")
  else:
    source[0].append(word)
    print("リストに存在しなかったので追加しました。")
    df = pd.DataFrame(source)

    # 書き込み
    df.to_csv(csv_path, header=None, index=False)


if __name__ == "__main__":
  search()
