import redis

# إنشاء اتصال مع خادم Redis
cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cache(key):
    """
    استرجاع قيمة من الكاش باستخدام المفتاح المحدد.
    
    Args:
        key (str): المفتاح المستخدم لاسترجاع القيمة.
    
    Returns:
        القيمة المخزنة في الكاش أو None إذا لم يتم العثور على المفتاح.
    """
    try:
        return cache.get(key)
    except redis.RedisError as e:
        # التعامل مع خطأ Redis
        print(f"Error retrieving key {key} from cache: {e}")
        return None

def set_cache(key, value, expire=3600):
    """
    تخزين قيمة في الكاش باستخدام المفتاح المحدد ووقت انتهاء الصلاحية.
    
    Args:
        key (str): المفتاح المستخدم لتخزين القيمة.
        value (str): القيمة المراد تخزينها.
        expire (int): وقت انتهاء الصلاحية بالثواني (الافتراضي 3600 ثانية).
    """
    try:
        cache.set(key, value, ex=expire)
    except redis.RedisError as e:
        # التعامل مع خطأ Redis
        print(f"Error setting key {key} in cache: {e}")