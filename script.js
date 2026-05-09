document.querySelector('.hamb')?.addEventListener('click',()=>document.querySelector('.links').classList.toggle('open'));
const y=document.getElementById('year'); if(y) y.textContent=new Date().getFullYear();
