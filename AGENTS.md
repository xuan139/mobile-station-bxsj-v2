# BXSJ V2 Agent 規則

## 專案邊界

- 本倉庫只保留 BXSJ／鈉鹽 V2 的獨立開發邊界。
- 禁止 import 或複製綠能 V2 與既有綠能程式。
- 舊系統 `/Users/lijiaxi/Documents/mobile station` 只能唯讀參考。
- 禁止連線既有 AWS、PostgreSQL、RabbitMQ、設備或 WPF。
- 在使用者另行確認前，不實作、部署或啟動 BXSJ 業務功能。

## 工作規則

修改、提交、推送或部署前，必須執行並報告：

```text
pwd
git rev-parse --show-toplevel
git branch --show-current
git status --short --branch
```

- 寫入型 Agent 必須使用獨立 Git worktree 與 `codex/` 分支。
- GitHub 建立、push、AWS 部署及任何外部寫入必須取得使用者明確確認。
- 不得與 Green V2 共用資料庫、schema、MQ vhost、queue、憑證或部署目錄。
- 已確認方法、測試結果及部署結果必須以繁體中文記錄於 `docs/`。

