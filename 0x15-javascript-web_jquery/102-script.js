$(document).ready(function () {
    let button = $('#btn_translate');
    button.click(function () {
        const INPUT = $('#language_code').val();
        const URL = 'https://www.fourtonfish.com/hellosalut/';
        $.get(URL, { lang: INPUT }, function (response) {
            $('#hello').text(response.hello);
        });
    });
});