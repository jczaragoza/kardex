var tblOrg;
var fv;
var organizacion = {
    model: {},
    list: function () {
        tblOrg = $('#data').DataTable({
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
                {"data": "nombre"},
                {"data": "tipo_organizacion"},
                // {"data": "estatus_ficha"},
                {"data": "fecha_creacion"},
                {"data": "modified"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    //IMAGEN
                    targets: [-6],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img alt="" class="img-fluid mx-auto d-block rounded-circle" src="' + data + '" width="20px" height="20px">';
                    }
                },
                // {
                //     targets: [-4],
                //     class: 'text-center',
                //     render: function (data, type, row) {
                //         if (data == 'En proceso') {
                //             return '<span class="badge badge-warning"> '+ data +'</span>';
                //         }
                //         else if (data == 'Corregir') {
                //             return '<span class="badge badge-danger"> '+ data +'</span>';
                //         }
                //         return '<span class="badge badge-success"> '+ data +'</span>';

                //     }
                // }, 
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    data: null,
                    render: function (data, type, row) {
                        var content = '<div class="btn-group" role="group"><button id="btnGroupDrop1" type="button" class="btn btn-secondary btn-xs dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-align-justify"></i> Opciones</button><div class="dropdown-menu dropdown-menu-right" aria-labelledby="btnGroupDrop1">';
                        content += '<a class="dropdown-item" href="' + '/fichas/consulta/org/detail/' + row.id + '/"><i class="fas fa-id-card"></i> Detalle</a>';
                        content += '<a class="dropdown-item" target="_blank" href="/report/organizacion/pdf/' + row.id + '/"><i class="fas fa-file-pdf"></i>PDF</a>';
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

    organizacion.list();
    
            
});
