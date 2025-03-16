import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Chat = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [conversations, setConversations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // جلب المحادثات السابقة من localStorage أو الخادم
  useEffect(() => {
    const fetchConversations = async () => {
      setLoading(true);
      setError('');

      try {
        // جلب المحادثات من localStorage إذا كانت موجودة
        const cachedConversations = localStorage.getItem('conversations');
        if (cachedConversations) {
          setConversations(JSON.parse(cachedConversations));
        }

        // جلب المحادثات من الخادم
        const response = await axios.get('http://localhost:5000/api/conversations');
        setConversations(response.data);
        localStorage.setItem('conversations', JSON.stringify(response.data));
      } catch (error) {
        console.error('Error fetching conversations:', error);
        setError('حدث خطأ أثناء جلب المحادثات السابقة. الرجاء المحاولة مرة أخرى.');
      } finally {
        setLoading(false);
      }
    };

    fetchConversations();
  }, []);

  const handleSend = async () => {
    if (!input.trim()) {
      setError('الرجاء إدخال رسالة.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const response = await axios.post('http://localhost:5000/api/generate/text', { text: input });
      const newMessages = [...messages, { text: input, sender: 'user' }, { text: response.data.result, sender: 'bot' }];
      setMessages(newMessages);
      setInput('');

      // حفظ المحادثة في localStorage
      localStorage.setItem('currentConversation', JSON.stringify(newMessages));

      // حفظ المحادثة في الخادم
      await axios.post('http://localhost:5000/api/conversations/save', {
        conversation: JSON.stringify(newMessages),
      });
    } catch (error) {
      console.error('Error sending message:', error);
      setError('حدث خطأ أثناء إرسال الرسالة. الرجاء المحاولة مرة أخرى.');
    } finally {
      setLoading(false);
    }
  };

  const handleNewConversation = () => {
    setMessages([]);
    localStorage.removeItem('currentConversation');
  };

  const handleCopyMessage = (text) => {
    navigator.clipboard.writeText(text);
    alert('تم نسخ الرسالة إلى الحافظة!');
  };

  const handleSaveConversation = () => {
    const blob = new Blob([JSON.stringify(messages, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'conversation.json';
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="flex h-screen bg-gray-50 p-8">
      {/* قائمة المحادثات السابقة */}
      <div className="w-1/4 bg-white rounded-lg shadow p-4">
        <h2 className="text-xl font-bold mb-4">المحادثات السابقة</h2>
        <button
          onClick={handleNewConversation}
          className="w-full bg-blue-500 text-white p-2 rounded mb-4"
        >
          محادثة جديدة
        </button>
        <ul>
          {conversations.map((conv, index) => (
            <li key={index} className="p-2 border-b">
              <button
                onClick={() => setMessages(JSON.parse(conv[2]))}
                className="text-left w-full"
              >
                المحادثة {index + 1}
              </button>
            </li>
          ))}
        </ul>
      </div>

      {/* واجهة المحادثة */}
      <div className="flex-1 ml-8 bg-gray-100 rounded-lg p-4">
        <div className="mb-4 h-64 overflow-y-auto">
          {messages.map((msg, index) => (
            <div key={index} className={`mb-2 ${msg.sender === 'user' ? 'text-right' : 'text-left'}`}>
              <div
                className={`inline-block p-2 rounded ${
                  msg.sender === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200'
                }`}
              >
                {msg.text}
                <button
                  onClick={() => handleCopyMessage(msg.text)}
                  className="ml-2 text-sm text-gray-500 hover:text-gray-700"
                >
                  نسخ
                </button>
              </div>
            </div>
          ))}
        </div>
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            className="flex-1 p-2 border rounded"
            placeholder="اكتب رسالتك..."
          />
          <button
            onClick={handleSend}
            disabled={loading}
            className={`bg-blue-500 text-white p-2 rounded ${
              loading ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 text-white'
            }`}
          >
            {loading ? 'جاري الإرسال...' : 'إرسال'}
          </button>
          <button
            onClick={handleSaveConversation}
            className="bg-green-500 text-white p-2 rounded"
          >
            حفظ المحادثة
          </button>
        </div>
        {error && <p className="text-red-500 mt-2">{error}</p>}
      </div>
    </div>
  );
};

export default Chat;