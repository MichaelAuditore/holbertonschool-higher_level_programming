const div = $('#add_item');
div.click(function () {
  const ul = $('.my_list');
  ul.append('<li>Item</li>');
});
