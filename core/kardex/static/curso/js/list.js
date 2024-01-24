var tblCursos;
var fv;
var curso = {
    model: {},
    list: function () {
        tblCursos = $('#data').DataTable({
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
                {"data": "nombre"},
                {"data": "persona_nombre"},
                {"data": "horas"},
                {"data": "tipo_curso"},
                {"data": "documento"},
                {"data": "institucion"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    data: null,
                    render: function (data, type, row) {
                        var content = '<div class="btn-group" role="group"><button id="btnGroupDrop1" type="button" class="btn btn-secondary btn-xs dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fas fa-align-justify"></i> Opciones</button><div class="dropdown-menu dropdown-menu-right" aria-labelledby="btnGroupDrop1">';
                        content += '<a class="dropdown-item" href="' + pathname + 'update/' + row.id + '/"><i class="fas fa-edit"></i> Editar</a>';
                        content += '<a class="dropdown-item" href="' + pathname + 'delete/' + row.id + '/"><i class="fas fa-trash"></i> Eliminar</a>';
                        return content;
                        
                    }
                    
                },
                {
                    targets: [-5],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return parseInt(data) + ' Horas';
                    }
                },
            ],  
            //ORDENAR TABLA 0 es la posicion de la columna 
            order: [[ 0, 'desc' ]],
            initComplete: function (settings, json) {
                //alert ("tabla cargada");
            }
        });
    }
};


$(function () {

    curso.list();
            
});
