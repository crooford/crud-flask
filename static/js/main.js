const btndelete = document.querySelectorAll('.btn-delete')

if (btndelete){
    const btnarray = Array.from(btndelete);
    btnarray.forEach((btn)=>{
        btn.addEventListener('click',(e)=>{
            if (!confirm('¿Estas seguro de eliminar este contacto?')){
                e.preventDefault();
            }
        });
    });
}