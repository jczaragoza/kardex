var tblCapturaLider;
var fv;
var capturaLider = {
    model: {},
    list: function () {
        tblCapturaLider = $('#data').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            ajax: {
                url: pathname,
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'action': 'searchdata'
                },
                dataSrc: ""
            },
            columns: [
                {"data": "id"},
                {"data": "foto"},
                {"data": "full_name"},
                {"data": "estatus_ficha"},
                {"data": "organizaciones"},
                {"data": "created"},
                {"data": "modified"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img alt="" class="img-fluid mx-auto d-block rounded-circle" src="' + data + '" width="20px" height="20px">';
                    }
                },
                {
                    targets: [3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data == 'En proceso') {
                            return '<span class="badge badge-warning"> '+ data +'</span>';
                        }
                        else if (data == 'Corregir') {
                            return '<span class="badge badge-danger"> '+ data +'</span>';
                        }
                        return '<span class="badge badge-success"> '+ data +'</span>';

                    }
                }, 
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    data: null,
                    render: function (data, type, row) {
                        var content = '<div class="btn-group" role="group"><button id="btnGroupDrop1" type="button" class="btn btn-secondary btn-xs dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-align-justify"></i> Opciones</button><div class="dropdown-menu dropdown-menu-right" aria-labelledby="btnGroupDrop1">';
                        content += '<a class="dropdown-item" href="' + '/fichas/captura/lider/update/' + row.id + '/"><i class="fas fa-edit"></i> Editar</a>';
                        content += '<a class="dropdown-item" href="' + '/fichas/captura/lider/detail/' + row.id + '/"><i class="fas fa-id-card"></i> Detalle</a>';
                        //content += '<a class="dropdown-item" target="_blank" href="/report/organizacion/pdf/' + row.id + '/"><i class="fas fa-file-pdf"></i>PDF</a>';
                        //content += '<a class="dropdown-item" href="' + '/fichas/lider/delete/' + row.id + '/"><i class="fas fa-trash"></i> Eliminar</a>';
                        return content;
                    }
                },
            ],
            //ORDENAR TABLA 0 es la posicion de la columna 
            order: [[ 5, 'desc' ]],
            initComplete: function (settings, json) {
                //alert ("tabla cargada");
            }
        });
    }
};


$(function () {

    capturaLider.list();
            
});
