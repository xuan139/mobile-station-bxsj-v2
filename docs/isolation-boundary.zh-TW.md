# BXSJ V2 隔離邊界

日期：2026-09-05
狀態：已建立空骨架，尚未實作業務功能

## 目的

將 BXSJ／鈉鹽從 Green V2 的程式、資料及部署生命週期完全分離，避免未來重寫時
再次形成同一倉庫、同一資料層或同一消息通道的耦合。

## 明確禁止

- 不與 Green V2 共用 Git 倉庫或 Python package。
- 不共用 PostgreSQL database、schema、角色或 migration。
- 不共用 RabbitMQ vhost、exchange、queue 或 consumer group。
- 不共用 AWS 部署目錄、systemd unit 或環境檔。
- 不把舊 `bxsj_protocol.py` 直接複製進本倉庫。

## 後續啟動條件

開始 BXSJ V2 業務開發前，須另外確認：設備協定、站台清單、資料模型、命令語意、
告警規則、安全邊界、模擬器、測試資料及切換／回退方式。

