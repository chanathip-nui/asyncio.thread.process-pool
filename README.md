# Python Concurrency: Dynamic Programming (Coin Change)

จัดทำโดย
นายชนาธิป นุ้ยสี 6810110566

โปรเจกต์นี้เป็นการทดสอบและเปรียบเทียบการทำงานของ Concurrency ในภาษา Python ผ่านการแก้ปัญหาคณิตศาสตร์ด้วยวิธี **Dynamic Programming (DP)** โดยโจทย์คือการหาจำนวนเหรียญที่น้อยที่สุดในการทอนเงิน (Coin Change Problem) ซึ่งมีเหรียญให้เลือกใช้คือ `[4, 3, 1]` 

โปรเจกต์นี้ประกอบด้วยวิธีการรันงานพร้อมกัน 3 รูปแบบ เพื่อเปรียบเทียบประสิทธิภาพในการจัดการงาน (CPU-bound task)

1. **`my_asyncio.py` (Asyncio + ProcessPoolExecutor)**
   * ใช้ไลบรารี `asyncio` ร่วมกับ `ProcessPoolExecutor` เพื่อรันงานแบบ Asynchronous และเลี่ยงข้อจำกัดของ GIL (Global Interpreter Lock) ใน Python
   * เหมาะสำหรับงานที่ต้องการควบคุม Flow แบบ Async แต่ยังต้องการพลังการประมวลผลแบบ Multi-core

2. **`my_multi.py` (Multiprocessing Pool)**
   * ใช้ไลบรารี `multiprocessing` รันงานแบบขนาน แยกกันคนละ Process
   * **จุดเด่น:** มีการคำนวณตาราง DP (`build_dp_table`) ไว้ล่วงหน้าเพียงครั้งเดียว แล้วส่งตารางนี้ไปให้แต่ละ Worker ใช้งาน ทำให้ประหยัดทรัพยากรการคำนวณซ้ำซ้อนได้ดีที่สุดใน 3 ไฟล์นี้

3. **`my_thread.py` (ThreadPoolExecutor)**
   * ใช้ไลบรารี `threading` (ผ่าน `concurrent.futures.ThreadPoolExecutor`) รันงานแบบ Concurrency 
   * เนื่องจากงานนี้เป็นแบบ CPU-bound การใช้ Thread ใน Python อาจไม่ได้ทำให้เร็วขึ้นมากนักเมื่อเทียบกับ Process เพราะติดข้อจำกัดของ GIL 

วิธีการรันโปรแกรม

โปรเจกต์นี้เขียนด้วย Python มาตรฐาน (Standard Library) ไม่จำเป็นต้องติดตั้งไลบรารีภายนอกเพิ่มเติม สามารถรันผ่าน Command Line หรือ Terminal ได้เลย:

```bash
# รันรูปแบบ Asyncio
python my_asyncio.py

# รันรูปแบบ Multiprocessing
python my_multi.py

# รันรูปแบบ Threading
python my_thread.py
