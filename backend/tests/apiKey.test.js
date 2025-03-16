const ApiKeyService = require('../features/apiKey/apiKey.service');

describe('ApiKeyService', () => {
  test('should generate valid API key', () => {
    const apiKey = ApiKeyService.generateKey('user123', 'free');
    expect(apiKey).toHaveLength(64);
  });
});