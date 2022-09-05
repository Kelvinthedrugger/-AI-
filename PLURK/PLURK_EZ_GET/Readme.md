
## Attention

### mult_just_in_case.py 不會檢查檔案是否已經存在, 務必再三確認
### , 或是動手改良程式碼
### e.g.,
```python
from pathlib import Path
import os
basedir = Path("face_files") # 創造出 face_files 這個物件

if not basedir.is_dir(): # 如果資料夾不存在
    basedir.mkdir() # 創造資料夾, 把抓到的.json 檔案放在這裡, 比較不會亂?


# 可以用face_list.pkl 來找檔名
filename = basedir/"the_filename.json"


# 確認檔案存在與否
# 這就是pathlib 神奇的地方, 用 a/b, 就可以把 a/b 也變成Path() 物件

if not filename.is_file(): 
    download the posts for this emoji

else:
    print(f"{filename} exists, skip")

```


## View the emoji & filename

#### this will print (emoji, name of emoji), loaded from face_list.pkl

```python
python view_faces.py 1 2 3
```

## Fetch emoji(s)

#### remember to change the numbers, which represents the faces to fetch

```python
python mult_just_in_case.py 21 3 6 2 7 69 65 49 > 21_3_6_2_7_69_65_49.txt
```

## Check if create .json file succeeded

#### will print the first 10 element from the fetched .json file
#### will throw an error if the file doesn't exist

```python
python load_json.py 1 2 3
```


