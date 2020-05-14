$(document).ready(function () {
  const list = $('.my_list');
  const buttons = {};

  buttons.add = function () {
    const addDiv = $('#add_item');
    addDiv.click(function () {
      list.append('<li>Item</li>');
    });
  };

  buttons.remove = function () {
    const removeDiv = $('#remove_item');
    removeDiv.click(function () {
      list.children().last().remove();
    });
  };

  buttons.clear = function () {
    const clearDiv = $('#clear_list');
    clearDiv.click(function () {
      list.empty();
    });
  };

  buttons.add();
  buttons.remove();
  buttons.clear();
});
