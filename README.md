# SRC808

**Per-App Volume Control for macOS**

SRC808 gives you independent volume sliders for each app on your Mac — seamless integration, zero compromises. Intercepts each app's audio stream before it hits the system mixer, giving you per-app volume with no quality loss.

**[Download Latest App Release](https://github.com/0xlab-co/SRC808/releases/latest)**

---

## What It Does

- **Free Core Features**:
  - **Per-App Volume**: Spotify at 80%, Discord at 40%, YouTube at 60% — all simultaneously and independently.
  - **Seamless Volume Keys**: Perfectly integrates with your Mac's native volume keys, automatically adjusting to your active output device.
  - **DDC Display Support**: Controls external monitor volume directly — no need for the display's OSD menu.
  - **Volume HUD**: A sleek overlay at the bottom of your screen shows the current device and volume whenever you press a volume key.
  - **Volume Memory**: Remembers each app's volume per output device. Switch from headphones to speakers — volumes restore automatically.

- **Pro Features** (Currently Free in Public Beta):
  - **Mini Media Controller**: A sleek now-playing panel inside SRC808. See current track info, album art, and control Spotify or Apple Music without ever switching windows.

---

## Changelog

### v1.4.1 Beta (2026-03-11)
- **In-App Update Notifications** — SRC808 now automatically checks for the latest GitHub releases. A green "UPDATE" pill appears when a new version is ready.
- **30-Day Pro Trial** — Added a 30-day free trial for all Pro features. View remaining days in Preferences and license status in the header.
- **External Display Mute Fix** — Resolved an issue where muting an external monitor (via HDMI/DP) failed to stop the audio.
- **Mini Media Controller Sync** — Fixed track info persistence after closing Spotify or Apple Music.
- **0% Volume Visual Fix** — UI now correctly triggers the mute icon when the slider is dragged to 0%.

### v1.4 Beta (2026-03-08)

### v1.2 (2026-03-02)
- **Volume keys follow current output** — supports Bluetooth headphones, USB DACs, and external displays.
- **Configurable volume steps** — set the step size per key press (1% to 25%) in Preferences.
- **New volume HUD** — redesigned on-screen display matches the app's style, showing at the bottom of the screen.

### v1.1 (2026-03-01)
- **Bluetooth & AirPlay device support** — identifies and controls Bluetooth and network audio output devices.
- **Launch at Login** — can be toggled in Preferences.
- **Persistent volume memory** — per-app, per-device volume settings are automatically saved and restored across restarts.
- **Driver status prompt** — shows an inline status indicator directly in the header when approval is required.

### v1.0 (2025)
- **The best tool is the one you never notice.**
- Ever broken your flow just to lower background music or mute a notification? We couldn't find that "just right" perfect solution, so we decided to build it ourselves.
- No flashy features. It simply blends into the system and works quietly in the background.
- Keep background music in the background and volume control effortless, so you can keep 100% of your focus on what truly matters.

---

## Licensing (SRC808-v1.4.1-beta-pro)
**Currently in Public Beta Testing**

SRC808 is currently in its Public Beta phase. During this period, you can enjoy a **30-day free trial** of all advanced Pro media tools. The core volume mixing capabilities will remain permanently free.

While final pricing and the exact split between Free and Pro are not yet finalized, **we can promise you one thing: SRC808 Pro will never be a subscription.** It will definitely be a one-time purchase. For now, start your trial to experience the full potential of SRC808!

---

## Privacy & Security
- **100% Local Processing**: All audio routing and processing happens exclusively on your Mac. No audio data is ever recorded, and no data is ever uploaded to any cloud service.
- **Permissions Explained**: 
  - **Microphone Access**: Required only to capture audio streams from other apps for independent routing. SRC808 does not listen to your physical environment.
  - **System Extension**: Required for high-performance, low-latency audio mixing at the system level.
- **No Tracking**: SRC808 contains no third-party analytics, tracking pixels, or advertisements.

---

## Before you install
- macOS Sonoma 14.2 or later
- Apple Silicon or Intel Mac
- One-time system extension approval in System Settings → Privacy & Security
- Microphone permission (required for audio capture)

## Feedback and Support
If you encounter any issues or have feature requests, please use the provided Issue templates:
- [Report a Bug](https://github.com/0xlab-co/SRC808/issues/new?template=bug_report.md)
- [Request a Feature](https://github.com/0xlab-co/SRC808/issues/new?template=feature_request.md)

Alternatively, you can reach out via email: [0xlab.co+src808@gmail.com](mailto:0xlab.co%2Bsrc808@gmail.com)

---
---

# SRC808 (繁體中文)

**為 macOS 打造的各 App 獨立音量控制**

SRC808 讓你能獨立調整 Mac 上每個應用程式的音量 — 無縫整合，不用妥協。在音訊進入系統混音器前攔截音訊流，為你帶來不損失音質的獨立音量控制。

**[下載最新版本 App](https://github.com/0xlab-co/SRC808/releases/latest)**

---

## 功能介紹

- **免費核心功能**:
  - **各 App 獨立音量 (Per-App Volume)**: Spotify 80%、Discord 40%、YouTube 60% — 同時並獨立調整。
  - **無縫音量鍵支援 (Seamless Volume Keys)**: 完美整合 Mac 原生音量鍵，並自動對齊目前正在使用的輸出裝置。
  - **支援外接螢幕 DDC (DDC Display Support)**: 直接控制外接顯示器的音量 — 不需要再按螢幕上的選單按鈕。
  - **音量提示 HUD (Volume HUD)**: 每次按下音量鍵時，螢幕底部會出現精美的提示，顯示當前裝置與音量。
  - **各裝置音量記憶 (Volume Memory)**: 為每一台輸出裝置記憶個別 App 的音量配置。從耳機切換到喇叭時，自動恢復設定。

- **Pro 專業功能** (公測期間免費開放):
  - **迷你媒體控制器 (Mini Media Controller)**: 內建在 SRC808 面板中的精緻播放列。免切換視窗，即可查看 Spotify 或 Apple Music 的播放資訊、專輯封面與控制播放。

---

## 更新日誌 (Changelog)

### v1.4.1 Beta (2026-03-11)
- **內建版本更新通知**——自動檢查 GitHub 的最新版本，釋出時會在面板頂部顯示「UPDATE」提示。
- **Pro 專業版 30 天免費試用**——新增 Pro 試用機制，可在偏好設定查看剩餘天數與授權狀態。
- **修復外接螢幕靜音失效問題**——解決 HDMI/DP 外接螢幕按下靜音鍵後聲音仍持續外放的問題。
- **修正 Mini Media Controller 資訊殘留**——確保播放控制器資訊與音樂 App 實際運行狀態同步。
- **音量歸零視覺修正**——修復音量拉至 0% 時未正確觸發靜音圖示的問題。

### v1.4 Beta (2026-03-08)

### v1.2 (2026-03-02)
- **音量鍵跟隨當前輸出裝置**——支援藍牙耳機、USB DAC 及外接螢幕。
- **可自定音量步幅**——在偏好設定中設定每次按鍵增減幅度（1%～25%）。
- **全新音量 HUD**——重新設計的提示介面，與 App 風格一致，顯示於螢幕底部。

### v1.1 (2026-03-01)
- **藍牙與 AirPlay 裝置支援**——識別並控制藍牙及網路音訊輸出裝置。
- **登入時自動啟動**——可在偏好設定中切換。
- **重啟後保留音量設定**——每個 App 在每個裝置上的音量設定均自動儲存與還原。
- **驅動程式狀態提示**——需要批准時，在標題列顯示內嵌狀態提示。

### v1.0 (2025)
- **最好的工具，是讓你『感覺不到它的存在』**
- 想要調低後台音樂、靜音系統通知，卻總被打斷了工作節奏。因為找不到那款「剛剛好」的完美解法，我們決定自己動手做
- 它沒有花俏的功能，只為純粹地融入系統、默默在背景運作
- 讓背景音樂不再喧賓奪主、讓聲音的控制變得理所當然，幫你將 100% 的精力留給真正重要的事

---

## 授權 (Licensing - SRC808-v1.4.1-beta-pro)
**目前處於公開 Beta 測試階段**

SRC808 目前正處於公開測試（SRC808-v1.4.1-beta-pro）階段。在測試期間，我們提供 **30 天的 Pro 進階功能免費試用**。核心的各 App 音量控制功能將永久免費提供。

最終售價與 Free / Pro 版本間的詳細功能差異尚未定案，但**我們能保證一件事：SRC808 Pro 絕對不會採用訂閱制。** 將會是一次性買斷的服務。現在，立即啟動您的試用，盡情體驗 SRC808 的完整功能，如果有任何建議，隨時歡迎與我們分享！

---

## 隱私與安全 (Privacy & Security)
- **100% 在地化處理**：所有音訊路由與處理程序均完全在您的 Mac 本機上執行。我們絕不錄音，也絕不將任何音訊資料上傳至任何雲端服務。
- **權限說明**：
  - **麥克風權限**：僅用於擷取其他應用程式的音訊流以實現獨立控制。SRC808 絕不會聆聽或記錄您的環境語音。
  - **系統延伸功能**：用於在系統層級實現高效能、低延遲的音訊混音。
- **無追蹤與廣告**：SRC808 內不包含任何第三方分析工具、追蹤器或廣告代碼。

---

## 安裝前須知
- macOS Sonoma 14.2 及其後版本
- 支援 Apple Silicon (M系列) 或 Intel 晶片 Mac
- 需於 系統設定 → 隱私權與安全性 完成一次性系統延伸功能授權
- 需要麥克風權限（用以擷取音訊）

## 意見回饋與援助
如果您遇到任何問題，或有新功能許願，歡迎透過內建的 Issue 範本提出：
- [回報問題 (Report a Bug)](https://github.com/0xlab-co/SRC808/issues/new?template=bug_report.md)
- [許願新功能 (Request a Feature)](https://github.com/0xlab-co/SRC808/issues/new?template=feature_request.md)

或者，您也可以透過電子郵件與我們聯繫：[0xlab.co+src808@gmail.com](mailto:0xlab.co%2Bsrc808@gmail.com)
