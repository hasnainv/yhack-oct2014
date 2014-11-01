/**
 * GET /
 * Home page.
 */

exports.index = function(req, res) {
  res.render('ideaboard', {
    title: 'Home'
  });
};

exports.dashboard = function(req, res) {
	res.render('dashboard', {
	  title: 'Dashboard'
	});
}

