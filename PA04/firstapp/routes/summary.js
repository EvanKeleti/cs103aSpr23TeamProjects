/*
    summary.js -- Router for the summary (group by category) page
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User');
const TransactionItem = require('../models/TransactionItem');

isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
}

router.get('/summary', async (req, res) => {
    const result = await TransactionItem.aggregate([
        { $group: { _id: '$category', totalAmount: { $sum: '$amount' } } },
        { $sort: { _id: 1} }
    ]);

    res.render('summary', { result });
});
module.exports = router