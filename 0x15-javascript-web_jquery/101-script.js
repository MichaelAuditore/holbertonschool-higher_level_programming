$(document).ready(function () {
    let list = $('.my_list');
    buttons = {};

    buttons.add = function () {
        let addDiv = $('#add_item');
        addDiv.click(function () {
            list.append('<li>Item</li>');
        });
    }

    buttons.remove = function () {
        let removeDiv = $('#remove_item');
        removeDiv.click(function () {
            list.children().last().remove();
        });
    }
    buttons.clear = function () {
        let clearDiv = $('#clear_list');
        clearDiv.click(function () {
            list.empty();
        });
    }

    buttons.add();
    buttons.remove();
    buttons.clear();
});

