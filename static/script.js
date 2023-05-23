
// let but = document.getElementById('knopka');
// console.log(data)
// but.addEventListener('click', function ddd() {
//     console.log(data)
// });
document.querySelector("#knopka").addEventListener("click", Handler);
let a = document.querySelector('.push')

function Handler(event) {
    fetch('/api')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            a.innerHTML += myjson
        });
    
   
}