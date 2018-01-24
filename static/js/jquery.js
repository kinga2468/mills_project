$(function() {
    $('a#wyslij').bind('click', function() {
        $.getJSON($SCRIPT_ROOT + '/add', {
            a: $('input[name="a"]').val()
        }, function(data) {
            var x = $('input[name="a"]').val();
            $('#p'+x).addClass(data.result);
        });
        return false;
    });
});
