Dozzle
Hosts
Hosts e Containers

548B/s
981B/s
06:08:42: Starting worker for 4 functions: job_translate_pdf, job_translate_docx, job_translate_epub, cron:cleanup_expired_jobs
2026-06-03 06:08:42,003 INFO [worker] — Starting worker for 4 functions: job_translate_pdf, job_translate_docx, job_translate_epub, cron:cleanup_expired_jobs
06:08:42: redis_version=7.4.8 mem_usage=1.04M clients_connected=1 db_keys=0
2026-06-03 06:08:42,004 INFO [worker] — redis_version=7.4.8 mem_usage=1.04M clients_connected=1 db_keys=0
2026-06-03 06:08:42,004 INFO [worker] — Worker iniciando — aquecendo modelos...
2026-06-03 06:08:43,403 INFO [worker] — Available Provider: CPUExecutionProvider
2026-06-03 06:08:43,994 INFO [worker] — [YOLO] CustomDocLayoutModel: conf=0.15 imgsz=1024
2026-06-03 06:08:43,994 INFO [worker] — [YOLO] Singleton inicializado: _CustomOnnxModel
2026-06-03 06:08:43,994 INFO [worker] — YOLO singleton aquecido: _CustomOnnxModel
2026-06-03 06:08:43,994 INFO [worker] — Worker pronto.
06:09:55:   0.48s → 998e46dfa6d54547a5085ce1eea186b2:job_translate_pdf(filename='document.pdf', glossario='', lang_in='Português', lang_out='Inglês', …)
2026-06-03 06:09:55,150 INFO [worker] —   0.48s → 998e46dfa6d54547a5085ce1eea186b2:job_translate_pdf(filename='document.pdf', glossario='', lang_in='Português', lang_out='Inglês', …)
2026-06-03 06:09:55,150 INFO [worker] — job_translate_pdf: document.pdf | Português→Inglês | fmt=pdf
2026-06-03 06:09:55,172 INFO [worker] — Métricas PDF v9.7: pages=3 scanned=False formulas=False fonts=4 img=0% drawings=19.7 table_density=0.0 colored=True x_var=0.203 decorative_fonts=False multi_col=True complex=True
2026-06-03 06:09:55,172 INFO [worker] — Engine: pdf2zh (layout complexo ou fórmulas)
2026-06-03 06:09:55,172 INFO [worker] — Engine: pdf2zh | 3 páginas
2026-06-03 06:09:55,822 INFO [worker] — Initializing cache database at /root/.cache/babeldoc/cache.v1.db
2026-06-03 06:09:57,549 INFO [worker] — [pdf2zh] Iniciando: pt → en | document.pdf
2026-06-03 06:09:57,588 INFO [worker] — start to translate: /tmp/tmpf_ab7mfs/document.pdf
2026-06-03 06:10:19,821 INFO [worker] — Found title paragraph: M I N U T A
2026-06-03 06:10:19,821 INFO [worker] — Found first title paragraph: M I N U T A
2026-06-03 06:10:21,708 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:22,255 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:22,629 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:22,673 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:23,870 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:24,529 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:25,223 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:26,034 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:26,889 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:27,147 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:27,396 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:27,781 WARNING [worker] — Translation result is too long or too short. Input: 4, Output: 1
2026-06-03 06:10:27,781 WARNING [worker] — Fallback to simple translation. paragraph id: uXqRV
2026-06-03 06:10:28,823 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:29,247 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:29,525 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:29,659 INFO [worker] — HTTP Request: POST https://openrouter.ai/api/v1/chat/completions "HTTP/1.1 200 OK"
2026-06-03 06:10:37,547 INFO [worker] — Translation completed. Total: 63, Successful: 62, Fallback: 1
2026-06-03 06:10:38,557 WARNING [worker] — [PARA DEBUG] scale=0.75 | bbox=(95.1x21.3) | text='M I N U T E S'
2026-06-03 06:10:38,561 WARNING [worker] — [PARA DEBUG] scale=0.60 | bbox=(51.0x9.7) | text='Minutes No. 55E9'
2026-06-03 06:10:38,565 WARNING [worker] — [PARA DEBUG] scale=0.75 | bbox=(77.3x8.2) | text='Generated on: 05/03/2026'
2026-06-03 06:10:38,569 WARNING [worker] — [PARA DEBUG] scale=0.90 | bbox=(109.3x9.7) | text='Ordinary General Meeting'
2026-06-03 06:10:38,571 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(78.4x9.7) | text='03/05/2026 · 17:58h'
2026-06-03 06:10:38,572 WARNING [worker] — [PARA DEBUG] scale=0.70 | bbox=(28.7x5.2) | text='LOCATION'
2026-06-03 06:10:38,577 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(125.0x41.2) | text='Party Room of the Residencial Parque das Acácias Condominium'
2026-06-03 06:10:38,587 WARNING [worker] — [PARA DEBUG] scale=0.80 | bbox=(72.4x8.2) | text='Name / Identification'
2026-06-03 06:10:38,588 WARNING [worker] — [PARA DEBUG] scale=0.95 | bbox=(38.3x5.7) | text='Signature'
2026-06-03 06:10:38,588 WARNING [worker] — [PARA DEBUG] scale=0.90 | bbox=(68.0x9.7) | text='João Carlos Silva'
2026-06-03 06:10:38,589 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(93.2x9.7) | text='Maria Aparecida Santos'
2026-06-03 06:10:38,590 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(95.7x9.7) | text='Pedro Henrique Oliveira'
2026-06-03 06:10:38,606 WARNING [worker] — [PARA DEBUG] scale=0.90 | bbox=(448.4x44.2) | text='The Ordinary General Assembly of the Parque das Acácias Resi'
2026-06-03 06:10:38,607 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(110.4x9.1) | text='AGENDA AND DISCUSSIONS'
2026-06-03 06:10:38,610 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(199.2x12.7) | text='1. Approval of the 2025 financial statements'
2026-06-03 06:10:38,617 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(175.0x12.7) | text='3. Replacement of the booster pumps'
2026-06-03 06:10:38,622 WARNING [worker] — [PARA DEBUG] scale=0.70 | bbox=(121.9x12.7) | text='4. Election of the governing body'
2026-06-03 06:10:38,628 WARNING [worker] — [PARA DEBUG] scale=0.80 | bbox=(290.0x11.8) | text='The financial statements for the 2025 fiscal year were unani'
2026-06-03 06:10:38,634 WARNING [worker] — [PARA DEBUG] scale=0.90 | bbox=(325.1x11.8) | text='João Carlos Silva was re-elected as trustee by acclamation f'
2026-06-03 06:10:38,639 WARNING [worker] — [PARA DEBUG] scale=0.70 | bbox=(186.5x11.8) | text='Pedro Henrique Oliveira was re-elected deputy superintendent'
2026-06-03 06:10:38,640 WARNING [worker] — [PARA DEBUG] scale=0.70 | bbox=(30.0x5.7) | text='DEADLINE'
2026-06-03 06:10:38,641 WARNING [worker] — [PARA DEBUG] scale=0.80 | bbox=(58.6x8.9) | text='hidro-systemas'
2026-06-03 06:10:38,643 WARNING [worker] — [PARA DEBUG] scale=0.80 | bbox=(195.4x11.8) | text='Execution of the replacement of the booster pumps.'
2026-06-03 06:10:38,644 WARNING [worker] — [PARA DEBUG] scale=0.75 | bbox=(27.2x9.9) | text='30 days'
2026-06-03 06:10:38,645 WARNING [worker] — [PARA DEBUG] scale=0.80 | bbox=(61.0x11.8) | text='Pedro Henrique'
2026-06-03 06:10:38,645 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(31.6x6.9) | text='Oliveira'
2026-06-03 06:10:38,647 WARNING [worker] — [PARA DEBUG] scale=0.80 | bbox=(197.5x11.8) | text='Monitoring the execution of the replacement of the'
2026-06-03 06:10:38,648 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(79.2x11.8) | text='recirculation pumps.'
2026-06-03 06:10:38,653 WARNING [worker] — [PARA DEBUG] scale=0.90 | bbox=(68.0x9.9) | text='João Carlos Silva'
2026-06-03 06:10:38,655 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(93.2x11.8) | text='Maria Aparecida Santos'
2026-06-03 06:10:38,656 WARNING [worker] — [PARA DEBUG] scale=0.90 | bbox=(57.6x8.4) | text='João Carlos Silva'
2026-06-03 06:10:38,657 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(78.8x10.0) | text='Maria Aparecida Santos'
2026-06-03 06:10:38,658 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(80.9x10.0) | text='Pedro Henrique Oliveira'
2026-06-03 06:10:38,661 WARNING [worker] — [PARA DEBUG] scale=0.95 | bbox=(193.2x21.1) | text='Automatically generated document · Minutes No 55E9 · 05/03/2'
2026-06-03 06:10:38,663 WARNING [worker] — [PARA DEBUG] scale=0.85 | bbox=(79.2x6.7) | text='MINUTES · DIGITAL MINUTES'
2026-06-03 06:10:38,663 WARNING [worker] — [SCALE DEBUG] lang=EN | mode_scale=1.0000 | floor=0.7800 | effective_mode=1.0000 | scales=[0.78, 0.8, 0.85, 0.9, 0.95, 1.0]
2026-06-03 06:10:38,663 WARNING [worker] — [SCALE DEBUG] após normalização | scales=[0.78, 0.8, 0.85, 0.9, 0.95, 1.0]
2026-06-03 06:10:40,379 INFO [worker] — PDF save with clean=False completed successfully
2026-06-03 06:10:40,419 INFO [worker] — Peak memory usage: 3948.24 MB
2026-06-03 06:10:40,419 INFO [worker] — finish translate: /tmp/tmpf_ab7mfs/document.pdf, cost: 42.830349922180176 s
2026-06-03 06:10:40,498 INFO [worker] — No TOC found in the original PDF, skipping migration.
2026-06-03 06:10:40,498 INFO [worker] — cleanup temp files: /tmp/tmp1kk68wk1
2026-06-03 06:10:40,499 INFO [worker] — [pdf2zh] Concluído: document.no_watermark.en.mono.pdf (782938 bytes)
2026-06-03 06:10:40,646 INFO [worker] — Upload Appwrite: traducao_ingles.pdf (751079 bytes)
2026-06-03 06:10:41,788 INFO [worker] — Upload concluído: https://appwrite.carlos-hub.duckdns.org/v1/storage/buckets/6a11c5da001385fbd570/
06:10:41:  46.64s ← 998e46dfa6d54547a5085ce1eea186b2:job_translate_pdf ● {'file_url': 'https://appwrite.carlos-hub.duckdns.org/v1/storage/buckets/6a11c5…
2026-06-03 06:10:41,788 INFO [worker] —  46.64s ← 998e46dfa6d54547a5085ce1eea186b2:job_translate_pdf ● {'file_url': 'https://appwrite.carlos-hub.duckdns.org/v1/storage/buckets/6a11c5…
