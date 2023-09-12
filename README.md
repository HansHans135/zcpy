# zcpy
中文程式(無聊做的)

# 使用
## 基本語法
- 用[ ]框起來的表示變數,實際使用時不需要添加
- 必須在每具後面加上 `,` 在判斷式結束時要加 `.`
```txt
顯示 [內容],
輸入 [變數],
如果 [內容] 等於 [內容],
如果 [內容] 不等於 [內容],
等待 [秒],
計算 [計算],

```

- 如果語法
```txt
如果 [內容] 等於 [內容],
顯示 動作1,
顯示 動作結束.
```

## 上手
- 參考並修改`test.zh`
```txt
顯示 請輸入密碼:,
輸入 passwd,

如果 passwd 等於 1234,
顯示 密碼正確.

如果 passwd 不等於 1234,
顯示 密碼錯誤.

```
修改完成後啟動`main.py`