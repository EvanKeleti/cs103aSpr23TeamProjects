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
        { $match: { userid: {userId:req.user._id} } },
        { $group: { _id: '$category', totalAmount: { $sum: '$amount' } } },
        { $sort: { totalAmount: -1} },
        { $project: { category: '$_id', totalAmount: 1, _id: 0 } }
    ]);

    res.render('summary', { result });
});
module.exports = router