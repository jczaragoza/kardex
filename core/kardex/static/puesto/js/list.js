var tblPuestos;
var fv;
var curso = {
    model: {},
    list: function () {
        tblPuestos = $('#data').DataTable({
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
                {"data": "codigo_puesto"},
                {"data": "nivel_rango"},
                {"data": "sueldo_bruto"},
                {"data": "sueldo_neto"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/kardex/puesto/update/' + row.id + '/" class="btn btn-warning btn-xs"><i class="fas fa-edit"></i></a> ';
                        return buttons;
                    }
                },
                {
                    targets: [-2, -3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
    
            ],
    
            initComplete: function (settings, json) {
                //alert ("tabla cargada");
            }
        });
    }
};


$(function () {

    curso.list();
            
});




