import pandas as pd
PATH = './csv/character.csv'


def search():
  word = input("鬼滅の登場人物の名前を入力してください >>> ")

  # 読み込み
  source = pd.read_csv(PATH, header=None).values.tolist()

  if word in source[0]:
    print("{}が見つかりました".format(word))
  else:
    source[0].append(format(word))
    print("リストに存在しなかったので追加しました。")
    df = pd.DataFrame(source)

    # 書き込み
    df.to_csv(PATH, header=None, index=False)


if __name__ == "__main__":
  search()
