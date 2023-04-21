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

// get the value associated to the key
router.get('/transaction/',
  isLoggedIn,
  async (req, res, next) => {
      const show = req.query.show
      const completed = show=='completed'
      let items=[]
      if (show) { // show is completed or transaction, so just show some items
        items = 
          await TransactionItem.find({userId:req.user._id, completed})
                        .sort({completed:1,priority:1,createdAt:1})
      }else {  // show is null, so show all of the items
        items = 
          await TransactionItem.find({userId:req.user._id})
                        .sort({completed:1,priority:1,createdAt:1})

      }
            res.render('transactions',{items,show,completed});
});

/* add the value in the body to the list associated to the key */
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const transaction = new TransactionItem(
        {item:req.body.item,
         createdAt: new Date(),
         completed: false,
         priority: parseInt(req.body.priority),
         userId: req.user._id
        })
      await transaction.save();
      res.redirect('/firstapp')
});

router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:itemId")
      await TransactionItem.deleteOne({_id:req.params.itemId});
      res.redirect('/firstapp')
});

router.get('/transaction/complete/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/complete/:itemId")
      await TransactionItem.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {completed:true}} );
      res.redirect('/firstapp')
});

router.get('/transaction/uncomplete/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/complete/:itemId")
      await TransactionItem.findOneAndUpdate(
        {_id:req.params.itemId},
        {$set: {completed:false}} );
      res.redirect('/firstapp')
});

router.get('/transaction/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/edit/:itemId")
      const item = 
       await TransactionItem.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit')
      //res.json(item)
});

router.post('/transaction/updateTodoItem',
  isLoggedIn,
  async (req, res, next) => {
      const {itemId,item,priority} = req.body;
      console.log("inside /transaction/complete/:itemId");
      await TransactionItem.findOneAndUpdate(
        {_id:itemId},
        {$set: {item,priority}} );
      res.redirect('/firstapp')
});

router.get('/transaction/byUser',
  isLoggedIn,
  async (req, res, next) => {
      let results =
            await ToDoItem.aggregate(
                [ 
                  {$group:{
                    _id:'$userId',
                    total:{$count:{}}
                    }},
                  {$sort:{total:-1}},              
                ])
              
        results = 
           await User.populate(results,
                   {path:'_id',
                   select:['username','age']})

        //res.json(results)
        res.render('summarizeByUser',{results})
});

module.exports = router;