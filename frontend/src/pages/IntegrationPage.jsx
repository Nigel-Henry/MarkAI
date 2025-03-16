// frontend/src/pages/IntegrationPage.jsx
import React, { useState, useEffect } from 'react';
import MarkAi from 'markai-sdk';
import Prism from 'prismjs'; // مكتبة مجانية لتنسيق الأكواد
import 'prismjs/themes/prism-tomorrow.css'; // ستايل الأكواد

const IntegrationPage = () => {
  const [apiKey, setApiKey] = useState('');
  const [messages, setMessages] = useState([{ role: 'user', content: 'Hello MarkAi' }]);
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // أمثلة جاهزة للاستخدام
  const codeExamples = {
    basic: `const client = new MarkAi('YOUR_API_KEY');
client.chat([{role: 'user', content: 'Hello'}])`,
    advanced: `// Summarization Example
const summary = await client.summarize('Your long text...');`
  };

  useEffect(() => {
    Prism.highlightAll(); // تنسيق الأكواد تلقائيًا
  }, []);

  const handleTest = async () => {
    try {
      setLoading(true);
      const client = new MarkAi(apiKey);
      const result = await client.chat(messages);
      setResponse(result.choices[0].message.content);
    } catch (err) {
      setError('Error: Invalid API Key or Server Issue');
    } finally {
      setLoading(false);
    }
  };

  return (

    

    <div className="container mx-auto p-6">
      <h1 className="text-4xl font-bold mb-8">MarkAI Developer Integration</h1>
      
      {/* قسم توليد المفتاح */}
      <section className="mb-12 p-6 bg-gray-50 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4">🚀 Get Your API Key</h2>
        <div className="flex gap-4">
          <button className="btn-primary">Get Free Key</button>
          <button className="btn-premium">Upgrade to Pro</button>
        </div>
      </section>

      {/* قسم التوثيق التفاعلي */}
      <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="documentation">
          <h2 className="text-2xl font-semibold mb-4">📚 Documentation</h2>
          <pre className="language-javascript">
            <code>{codeExamples.basic}</code>
          </pre>
          
          <h3 className="text-xl mt-6 mb-3">Advanced Usage</h3>
          <pre className="language-javascript">
            <code>{codeExamples.advanced}</code>
          </pre>
        </div>

        {/* محاكي API تفاعلي */}
        <div className="playground p-6 bg-white rounded-lg shadow">
          <h2 className="text-2xl font-semibold mb-4">🧪 API Playground</h2>
          
          <div className="mb-4">
            <label className="block mb-2">API Key:</label>
            <input
              type="password"
              className="w-full p-2 border rounded"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
            />
          </div>

          <button 
            onClick={handleTest}
            className="btn-test"
            disabled={loading}
          >
            {loading ? 'Testing...' : 'Test Integration'}
          </button>

          {response && (
            <div className="mt-6 p-4 bg-green-50 rounded">
              <h3 className="font-bold mb-2">✅ Successful Response:</h3>
              <p>{response}</p>
            </div>
          )}

          {error && (
            <div className="mt-6 p-4 bg-red-50 rounded">
              <h3 className="font-bold mb-2">❌ Error:</h3>
              <p>{error}</p>
            </div>
          )}
        </div>
      </section>

      {/* قسم الأسعار */}
      <section className="mt-12">
        <h2 className="text-3xl font-bold mb-6">💎 Pricing Plans</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="pricing-card">
            <h3>Free Tier</h3>
            <ul>
              <li>100 requests/day</li>
              <li>Basic features</li>
            </ul>
          </div>
          <div className="pricing-card premium">
            <h3>Pro Plan</h3>
            <ul>
              <li>Unlimited requests</li>
              <li>Priority support</li>
            </ul>
          </div>
        </div>
      </section>
    </div>
  );
};

export default IntegrationPage;


