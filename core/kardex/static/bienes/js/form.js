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
                categoria: {
                    validators: {
                        notEmpty: {},
                    }
                },
                descripcion: {
                    validators: {
                        notEmpty: {},
                    }
                },
                curp: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 2,
                        },
                        //digits: {},
                        remote: {
                            url: pathname,
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="resguardo"]').value,
                                    type: 'resguardo',
                                    action: 'validate_data'
                                };
                            },
                            message: 'Resguardo ya registrado' ,
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
                    }
                },
             }
            
        }
    )
    .on('core.form.valid', function () {
        submit_formdata_with_ajax_form(fv);
    });
});

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

});