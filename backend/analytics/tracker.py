from prometheus_client import Counter

REQUEST_COUNT = Counter('markai_requests', 'Total API requests')

def track_request():
    REQUEST_COUNT.inc()