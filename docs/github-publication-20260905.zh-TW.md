# BXSJ V2 GitHub 建立與首次推送記錄

日期：2026-09-05
執行帳號：`xuan139`
Repository：`xuan139/mobile-station-bxsj-v2`
URL：`https://github.com/xuan139/mobile-station-bxsj-v2`
可見性：Private
預設分支：`main`

## 本機來源

- 路徑：`/Users/lijiaxi/Documents/mobile-station-bxsj-v2`
- 獨立 Git：`/Users/lijiaxi/Documents/mobile-station-bxsj-v2/.git`
- Remote：`origin = https://github.com/xuan139/mobile-station-bxsj-v2.git`

## 首次推送內容

- `main`：`9b3743b`，BXSJ V2 隔離空骨架。
- `dev`：首次推送時為 `9169e25`，另含 macOS 系統檔案忽略規則。
- Tags：`bxsj-v2-isolation-r1`、`bxsj-v2-stage0-local-r1`。

## 建立與推送命令

```bash
gh repo create xuan139/mobile-station-bxsj-v2 --private --source=. --remote=origin
git push -u origin main
git push -u origin dev
git push origin --tags
```

## 驗證結果

- GitHub repository 顯示為 `PRIVATE`。
- 預設分支為 `main`。
- 本機 `main`／`dev` 已設定追蹤 `origin/main`／`origin/dev`。
- Green V2 與舊綠能 remote、分支及內容均未修改。

## 未執行事項

- 未搬入任何舊 BXSJ 業務程式。
- 未連線或修改 BXSJ AWS、資料庫、MQ、服務或設備。
- 未建立 Pull Request、branch protection 或 GitHub Actions secret。

