/*
    transaction.js -- Router for the transaction list
*/
const express = require('express');
const router = express.Router();
const ToDoItem = require('../models/TransactionItem')
const User = require('../models/User')