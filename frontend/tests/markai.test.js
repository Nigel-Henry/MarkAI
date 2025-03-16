// tests/markai.test.js
const MarkAi = require('../index');
const nock = require('nock');

describe('MarkAi', () => {
  let client;

  beforeAll(() => {
    client = new MarkAi({ apiKey: 'test-key' });
    nock('https://api.markai.com')
      .post('/v1/chat')
      .reply(200, {
        choices: [{ message: { content: 'Test response' } }]
      });
  });

  test('should return chat response', async () => {
    const response = await client.chat({
      messages: [{ role: 'user', content: 'Test' }]
    });
    expect(response.choices[0].message.content).toBe('Test response');
  });
});