/*
    transaction.js -- Router for the transaction list
*/
const express = require('express');
const router = express.Router();
const User = require('../models/User');
const TransactionItem = require('../models/TransactionItem');
//const { isLoggedIn } = require('./pwauth');



isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
}

router.get('/transaction/',
    isLoggedIn,
    async (req, res, next) => {
        const sortBy = req.query.sortBy
        let trs=[]
        if (sortBy == "category") {
            trs= 
            await TransactionItem.find({userId:req.user._id}).sort({category:1})
        }
        else if (sortBy == "amount") {
            trs= 
            await TransactionItem.find({userId:req.user._id}).sort({amount:1})
        }
        else if (sortBy == "date") {
            trs= 
            await TransactionItem.find({userId:req.user._id}).sort({date:1})
        }
        else if (sortBy == "description") {
            trs= 
            await TransactionItem.find({userId:req.user._id}).sort({description:1})
        }
        else {
            trs = 
             await TransactionItem.find({userId:req.user._id}).sort({createdAt:1})
        }
            res.render('transactions',{trs, sortBy})
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
        res.redirect('/transaction/')
    }
)

router.get('/transaction/remove/:transactionId',
    isLoggedIn,
    async (req, res) => {
        console.log("inside /transaction/remove/:transactionId")
        await TransactionItem.deleteOne(
            {_id:req.params.transactionId}
        );
        res.redirect('/transaction')
    }
)

module.exports = router;