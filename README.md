# BXSJ V2

本專案是 BXSJ／鈉鹽系統的獨立預留倉庫，目前只建立隔離規則與可驗證的
Python 套件骨架，不包含既有 BXSJ 程式或正式業務功能。

## 現階段原則

- 與 Green V2 使用不同 Git 倉庫。
- 不連線任何既有 AWS、資料庫、MQ 或真實設備。
- 不共用 Green V2 Python package、資料表或消息契約。
- 後續實作前須先建立專屬需求、協定、資料及驗收文件。

## 驗證

```bash
python3 -m unittest discover -s tests -v
```

