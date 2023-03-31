# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import path

# font type
HAN_SERIF_TYPE    = 1
HANDWRITTEN_TYPE  = 2
CHILL_K_SANS_TYPE = 3

# metadata for font size
METADATA_FOR_HAN_SERIF = {
    "pinyin_canvas":{
        "width"    : 850,   # ピンイン表示部の幅
        "height"   : 283.3, # ピンイン表示部の高さ
        "base_line": 935,   # ベースラインからの高さ
        "tracking" : 22.145 # 拼音の標準空白幅： Tracking is about uniform spacing across a text selection.
    },
    "expected_hanzi_canvas":{
        "width" : 1000, # 基準にする漢字の表示部の幅
        "height": 1000, # 基準にする漢字の表示部の高さ
    },
    # ピンインが 5~6 文字以上(最大は6のはず)のとき、文字が重なることがある。この時にx軸を縮小して重なりを避けるモード
    "is_avoid_overlapping_mode": False, 
    "x_scale_reduction_for_avoid_overlapping": 0.1 # 上記のモードの際に x軸をどれだけ縮小するか
}

METADATA_FOR_HANDWRITTEN = {
    "pinyin_canvas":{
        "width"    : 800,   # ピンイン表示部の幅
        "height"   : 300, # ピンイン表示部の高さ
        "base_line": 920,   # ベースラインからの高さ
        "tracking" : 5 # 拼音の標準空白幅： Tracking is about uniform spacing across a text selection.
    },
    "expected_hanzi_canvas":{
        "width" : 1000, # 基準にする漢字の表示部の幅
        "height": 1000, # 基準にする漢字の表示部の高さ
    },
    # ピンインが 5~6 文字以上(最大は6のはず)のとき、文字が重なることがある。この時にx軸を縮小して重なりを避けるモード
    "is_avoid_overlapping_mode": True, 
    "x_scale_reduction_for_avoid_overlapping": 0.1 # 上記のモードの際に x軸をどれだけ縮小するか
}

METADATA_FOR_CHILL_K_SANS = {
    "pinyin_canvas":{
        "width"    : 1000, # The width of the canvas.
        "height"   : 300,  # The height of the canvas.
        "base_line": 850, # The height from the bottom of the Chinese character canvas to pinyin canvas.
        "tracking" : 10    # Character spacing in the pinyin display area (Tracking is about uniform spacing across a text selection).
    },
    "expected_hanzi_canvas":{
        "width" : 1200, # Expected Width of the Chinese character canvas.
        "height": 852, # Expected Height of the Chinese character canvas.
    },
    # When the Pinyin is 5-6 characters or more (up to a maximum of 6), there may be overlapping of characters.
    # This is a mode to reduce the x-axis scale to avoid overlapping.
    "is_avoid_overlapping_mode": True, 
    "x_scale_reduction_for_avoid_overlapping": 0.1 # How much to reduce the x-axis when in the above mode.
}


# using font name
HAN_SERIF_MAIN   = os.path.normpath( os.path.join(path.DIR_FONT_FOR_HAN_SERIF, "SourceHanSerifCN-Regular.ttf") )
HAN_SERIF_PINYIN = os.path.normpath( os.path.join(path.DIR_FONT_FOR_HAN_SERIF, "mplus-1m-medium.ttf") )

HAN_HANDWRITTEN_MAIN   = os.path.normpath( os.path.join(path.DIR_FONT_FOR_HANDWRITTEN, "XiaolaiMonoSC-without-Hangul-Regular.ttf") )
HAN_HANDWRITTEN_PINYIN = os.path.normpath( os.path.join(path.DIR_FONT_FOR_HANDWRITTEN, "latin-alpabet-of-SetoFont-SP.ttf") )

CHILL_K_SANS_MAIN   = os.path.normpath( os.path.join(path.DIR_FONT_FOR_CHILL_K_SANS, "Chill-K-Sans.otf") )
CHILL_K_SANS_PINYIN = os.path.normpath( os.path.join(path.DIR_FONT_FOR_CHILL_K_SANS, "mplus-1m-medium.ttf") )
