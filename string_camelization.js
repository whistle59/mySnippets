/*
This example was taken from https://javascript.info/constructor-new
Thanks to Ilya for that awsome course!!

FUNCTIONALITY:
Changes dash-separated words like “my-short-string” into camel-cased “myShortString”.
That is: removes all dashes, each word after dash becomes uppercased
 and also fixes any case typo in each word.

Note: The "dot" chain is possible because each method returs an array
*/


function camelize(str) {
  return str
    .split("-")
    .map(
      (item, index) => (index == 0) ? item.toLowerCase()
        : item[0].toUpperCase() + item.slice(1).toLowerCase()
    )
    .join("");
}

console.log( camelize("jUSt-onE-crazy-LONG-strinG-to-camELIze"));
