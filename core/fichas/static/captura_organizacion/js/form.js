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
            fields: {
                nombre: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 5,

                        },
                        //digits: {},
                        // remote: {
                        //     url: pathname,
                        //     data: function () {
                        //         return {
                        //             obj: form.querySelector('[name="nombre"]').value,
                        //             type: 'nombre',
                        //             action: 'validate_data'
                        //         };
                        //     },
                        //     message: 'El nombre ya se encuentra registrado' ,
                        //     method: 'POST',
                        //     headers: {
                        //         'X-CSRFToken': csrftoken
                        //     },
                        // }
                    }
                },
                fecha_creacion: {
                    validators: {
                        notEmpty: {},
                    }
                },
                estatus_ficha: {
                    validators: {
                        notEmpty: {},
                    }
                },
                foto: {
                    validators: {
                        file: {
                            extension: 'jpeg,jpg,png',
                            type: 'image/jpeg,image/png',
                            maxFiles: 1,
                            message: 'Introduce una imagen válida'
                        }
                    }
                },
             }
        }
    )
        .on('core.element.validated', function (e) {
            if (e.valid) {
                const groupEle = FormValidation.utils.closest(e.element, '.form-group');
                if (groupEle) {
                    FormValidation.utils.classSet(groupEle, {
                        'has-success': false,
                    });
                }
                FormValidation.utils.classSet(e.element, {
                    'is-valid': false,
                });
            }
            const iconPlugin = fv.getPlugin('icon');
            const iconElement = iconPlugin && iconPlugin.icons.has(e.element) ? iconPlugin.icons.get(e.element) : null;
            iconElement && (iconElement.style.display = 'none');
        })
        .on('core.validator.validated', function (e) {
            if (!e.result.valid) {
                const messages = [].slice.call(form.querySelectorAll('[data-field="' + e.field + '"][data-validator]'));
                messages.forEach((messageEle) => {
                    const validator = messageEle.getAttribute('data-validator');
                    messageEle.style.display = validator === e.validator ? 'block' : 'none';
                });
            }
        })
        .on('core.form.valid', function () {
            submit_formdata_with_ajax_form(fv);
        });
});

$(function () {

    $('.select2').select2({
        theme: 'bootstrap4',
        language: 'es'
        
    });

    $('select[name="lideres"]').select2({
        theme: 'bootstrap4',
        language: "es",
        placeholder: 'Buscar..',
    });

    
    $('input[name="nombre"]').on('input', function(e) {
        $(this).val(function(_, val) {
          return val.toUpperCase();
        });
    });

    // MODAL AGREGAR EVENTO
    $('.btnAddEvento').on('click', function () {
        $('#myModalEvento').modal('show');
    });

    $('#myModalEvento').on('hidden.bs.modal', function (e) {
        $('#frmEvento').trigger('reset');
    })

    $('#frmEvento').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'add_evento');
        
        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar evento?',
            pathname,
            parameters,
            function (response) {
                var newOption = new Option(response.nombre, response.id, false, true);
                $('select[name="nombre"]').append(newOption).trigger('change');
                location.href = pathname;
            });
    });

    //MODAL AGREGAR INTEGRANTES
    $('.btnAddIntegrante').on('click', function () {
        $('#myModalIntegrante').modal('show');
    });

    $('#myModalIntegrante').on('hidden.bs.modal', function (e) {
        $('#frmIntegrante').trigger('reset');
    })

    $('#frmIntegrante').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'add_integrante');
        
        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar evento?',
            pathname,
            parameters,
            function (response) {
                var newOption = new Option(response.integrantes_nombres, response.id, false, true);
                $('select[name="integrantes_nombres"]').append(newOption).trigger('change');
                location.href = pathname;
            });
    });

});