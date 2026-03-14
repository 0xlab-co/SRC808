# SRC808

**All your audio apps. One control panel on macOS.**

SRC808 brings the audio apps currently running on your Mac and your output devices into one menu bar panel, so you can check, adjust, and manage everything without constantly switching between windows.

**[Download Latest App Release](https://github.com/0xlab-co/SRC808/releases/latest)**

---

## What It Does

- **Free Core Features**:
  - **App Volume Control**: Keep Spotify at 80%, Discord at 40%, and YouTube at 60% from one panel without jumping between apps.
  - **Keyboard Volume for External Displays**: When your audio is coming from a supported external display, your Mac's volume keys can control the display directly.
  - **Volume HUD**: A clean on-screen panel shows the current output device and volume whenever you press a volume key.
  - **Per-Device Volume Memory**: SRC808 remembers the levels you use for each app on different output devices, so switching back from headphones to speakers does not mean starting over.

- **Pro Features** (Currently Free in Public Beta):
  - **Mini Media Controller**: See what is playing in Spotify or Apple Music right inside SRC808, then pause, skip, or resume without leaving the panel.

---

## Changelog

### v1.5.2 Beta (2026-03-14)
- **Fixed launch issues on macOS 14 and older Intel Macs** — Updated the first-launch and feature unlock flow to prevent cases where the app could close immediately or fail to open normally on some machines.

### v1.4 Beta (2026-03-08)
- **Mini Media Controller (Pro)** — See what's playing in Spotify or Apple Music directly inside SRC808. Includes track info, cover art, and playback controls.
- **Stealth Volume HUD & Interface** — SRC808's beautiful volume indicator replaces the native macOS volume HUD, with a more polished preferences experience.
- **Flawless Bluetooth Audio** — Fixed an issue where volume adjustments on AirPods and other Bluetooth headphones might be unbalanced.
- **Rock-solid Stability** — Optimized first-time setup, resolved rare crashes, and improved overall stability for newer macOS updates.

### v1.2 (2026-03-02)
- **Support keyboard shortcuts for external display volume** — when audio is playing through a supported external display, you can control the display volume directly with your keyboard volume keys.
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

## Licensing (SRC808-v1.5.2-beta-pro)
**Currently in Public Beta Testing**

SRC808 is currently in the public beta phase (`SRC808-v1.5.2-beta-pro`). During this period, we provide a **30-day free trial** of Pro features, currently including the Mini Media Controller. After the trial ends, the core per-app volume controls will remain permanently free.

While final pricing and the exact split between Free and Pro are not yet finalized, **we can promise you one thing: SRC808 Pro will never be a subscription.** It will be a one-time purchase.

### Repository Notice
This repository is provided for official product information, release notes, and download guidance.
All rights reserved unless otherwise stated.

---

## Privacy & Security
- **100% Local Processing**: All audio routing and processing happens exclusively on your Mac. No audio data is ever recorded, and no data is ever uploaded to any cloud service.
- **Permissions Explained**:
  - **System Extension**: Required for low-latency audio control at the system level.
  - **Apple Events**: Requested only if you want Spotify / Apple Music integration in Mini Media Controller.
  - **Media Key Access**: Used only for SRC808's volume HUD and keyboard-based control on supported output devices.
- **No Tracking**: SRC808 contains no third-party analytics, tracking pixels, or advertisements.

---

## Before you install
- macOS Sonoma 14.2 or later
- Apple Silicon or Intel Mac
- One-time system extension approval in System Settings → Privacy & Security
- Apple Events permission only if you want Spotify / Apple Music integration in Mini Media Controller

## Feedback and Support
If you encounter any issues or have feature requests, please use the provided Issue templates:
- [Report a Bug](https://github.com/0xlab-co/SRC808/issues/new?template=bug_report.md)
- [Request a Feature](https://github.com/0xlab-co/SRC808/issues/new?template=feature_request.md)

Alternatively, you can reach out via email: [0xlab.co+src808@gmail.com](mailto:0xlab.co%2Bsrc808@gmail.com)

---
---

# SRC808 (繁體中文)

**把所有音訊 App，集中在同一個控制面板。**

SRC808 會把目前 Mac 上正在運作的音訊 App 與輸出裝置整理到同一個選單列面板裡，讓你不用來回切換視窗，就能直接查看、調整與管理。

**[下載最新版本 App](https://github.com/0xlab-co/SRC808/releases/latest)**

---

## 功能介紹

- **免費核心功能**:
  - **控制個別 App 音量 (Per-App Volume)**: 在同一個面板裡直接調整 Spotify、Discord、YouTube 等不同 App 的音量，不用來回切換視窗。
  - **用鍵盤直接控制外接螢幕音量**: 當聲音輸出到支援的外接螢幕時，可直接使用 Mac 鍵盤上的音量鍵調整螢幕音量。
  - **音量提示 HUD (Volume HUD)**: 按下音量鍵時，螢幕底部會顯示目前輸出裝置與音量。
  - **各裝置音量記憶 (Volume Memory)**: SRC808 會記住你在不同輸出裝置上的各自 App 慣用音量，切回原本裝置時不用重調。

- **Pro 專業功能** (公測期間免費開放):
  - **迷你媒體控制器 (Mini Media Controller)**: 直接在 SRC808 面板內查看 Spotify 或 Apple Music 的播放內容並控制播放，無需切換視窗。

---

## 更新日誌 (Changelog)

### v1.5.2 Beta (2026-03-14)
- **修正 macOS 14 與舊款 Intel Mac 的啟動問題**——調整首次啟動與功能解鎖流程，解決部分裝置上可能直接關閉或無法正常開啟的情況。

### v1.4 Beta (2026-03-08)
- **Mini Media Controller (Pro)**——直接在 SRC808 面板內查看 Spotify 或 Apple Music 的現正播放資訊，包含封面與播放控制。
- **專屬音量 HUD 與介面優化**——音量提示現在能取代系統原生的音量圖示，同時也優化了偏好設定的互動流程與待機應用程式顯示。
- **修正藍牙立體聲**——解決了在 AirPods 或藍牙耳機上調整音量時，可能出現左右聲道些微不平衡的問題。
- **整體穩定性提升**——優化首次解鎖功能時的權限請求流程，修復少見的閃退錯誤，提升整體穩定度與相容性。

### v1.2 (2026-03-02)
- **支援鍵盤快捷鍵調整外接螢幕音量**——當聲音輸出到支援的外接螢幕時，可直接用鍵盤音量鍵控制螢幕音量。
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

## 授權 (Licensing - SRC808-v1.5.2-beta-pro)
**目前處於公開 Beta 測試階段**

SRC808 目前正處於公開測試（SRC808-v1.5.2-beta-pro）階段。在測試期間，我們提供 **30 天的 Pro 功能免費試用**，目前包含 Mini Media Controller。試用期結束，核心的各 App 音量控制功能將永久免費提供。

最終售價與 Free / Pro 版本間的詳細功能差異尚未定案，但**我們能保證一件事：SRC808 Pro 絕對不會採用訂閱制。** 將會是一次性買斷的服務。

### Repository 說明
此 repository 主要提供官方產品資訊、更新日誌與下載指引。
除另有說明外，相關內容均保留所有權利。

---

## 隱私與安全 (Privacy & Security)
- **100% 在地化處理**：所有音訊路由與處理程序均完全在您的 Mac 本機上執行。我們絕不錄音，也絕不將任何音訊資料上傳至任何雲端服務。
- **權限說明**：
  - **系統延伸功能**：用於在系統層級提供低延遲音訊控制。
  - **Apple Events**：只在您要使用 Mini Media Controller 的 Spotify / Apple Music 整合時才會請求。
  - **多媒體按鍵權限**：只用來顯示 SRC808 的音量 HUD，以及在支援的輸出裝置上使用鍵盤進行音量控制。
- **無追蹤與廣告**：SRC808 內不包含任何第三方分析工具、追蹤器或廣告代碼。

---

## 安裝前須知
- macOS Sonoma 14.2 及其後版本
- 支援 Apple Silicon (M系列) 或 Intel 晶片 Mac
- 需於 系統設定 → 隱私權與安全性 完成一次性系統延伸功能授權
- 若要使用 Mini Media Controller 的 Spotify / Apple Music 整合，需額外允許 Apple Events

## 意見回饋與援助
如果您遇到任何問題，或有新功能許願，歡迎透過內建的 Issue 範本提出：
- [回報問題 (Report a Bug)](https://github.com/0xlab-co/SRC808/issues/new?template=bug_report.md)
- [許願新功能 (Request a Feature)](https://github.com/0xlab-co/SRC808/issues/new?template=feature_request.md)

或者，您也可以透過電子郵件與我們聯繫：[0xlab.co+src808@gmail.com](mailto:0xlab.co%2Bsrc808@gmail.com)
