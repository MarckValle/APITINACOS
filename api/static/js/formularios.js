function validarFormulario() {
    var campo1 = document.getElementById('nombre').value;
    var campo2 = document.getElementById('correo').value;
    var campo3 = document.getElementById('psw').value;
    var campo4 = document.getElementById('genero').value;
    
    if ((campo1 == '') || (campo2 == '') || (campo3=='') || (campo4=='Género')) {
        Swal.fire({
            titleText:"Ha ocurrido un error!",
            text: "No puedes acceder con los campos vacíos.",
            icon:"warning",
            confirmButtonText:"OK!"
           });
       
         return false;
        }else{
            document.getElementById('a-form').submit();
            toastr.options = {
                "closeButton": false,
                "debug": false,
                "newestOnTop": false,
                "progressBar": false,
                "positionClass": "toast-top-center",
                "preventDuplicates": false,
                "onclick": null,
                "showDuration": "300",
                "hideDuration":   "1000",
                "timeOut": "5000",
                "extendedTimeOut": "1000",
                "showEasing": "swing",
                "hideEasing": "linear",
                "showMethod": "fadeIn",
                "hideMethod": "fadeOut"
              }
              toastr["success"]("Te has registrado correctamente, Verifica tu correo", "Registro Exitoso!")
        }
        // Otras validaciones...
        
        return true;
    }