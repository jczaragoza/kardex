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
                clavesp: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 9,
                        },
                        digits: {},
                        remote: {
                            url: pathname,
                            // Send { username: 'its value', email: 'its value' } to the back-end
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="clavesp"]').value,
                                    type: 'clavesp',
                                    action: 'validate_data'
                                };
                            },
                            message: 'Clave de servidor público ya registrada',
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
                    }
                },
                rfc: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 13,
                        },
                        //digits: {},
                        remote: {
                            url: pathname,
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="rfc"]').value,
                                    type: 'rfc',
                                    action: 'validate_data'
                                };
                            },
                            message: 'El RFC ya se encuentra registrado' ,
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
                    }
                },
                curp: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 18,
                        },
                        //digits: {},
                        remote: {
                            url: pathname,
                            data: function () {
                                return {
                                    obj: form.querySelector('[name="curp"]').value,
                                    type: 'curp',
                                    action: 'validate_data'
                                };
                            },
                            message: 'La CURP ya se encuentra registrada' ,
                            method: 'POST',
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                        }
                    }
                },
                cuip: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 20,
                        },
                        
                    }
                },
                correo: {
                    validators: {
                        stringLength: {
                            min: 5
                        },
                        regexp: {
                            regexp: /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/i,
                            message: 'El email no es correcto'
                        },
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
    
 
    $('input[name="clavesp"]').on('keypress', function (e) {
        return validate_form_text('numbers', e, null);
    });

    $('input[name="rfc"]').on('input', function(e) {
        $(this).val(function(_, val) {
          return val.toUpperCase();
        });
    });

    $('input[name="curp"]').on('input', function(e) {
        $(this).val(function(_, val) {
          return val.toUpperCase();
        });
    });
    
    $('input[name="cuip"]').on('input', function(e) {
        $(this).val(function(_, val) {
          return val.toUpperCase();
        });
    });
    

});