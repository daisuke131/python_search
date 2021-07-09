source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]


def search():
  word = input("鬼滅の登場人物の名前を入力してください >>> ")

  if word in source:
    print("{}が見つかりました".format(word))
  else:
    source.append(format(word))
    print("{}は見つかりませんでした".format(word))


if __name__ == "__main__":
  search()
