const express = require('express');
const router = express.Router();
const ApiKeyService = require('./apiKey.service');

router.post('/generate', async (req, res) => {
  const { userId, plan } = req.body;
  const apiKey = await ApiKeyService.generateKey(userId, plan);
  res.json({ apiKey });
});

module.exports = router;