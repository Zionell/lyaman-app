const express = require('express');
const controller = require('../controllers');

const router = express.Router();

router.post('/request', controller.request);

module.exports = router;
