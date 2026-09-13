# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Phú Bình  
> **Mã Sinh Viên / Mã Học viên:** 2A202602410  
> **Chủ đề Lựa chọn:** Trợ lý học vụ VinUni – ReAct Agent tra cứu thông tin sinh viên và đặt lịch tư vấn  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | **5 / 5** | Bài toán đòi hỏi Agent phải hiểu intent, xác định việc cần tra cứu hoặc đặt lịch, rồi tổng hợp dữ liệu để đưa ra câu trả lời cuối cùng. Đó là ví dụ điển hình của suy luận nhiều bước. |
| **2. Tool Interaction** | **5 / 5** | Hệ thống cần truy cập dữ liệu thực tế thông qua MCP Server: tra cứu hồ sơ học vụ và đặt lịch hẹn tư vấn. Đây là dạng bài toán mà chat bot đơn thuần không thể xử lý tốt nếu không có Tool. |
| **3. Dynamic Decision** | **5 / 5** | Agent phải quyết định hành động theo ngữ cảnh: hỏi quy chế chung thì trả lời trực tiếp; cần tra cứu thông tin sinh viên thì gọi academic_query; cần đặt lịch thì gọi schedule_appointment. |
| **4. Long Horizon Goal** | **4 / 5** | Mục tiêu của hệ thống kéo dài từ nhận câu hỏi đến gọi Tool, quan sát dữ liệu, rồi đưa ra phản hồi cuối cùng. Hệ thống có tính liên tục, tuy nhiên quy mô dữ liệu và workflow còn ở mức demo. |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | *Bài toán rất phù hợp triển khai Agentic System vì có cả suy luận, hành động qua Tool, và phản hồi phụ thuộc vào dữ liệu thực tế.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (ĐÃ CHẠY THÀNH CÔNG TRÊN MÔI TRƯỜNG DEMO)

> Lưu ý: Trong môi trường hiện tại, hệ thống đã kiểm thử thành công trong chế độ mock offline. Kết quả dưới đây là bằng chứng thực tế khi chạy `python src/app.py --all` và lưu log vào file [docs/trace_waterfall.json](docs/trace_waterfall.json).

Dán 1 đoạn trích xuất log tiêu biểu từ file [docs/trace_waterfall.json](docs/trace_waterfall.json):

```json
[
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
      }
    },
    "latency_ms": 0.33
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả tra cứu cho sinh viên SV2026001 (Nguyễn Văn An): Lớp AI-K4, GPA: 3.85, Email: an.nv@vinuni.edu.vn, Trạng thái: Đang học, Cố vấn: PGS.TS Nguyễn Văn A.",
    "latency_ms": 10.0
  }
]
```

### Giải thích trace log
- Bước 1: Agent phát sinh Action `academic_query`
- Bước 2: MCP Server trả về Observation chứa dữ liệu sinh viên thực tế
- Bước 3: Agent tổng hợp output cuối cùng dựa trên dữ liệu từ Tool, không bịa đặt

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- [x] Hệ thống đã chạy thành công trên môi trường demo với mô hình mock offline: `python src/app.py --all`.
- **Tổng số Test Cases đã chạy thành công:** **5 / 5 test cases**.
- **Số lượt gọi Tool qua MCP Server chính xác:** **4 lượt**.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

### Kết luận ngắn
- ReAct Agent đã thể hiện được khả năng suy luận và tương tác với Tools thông qua MCP Server.
- Cả 5 tình huống demo đã được thực thi trong quy trình ReAct: Thought → Action → Observation → Final Answer.
- Bài toán này phù hợp với mô hình Agentic AI và dễ minh họa trong Demo Day 3.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
