<div align="center">

# gomoku-ttnt-group04

Caro/Gomoku 15x15 với AI Minimax + Alpha-Beta, giao diện React/Tailwind, kèm bridge Python (FastAPI) để phục vụ bản build và xuất API.

</div>

## Yêu cầu môi trường

- Node.js ≥ 18 và npm (đã cài đặt sẵn trên máy)
- Python ≥ 3.10 (chỉ cần nếu chạy bridge FastAPI)
- Trên Windows: nếu đường dẫn có ký tự Unicode, script build đã tự gắn tạm ổ đĩa ASCII để tránh lỗi Rollup; nếu vẫn lỗi hãy chuyển dự án sang thư mục không dấu rồi chạy lại.

## Hướng dẫn chạy sau khi tải và giải nén

1. Giải nén thư mục `gomoku-ttnt-group04` từ gói đã tải.
2. Mở terminal và chuyển vào thư mục dự án:
   ```bash
   cd path/to/gomoku-ttnt-group04
   ```
3. Cài phụ thuộc Node:
   ```bash
   npm install
   ```
4. Chạy chế độ phát triển (hot reload tại `http://localhost:5173`):
   ```bash
   npm run dev
   ```
5. Build sản phẩm (tạo `dist/` + kiểm tra TypeScript dự án):
   ```bash
   npm run build
   ```
6. Xem thử bản build sản phẩm:
   ```bash
   npm run preview
   ```
7. Chạy test AI/game logic:
   ```bash
   npm run test
   ```

## Chạy bridge Python (tùy chọn)

1. Đảm bảo đã có bản build: `npm run build`.
2. Cài phụ thuộc Python: `pip install -r python/requirements.txt`.
3. Chạy server:
   ```bash
   cd python
   uvicorn server:app --reload
   ```
4. Mở `http://127.0.0.1:8000` (phục vụ dist/ và các API `/api/status`, `/api/weights`, `/api/ping`).

## Tính năng nổi bật

- **Chơi mượt**: PvP & PvE, hoàn tác/làm lại, lịch sử nước đi, highlight đường thắng, đánh dấu nước cuối, gợi ý nước đi, tự lưu trận.
- **UI linh hoạt**: Zustand store, Tailwind animation, điều khiển bàn phím, toggle chủ đề, chế độ tương phản cao, âm thanh.
- **AI thông minh**: Negamax + Alpha-Beta với iterative deepening, bán kính ứng viên, sắp xếp nước, trọng số heuristic, chạy trong Web Worker.
- **Tài liệu & công cụ**: Hướng dẫn nhanh, template báo cáo/slide, script tinh chỉnh trọng số, bridge FastAPI để đáp ứng yêu cầu “có Python” mà không đụng logic TS.

## Ngăn xếp công nghệ

| Tầng | Công nghệ |
| --- | --- |
| Frontend | React 19 + TypeScript + Vite + Tailwind |
| State | Zustand + Web Worker (AI) |
| AI | Minimax (Negamax) + Alpha-Beta, heuristic patterns |
| Test | Vitest |
| Python bridge | FastAPI + Uvicorn (serve dist/ + expose AI metadata) |
| Docs | python-docx / python-pptx |

## Gợi ý sử dụng

- **Đánh cờ**: Click chuột hoặc phím mũi tên + Enter/Space (ô đang focus có ghost stone).
- **Gợi ý**: Nút “Gợi ý” gửi job sang worker, ô đề xuất sẽ tô xanh cho tới khi bị ghi đè.
- **Lưu/khôi phục**: Lưu vào `localStorage` với key `gomoku-ttnt-group04:save`.
- **Cấu hình PVE**: Chọn bên, người đi trước, độ khó (Easy depth2 ~0.4s, Medium depth3 ~1.2s, Hard depth5 ~2.5s). AI có thể đi trước hoặc đáp trả ngay.
- **Tùy chỉnh bàn**: Kích thước 5x5–19x19 (mặc định 15), độ dài thắng chỉnh được, bán kính xét ứng viên chỉnh được.

## Ghi chú AI

- **Search**: Negamax + Alpha-Beta, iterative deepening theo thời gian; dừng khi tìm thấy FIVE hoặc hết thời gian.
- **Ứng viên**: Gom cụm theo khoảng cách Manhattan (mặc định 2), bias vào giữa bàn khi trống.
- **Ordering**: Đánh giá nhẹ để ưu tiên đe dọa công/thủ trước khi mở rộng.
- **Patterns**: Trọng số OPEN_FOUR, CLOSED_THREE... nằm trong JSON, có thể import/export và chuyển qua lại giữa default/custom.
- **Cách ly**: AI chạy trong Web Worker, UI vẫn mượt và có log depth, nodes, duration, score.

## Cấu trúc thư mục

```
gomoku-ttnt-group04/
|-- public/weights.json        # trọng số heuristic mặc định/tuned
|-- src/
|   |-- ai/                    # types, patterns, heuristics, minimax, move generation
|   |-- components/            # Board, Sidebar, Controls, TopBar, MoveList
|   |-- game/                  # rules + Zustand store
|   |-- hooks/useAIController  # cầu nối Web Worker
|   |-- worker/aiWorker.ts     # entry worker chạy search
|-- tests/                     # vitest (win/eval/movegen/search)
|-- training/tune_weights.ts   # script tự chơi tinh chỉnh trọng số
|-- docs/                      # template báo cáo + slide
|-- guide/README_RUN.txt       # hướng dẫn chạy nhanh 3 bước
|-- python/                    # FastAPI bridge + requirements
```

## Lưu trữ & dữ liệu

- **Save/Restore**: điều khiển từ panel, lưu ở `localStorage` key `gomoku-ttnt-group04:save`.
- **Weights**: `public/weights.json`, có thể import/export và cache ở `gomoku-ttnt-group04:weights`.
- **Log tuning**: `training/log.csv` ghi lại từng epoch (win rate + snapshot JSON).

## Kiểm thử

- `tests/win.test.ts` - phát hiện thắng ngang/dọc/chéo.
- `tests/eval.test.ts` - thứ tự heuristic (OPEN_FOUR > OPEN_THREE > CLOSED_THREE ...).
- `tests/movegen.test.ts` - chọn biên mở rộng Manhattan đúng.
- `tests/search.test.ts` - regression để AI chặn tứ nước rõ ràng.

## Checklist bàn giao

- [x] PvP + PvE, bàn 5x5–19x19, undo/redo, highlight, gợi ý.
- [x] AI chặn/tạo four, chọn độ khó, worker tách biệt, hỗ trợ accessibility.
- [x] README tiếng Việt, hướng dẫn cài/chạy, template docs, script tuning, bridge Python tùy chọn.

Chúc bạn chơi vui và đạt điểm tối đa!
