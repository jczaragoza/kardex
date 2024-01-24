var tblPersonas;
var kar = {
    items : {
        curso: '',
        fecha_nacimiento: '',
        personas: [],

    },
    add: function(item){
        this.items.personas.push(item);
        this.list();
    },
    list: function () {
        tblPersonas == $('#tblPersonas').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.personas,
            columns: [
                
                {"data": "full_name"},
                {"data": "clavesp"},
                {"data": "estatus"},
                {"data": "rfc"},
                {"data": "cuip"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                
            ],
            initComplete: function (settings, json) {

            }
        });
    },
};

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#fecha_actual').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    }); 
    
    
    //SEARCH CURSOS
    $('select[name="curso"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 100,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_cursos'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        
        placeholder: 'Ingrese nombre de curso',
        minimumInputLength: 1,
    });


    // Agregar Curso with modal
    $('.btnAddCurso').on('click', function(){
        $("#myModalCurso").modal('show');
    });
    
    $('#myModalCurso').on('hidden.bs.modal', function (e){
        $('#frmCurso').trigger('reset')
    })

    $('frmCurso').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_curso');
        submit_with_ajax(window.location.pathname, 'Notificación',
        '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
            $("#myModalCurso").modal('hide');

        });
    });

    /*
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_personas',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 50,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            console.log(kar.items);
            kar.add(ui.item);
            $(this).val('');
        }
    }); 
    */

    //remove all
    $('.btnRemoveAll').on('click', function () {
        if (kar.items.personas.length === 0) return false;
        alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
            kar.items.personas = [];
            kar.list();
        });
    });

  
    // event remove
    $('#tblPersonas tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblPersonas.cell($(this).closest('td, li')).index();
            alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?',
                function () {
                    kar.items.personas.splice(tr.row, 1);
                    kar.list();
                }, function () {

                });
        });

    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();
    });

    //event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if(kar.items.personas.length === 0){
            message_error('Debe al menos tener un registro');
            return false;
        }
        kar.items.fecha_actual = $('input[name="fecha_actual"]').val();
        kar.items.curso = $('select[name="curso"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('kar', JSON.stringify(kar.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
             location.href = '/kardex/kardex/list/';
        });

    });
 
    $('select[name="search"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 100,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_personas'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        
        placeholder: 'Ingrese nombre de Personal',
        minimumInputLength: 1,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        kar.add(data);
        $(this).val('').trigger('change.select2');
    });


    kar.list();
  
});
