# Combine Images
画像を格子状に並べて一枚の画像にするツール

## Installation
```
git clone https://github.com/eg-itn/combine_images.git
```

## Usage
```
usage: combine_images.py [-h] [-outputdir DIR]
                         inputdir grid_width grid_height

positional arguments:
    inputdir              input directory
    grid_width            grid width
    grid_height           grid height

optional arguments:
    -h, --help            show this help message and exit
    -outputdir DIR, --outputdir DIR
                            output directory
```

`inputdir`: 入力画像ディレクトリ  
`grid_width`: 横に並べる画像数  
`grid_height`: 縦に並べる画像数  
`outputdir`: 出力画像ディレクトリ（未指定時は入力ディレクトリに出力される）  

## Example
```
python combine_images.py inputdir 3 2
python combine_images.py inputdir 2 0  # 片方が0の場合は自動で計算される
```