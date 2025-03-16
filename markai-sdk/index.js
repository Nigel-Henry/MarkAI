class MarkAi {
    constructor(apiKey) {
      this.apiKey = apiKey;
      this.baseUrl = 'https://api.markai.com/v1';
    }
  
    async chat(messages) {
      const response = await fetch(`${this.baseUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.apiKey}`
        },
        body: JSON.stringify({ messages })
      });
      return response.json();
    }
  }
  
  module.exports = MarkAi;


class MarkAi {
    constructor(apiKey, config = {}) {
      this.apiKey = apiKey;
      this.baseUrl = config.baseUrl || 'https://api.markai.vercel.app';
      this.version = config.version || 'v1';
    }
  
    async _request(endpoint, method = 'GET', data = null) {
      const url = `${this.baseUrl}/${this.version}/${endpoint}`;
      const headers = {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      };
  
      const response = await fetch(url, {
        method,
        headers,
        body: data ? JSON.stringify(data) : null
      });
  
      if (!response.ok) {
        throw new Error(`API Error: ${response.statusText}`);
      }
  
      return response.json();
    }
  
    async chat(messages, options = {}) {
      return this._request('chat', 'POST', {
        messages,
        ...options
      });
    }
  
    async summarize(text, options = {}) {
      return this._request('summarize', 'POST', {
        text,
        ...options
      });
    }
  
    // إضافة المزيد من الوظائف حسب الحاجة
  }
  
  export default MarkAi;