import pytest

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 201),
    (2, 201),
    (None, 400)  # مثال على اختبار حالة فشل
])
def test_create_conversation(client, user_id, expected_status):
    """
    اختبار إنشاء محادثة جديدة باستخدام معرف المستخدم.
    """
    response = client.post('/api/conversations', json={'user_id': user_id})
    assert response.status_code == expected_status