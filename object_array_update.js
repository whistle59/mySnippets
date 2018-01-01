let arr1 = [{
    name: "John",
    age: 22
  },
  {
    name: "Theresa",
    age: 35
  },
  {
    name: "Peter",
    age: 17
  },
  {
    name: "Mary",
    age: 99
  },
  {
    name: "Anna",
    age: 36
  },
];

let arr2 = [{
    name: "John",
    age: 23
  },
  {
    name: "Anna",
    age: 36
  },
  {
    name: "Joseph",
    age: 99
  },
  {
    name: "Theresa",
    age: 88
  },
  {
    name: "Albert",
    age: 12
  },
];

function updateArr(arr1, arr2) {
  for (let item2 of arr2) {
    let toUpdate = arr1.find(item1 => item1.name == item2.name);

    if (toUpdate === undefined) {
      arr1.push(item2);
    } else {
      let idx = arr1.findIndex(elem => elem.name == toUpdate.name);
      arr1[idx].age = toUpdate.age;
    }
  }
}

updateArr(arr1, arr2);

console.log(arr1);
