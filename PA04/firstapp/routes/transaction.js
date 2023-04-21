/*
    transaction.js -- Router for the transaction list
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

router.get('/transaction',
    isLoggedIn,
    async (req, res, next) => {
        let trs=[]
         trs= 
            await TransactionItem.find({userId:req.user._id}).sort({createdAt:1})
        res.render('transactions',{trs})
});

router.post('/transaction',
    isLoggedIn,
    async (req, res, next) => {
        const transact = new TransactionItem(
            {description:req.body.description,
            amount: parseFloat(req.body.amount),
            category:req.body.category,
            date:req.body.date,
            createdAt: new Date(),
            userId:req.user._id}
        )
        await transact.save();
        res.redirect('/transaction')
    }
)


module.exports = router;