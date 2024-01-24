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

var vents = {
    items: {
        evento: '',
        organizacion: '',
        fichacurricular: '',
        created: '',
        modified: '',
    },
};

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('select[name="search_org"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'autocomplete_org'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
    });

    $('select[name="fichacurricular"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_lider'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
    });


    $('select[name="evento"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_evento'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripción',
        minimumInputLength: 1,
    });

    $('.btnAddEvento').on('click', function () {
        $('#myModalEvento').modal('show');
    });

    $('#myModalEvento').on('hidden.bs.modal', function (e) {
        $('#frmEvento').trigger('reset');
    })

    $('#frmEvento').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'create_evento');
        
        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar evento?',
            pathname,
            parameters,
            function (response) {
                var newOption = new Option(response.full_name, response.id, false, true);
                $('select[name="nombre"]').append(newOption).trigger('change');
                location.href = pathname;
            });
    });

    $('#frmDetalle').on('submit', function (e) {
        e.preventDefault();

        vents.items.evento = $('select[name="evento"]').val();
        vents.items.organizacion = $('select[name="organizacion"]').val();
        vents.items.fichacurricular = $('select[name="fichacurricular"]').val();
       
        var parameters = new FormData();
        parameters.append('action', 'add_detalle');
        parameters.append('vents', JSON.stringify(vents.items));

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar evento1212?',
            pathname,
            parameters,
            function (response) {
                location.href = '/organizaciones/detalle/add/';
            });
    });


});