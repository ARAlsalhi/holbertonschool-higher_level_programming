const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  const myList = document.querySelector('.my_list');
  myList.appendChild(newItem);
});
