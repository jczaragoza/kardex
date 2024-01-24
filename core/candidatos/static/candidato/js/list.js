var tblCandidatos;
var fv;
var candidato = {
    model: {},
    list: function () {
        tblCandidatos = $('#data').DataTable({
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
                {"data": "zona_influencia"},
                {"data": "poder_convocatoria"},
                {"data": "riesgo"},
                {"data": "full_partido"},
                {"data": "estatus_candidato"},
                {"data": "periodo"},
                {"data": "modified"},
                {"data": "is_active"},
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
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    data: null,
                    render: function (data, type, row) {
                        var content = '<div class="btn-group" role="group"><button id="btnGroupDrop1" type="button" class="btn btn-secondary btn-xs dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-align-justify"></i> Opciones</button><div class="dropdown-menu dropdown-menu-right" aria-labelledby="btnGroupDrop1">';
                        content += '<a class="dropdown-item" href="' + '/candidato/update/' + row.id + '/"><i class="fas fa-edit"></i> Editar</a>';
                        content += '<a class="dropdown-item" href="' + '/candidato/detail/' + row.id + '/"><i class="fas fa-id-card"></i> Detalle</a>';
                        content += '<a class="dropdown-item" target="_blank" href="/report/candidato/pdf/' + row.id + '/"><i class="fas fa-file-pdf"></i>PDF</a>';
                        content += '<a class="dropdown-item" href="' + '/candidato/delete/' + row.id + '/"><i class="fas fa-trash"></i> Eliminar</a>';
                        return content;
                        
                    }
                },
                {
                    targets: [-2], // Índice de la columna "is_active"
                    visible: false,
                    searchable: false,
                    render: function(data, type, row, meta) {
                        if (data === 'false') {
                            return 'Inactivo';
                        } else {
                            return 'Activo';
                        }
                    }
                },
                // {
                //     targets: [-2], // Índice de la columna "is_active"
                //     visible: false,
                //     render: function(data, type, row, meta) {
                //         if (type === 'display') {
                //             return data ? 'true' : 'false';
                //         }
                //         return data ? 1 : 0;
                //     }
                // },
            ],
            //ORDENAR TABLA 0 es la posicion de la columna 
            order: [[ 9, 'desc' ]],
            initComplete: function (settings, json) {
                //alert ("tabla cargada");
            }
        });
    }
};


$(function () {

    candidato.list();
    
            
});
