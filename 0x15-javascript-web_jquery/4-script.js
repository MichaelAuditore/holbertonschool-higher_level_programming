let div = $('#toggle_header');
div.click(function () {
    let header = $('header');
    let clss = header.attr('class');
    header.addClass(clss === 'red' ? 'green' : 'red');
    header.removeClass(clss === 'red' ? 'red' : 'green');
});