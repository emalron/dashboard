import redis
import time
import random
import json

# Redis 연결 설정
r = redis.Redis(host='localhost', port=6379, db=0)

while True:
    # 현재 시간
    current_time = int(time.time())

    # 가상의 서버 메트릭 생성
    cpu_usage = random.uniform(0, 100)
    memory_usage = random.uniform(0, 16000)  # MB
    network_traffic = random.uniform(0, 1000)  # Mbps

    # 데이터 포인트 생성
    data_point = {
        "timestamp": current_time,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "network_traffic": network_traffic
    }

    # Redis에 데이터 저장
    # 'server_metrics'라는 키에 JSON 형태로 데이터를 저장합니다
    r.lpush('server_metrics', json.dumps(data_point))

    # 최근 1000개의 데이터 포인트만 유지
    r.ltrim('server_metrics', 0, 999)

    print(f"Data inserted at {current_time}")

    # 5초 대기
    time.sleep(5)