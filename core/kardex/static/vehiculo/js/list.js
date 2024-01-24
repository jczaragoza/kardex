var tblVehiculos;
var fv;
var vehiculos = {
    model: {},
    list: function () {
        tblVehiculos = $('#data').DataTable({
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
                {"data": "marca"},
                {"data": "submarca"},
                {"data": "tipo"},
                {"data": "modelo"},
                {"data": "color"},
                {"data": "matricula"},
                {"data": "motor"},
                {"data": "serie"},
                {"data": "persona_nombre"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/kardex/vehiculo/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="/kardex/vehiculo/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                        return buttons;
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

    vehiculos.list();
            
});
