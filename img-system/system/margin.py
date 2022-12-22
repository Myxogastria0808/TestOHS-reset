import cv2
import math
import glob
import os

os.chdir('../')
white = [255, 255, 255]

png = glob.glob('*.png')
png_len = len(png)

if png_len == 0:
    pass
elif png_len != 0:
    for png_arr in png:
      if __name__ == "__main__":
        img = cv2.imread(png_arr)
        height, width, color = img.shape # 画像の縦横サイズを取得

        # 縦長画像→幅を拡張する
      if height > width:
        diffsize = height - width
        # 元画像を中央ぞろえにしたいので、左右に均等に余白を入れる
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, value=white)
        path = ('{png_arr}' .format(png_arr=png_arr))
        cv2.imwrite(path, padding_img)

      # 横長画像→高さを拡張する
      elif width > height:
        diffsize = width - height
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, value=white)
        path = ('{png_arr}' .format(png_arr=png_arr))
        cv2.imwrite(path, padding_img)
      else:
        pass


png_large = glob.glob('*.PNG')
png_len_large = len(png_large)

if png_len_large == 0:
    pass
elif png_len_large != 0:
    for png_arr_large in png_large:
      if __name__ == "__main__":
        img = cv2.imread(png_arr_large)
        height, width, color = img.shape # 画像の縦横サイズを取得

        # 縦長画像→幅を拡張する
      if height > width:
        diffsize = height - width
        # 元画像を中央ぞろえにしたいので、左右に均等に余白を入れる
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, value=white)
        path = ('{png_arr_large}' .format(png_arr_large=png_arr_large))
        cv2.imwrite(path, padding_img)

      # 横長画像→高さを拡張する
      elif width > height:
        diffsize = width - height
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, value=white)
        path = ('{png_arr_large}' .format(png_arr_large=png_arr_large))
        cv2.imwrite(path, padding_img)
      else:
        pass


jpg = glob.glob('*.jpg')
jpg_len = len(jpg)

if jpg_len == 0:
    pass
elif jpg_len != 0:
    for jpg_arr in jpg:
      if __name__ == "__main__":
        img = cv2.imread(jpg_arr)
        height, width, color = img.shape # 画像の縦横サイズを取得

        # 縦長画像→幅を拡張する
      if height > width:
        diffsize = height - width
        # 元画像を中央ぞろえにしたいので、左右に均等に余白を入れる
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpg_arr}' .format(jpg_arr=jpg_arr))
        cv2.imwrite(path, padding_img)

      # 横長画像→高さを拡張する
      elif width > height:
        diffsize = width - height
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpg_arr}' .format(jpg_arr=jpg_arr))
        cv2.imwrite(path, padding_img)
      else:
        pass


jpg_large = glob.glob('*.JPG')
jpg_len_large = len(jpg_large)

if jpg_len_large == 0:
    pass
elif jpg_len_large != 0:
    for jpg_arr_large in jpg_large:
      if __name__ == "__main__":
        img = cv2.imread(jpg_arr_large)
        height, width, color = img.shape # 画像の縦横サイズを取得

        # 縦長画像→幅を拡張する
      if height > width:
        diffsize = height - width
        # 元画像を中央ぞろえにしたいので、左右に均等に余白を入れる
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpg_arr_large}' .format(jpg_arr_large=jpg_arr_large))
        cv2.imwrite(path, padding_img)

      # 横長画像→高さを拡張する
      elif width > height:
        diffsize = width - height
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpg_arr_large}' .format(jpg_arr_large=jpg_arr_large))
        cv2.imwrite(path, padding_img)
      else:
        pass


jpeg = glob.glob('*.jpeg')
jpeg_len = len(jpeg)

if jpeg_len == 0:
    pass
elif jpeg_len != 0:
    for jpeg_arr in jpeg:
      if __name__ == "__main__":
        img = cv2.imread(jpeg_arr)
        height, width, color = img.shape # 画像の縦横サイズを取得

        # 縦長画像→幅を拡張する
      if height > width:
        diffsize = height - width
        # 元画像を中央ぞろえにしたいので、左右に均等に余白を入れる
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpeg_arr}' .format(jpeg_arr=jpeg_arr))
        cv2.imwrite(path, padding_img)

      # 横長画像→高さを拡張する
      elif width > height:
        diffsize = width - height
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpeg_arr}' .format(jpeg_arr=jpeg_arr))
        cv2.imwrite(path, padding_img)
      else:
        pass


jpeg_large = glob.glob('*.JPEG')
jpeg_len_large = len(jpeg_large)

if jpeg_len_large == 0:
    pass
elif jpeg_len_large != 0:
    for jpeg_arr_large in jpeg_large:
      if __name__ == "__main__":
        img = cv2.imread(jpeg_arr_large)
        height, width, color = img.shape # 画像の縦横サイズを取得

        # 縦長画像→幅を拡張する
      if height > width:
        diffsize = height - width
        # 元画像を中央ぞろえにしたいので、左右に均等に余白を入れる
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, 0, 0, padding_half, padding_half, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpeg_arr_large}' .format(jpeg_arr_large=jpeg_arr_large))
        cv2.imwrite(path, padding_img)

      # 横長画像→高さを拡張する
      elif width > height:
        diffsize = width - height
        padding_half = int(diffsize / 2)
        padding_img = cv2.copyMakeBorder(img, padding_half, padding_half, 0, 0, cv2.BORDER_CONSTANT, value=white)
        path = ('{jpeg_arr_large}' .format(jpeg_arr_large=jpeg_arr_large))
        cv2.imwrite(path, padding_img)
      else:
        pass