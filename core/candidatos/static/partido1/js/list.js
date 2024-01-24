var tblPartidos;
var fv;
var partido = {
    model: {},
    list: function () {
        tblPartidos = $('#data').DataTable({
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
                {"data": "siglas"},
                {"data": "foto"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="/candidato/partido/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="/candidato/partido/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                        return buttons;
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img alt="" class="img-fluid mx-auto d-block rounded-circle" src="' + data + '" width="20px" height="20px">';
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

    partido.list();
            
});
