var mongoose = require('mongoose');
var User = require('./User');

var ideaSchema = new mongoose.Schema({
  //'id': {type: String, index: true},
  //'user': String,
  'user': {
    type: mongoose.Schema.ObjectId,
    ref: 'userSchema'
  },
  'tags': [String],
  'content': String
});

function extractKeywords(text) {
  if (!text) return [];
  return text.
    split(/\s+/).
    filter(function(v) { return v.length > 2; }).
    filter(function(v, i, a) { return a.lastIndexOf(v) === i; });
}

ideaSchema.pre('save', function(next) {
  this.keywords = extractKeywords(this.data);
  next();
});

module.exports = mongoose.model('Idea', ideaSchema);