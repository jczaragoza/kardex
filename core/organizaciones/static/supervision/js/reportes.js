var tblOrganizacion;

var organizacion = {
    model: {},
    list: function (){
        tblOrganizacion = $('#data').DataTable({
            orderCellsTop: false,
            fixedHeader: false, 
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            searching: true,
            dom: 'Bfrtip',
            buttons: [
                // {
                //     extend: 'csv',
                //     text: 'Descargar csv <i class="fas fa-file-excel"></i>',
                //     className: 'btn btn-warning btn-flat btn rounded'
                // },
                {
                    extend: 'excel',
                    text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
                    className: 'btn btn-success btn-flat btn-xs rounded'
                },
                {
                    extend: 'pdf',
                    text: 'Descargar PDF <i class="fas fa-file-pdf"></i>',
                    className: 'btn btn-danger btn-flat btn-xs rounded'
                },
            ],
            // buttons: [
            //     {
            //         extend: 'excelHtml5',
            //         text: 'Descargar Excel <i class="fas fa-file-excel"></i>',
            //         titleAttr: 'excel',
            //         className: 'btn btn-success btn-flat btn-xs'
            //     },
            // ],
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
            // columns: [
            //     {"data": "id"},
            //     {"data": "nombre"},
            //     {"data": "tipo_organizacion"},
            //     {"data": "estatus_ficha"},
            //     {"data": "usuario"},
            //     {"data": "modified"},
            // ],

            initComplete: function (settings, json) {

            }

        });

        //Creamos una fila en el head de la tabla y lo clonamos para cada columna
        $('#data thead tr').clone(true).appendTo( '#data thead' );
    
        $('#data thead tr:eq(1) th').each( function (i) {
            var title = $(this).text(); //es el nombre de la columna
            $(this).html( '<input type="text" placeholder="Búsqueda por...'+title+'" />' );
    
            $( 'input', this ).on( 'keyup change', function () {
                if ( tblOrganizacion.column(i).search() !== this.value ) {
                tblOrganizacion
                    .column(i)
                    .search( this.value )
                    .draw();
                }
            });
        });       
    
    }
};

$(function (){
    organizacion.list();
    
});

    // //Creamos una fila en el head de la tabla y lo clonamos para cada columna
    // $('#data thead tr').clone(true).appendTo( '#data thead' );

    // $('#data thead tr:eq(1) th').each( function (i) {
    //     var title = $(this).text(); //es el nombre de la columna
    //     $(this).html( '<input type="text" placeholder="Búsqueda por...'+title+'" />' );
 
    //     $( 'input', this ).on( 'keyup change', function () {
    //         if ( colectivo.column(i).search() !== this.value ) {
    //         colectivo
    //             .column(i)
    //             .search( this.value )
    //             .draw();
    //         }
    //     });
    // });       
