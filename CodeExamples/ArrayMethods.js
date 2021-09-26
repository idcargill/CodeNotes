// map  array.map() 9.23
// Reurns equal length array

const movies = [
  { title: 'Fatman', rating: 'Good' },
  { title: 'Nightmare Before Christmas', rating: 'Good' },
  { title: 'Black Christmas', rating: 'Good' },
  { title: 'Bad Sandta', rating: 'bad' },
  { title: 'Die Hard', rating: 'wtf' },
];

let goodMovies = movies.map((movie, idx) => {
  return movie.rating == 'Good' ? movie.title : 'Its Bad';
});

// console.log(goodMovies);

const num = [1, 2, 3, 4, 5];

let addNums = num.map((n) => {
  return n + 2;
});

// one line  =======================
let addNum2 = num.map((n) => n + 3);

console.log('\t \t', addNum2);
