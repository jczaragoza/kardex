var fv;

document.addEventListener('DOMContentLoaded', function (event) {
    const form = document.getElementById('frmForm');
    const submitButton = form.querySelector('[type="submit"]');
    fv = FormValidation.formValidation(form, {
            locale: 'es_ES',
            localization: FormValidation.locales.es_ES,
            plugins: {
                trigger: new FormValidation.plugins.Trigger(),
                submitButton: new FormValidation.plugins.SubmitButton(),
                // defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
                bootstrap: new FormValidation.plugins.Bootstrap(),
                icon: new FormValidation.plugins.Icon({
                    valid: 'fa fa-check',
                    invalid: 'fa fa-times',
                    validating: 'fa fa-refresh',
                }),
            },
            // fields: {
            //     rfc: {
            //         validators: {
            //             notEmpty: {},
            //             stringLength: {
            //                 min: 13,
            //             },
            //             //digits: {},
            //             remote: {
            //                 url: pathname,
            //                 data: function () {
            //                     return {
            //                         obj: form.querySelector('[name="rfc"]').value,
            //                         type: 'rfc',
            //                         action: 'validate_data'
            //                     };
            //                 },
            //                 message: 'El RFC ya se encuentra registrado' ,
            //                 method: 'POST',
            //                 headers: {
            //                     'X-CSRFToken': csrftoken
            //                 },
            //             }
            //         }
            //     },
            //     zona_influencia: {
            //         validators: {
            //             notEmpty: {},
            //             stringLength: {
            //                 min: 20,
            //             },
                        
            //         }
            //     },
                
            // }
        }
    )
    .on('core.form.valid', function () {
        submit_formdata_with_ajax_form(fv);
    });
});

$(function () {

    $('select[name="municipio"]').select2({
        theme: 'bootstrap4',
        language: "es",
        placeholder: 'Buscar Municipio ...',
    });

    // SELECT tipo contendiente CHAINED
    $(document).ready(function() {
        var $tipoContendiente = $('#id_tipo_contendiente');
        var $municipio = $('#id_municipio');
        var $distritoLocal = $('#id_distrito_local');
        var $distritoFederal = $('#id_distrito_federal');
        
        $tipoContendiente.on('change', function() {
            if ($tipoContendiente.val() === '1'){
                $municipio.parent().show();
                $distritoLocal.parent().hide();
                $distritoFederal.parent().hide();
            }
            else if ($tipoContendiente.val() === '3') {
                $municipio.parent().hide();
                $distritoLocal.parent().show();
                $distritoFederal.parent().hide();
            } else if ($tipoContendiente.val() === '2') {
                $municipio.parent().hide();
                $distritoLocal.parent().hide();
                $distritoFederal.parent().show();
            } else {
                $municipio.parent().hide();
                $distritoLocal.parent().hide();
                $distritoFederal.parent().hide();
            }
        });
        
    
        //Oculta los campos inicialmente si no se selecciona 'medios' o 'redes_sociales'
        if ($tipoContendiente.val() !== '3' && $tipoContendiente.val() !== '2' && $tipoContendiente.val() !== '1') {
            $municipio.parent().hide();
            $distritoLocal.parent().hide();
            $distritoFederal.parent().hide();
        }
    });

        
    // $('input[name="rfc"]').on('input', function(e) {
    //     $(this).val(function(_, val) {
    //       return val.toUpperCase();
    //     });
    // });
    
    // $('input[name="zona_influencia"]').on('input', function(e) {
    //     $(this).val(function(_, val) {
    //       return val.toUpperCase();
    //     });
    // });

});