$(document).ready(function () {
    let button = $('#btn_translate');
    let language = $('#language_code');
    
    const URL = 'https://www.fourtonfish.com/hellosalut/';
    language.on('keypress', function (e) {
        const INPUT = language.val();
        if (e.which == 13) {
            $.get(URL, { lang: INPUT }, function (response) {
                $('#hello').text(response.hello);
            });
        }
    });
    button.click(function () {
        const INPUT = language.val();
        $.get(URL, { lang: INPUT }, function (response) {
            $('#hello').text(response.hello);
        });
    });
});