/*$(document).ready(function() {

}*/

//function test() {
	// Place JavaScript code here...
var pages = {};
var lastPageId = 0;
socket.on('connect', function () {
    console.log('Socket connected');
    socket.on('pageview', function (msg) {
        console.log('Connections: ' + msg.connections);
        $('#connections > p').html(msg.connections - 1);  // -1 since we don't count our own dashboard connection
        if (msg.url) {
            if ($('#visits tr').length > 10) {
                $('#visits tr:last').remove();
            }
            $('#visits tbody').prepend('<tr><td>' + msg.url + '</td><td>' + msg.ip + '</td><td>' + msg.timestamp + '</td></tr>');
            if (pages[msg.url]) {
                pages[msg.url].views = pages[msg.url].views + 1;
                $('#page' + pages[msg.url].pageId).html(pages[msg.url].views);
            } else {
                pages[msg.url] = {views: 1, pageId: ++lastPageId};
                $('#pageViews tbody').append('<tr><td>' + msg.url + '</td><td id="page' + lastPageId + '">1</td></tr>');
            }
        }
    });
});
