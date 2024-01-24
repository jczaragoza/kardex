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
                            min: 2,
                        },
                        
                    }
                },
                curp: {
                    validators: {
                        notEmpty: {},
                        stringLength: {
                            min: 18,
                            max: 18,
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

    var candidatoActivoCheckbox = $('#id_candidato_activo');
    var tipoContendienteField = $('#id_tipo_contendiente');
    var municipioElectoralField = $('#id_municipio');
    var periodoElectoralField = $('#id_periodo_electoral');
    var partidoField = $('#id_partido');
    var protestaField = $('#id_protesta');
    var distritoLocalField = $('#id_distrito_local');
    var distritoFederalField = $('#id_distrito_federal');
     
    var tipoContendientelabel = $('#id_tipo_contendiente_label');
    var municipioElectoralLabel =  $('#id_municipio_label');
    var periodoElectoralLabel = $('#id_periodo_electoral_label');
    var partidoLabel = $('#id_partido_label');
    var protestaLabel = $('#id_protesta_label');
    var distritoLocalLabel = $('#id_distrito_local_label');
    var distritoFederalLabel = $('#id_distrito_federal_label');
    
    if (!candidatoActivoCheckbox.prop('checked')) {
        tipoContendienteField.hide();
        municipioElectoralField.hide();
        periodoElectoralField.hide();
        partidoField.hide();
        protestaField.hide();
        distritoLocalField.hide();
        distritoFederalField.hide();

        tipoContendientelabel.hide();
        municipioElectoralLabel.hide();
        periodoElectoralLabel.hide();
        partidoLabel.hide();
        protestaLabel.hide();
        distritoLocalLabel.hide();
        distritoFederalLabel.hide();
    }

    // Maneja la visibilidad del campo cuando cambia el estado del checkbox
    candidatoActivoCheckbox.change(function() {
        if (this.checked) {
            tipoContendienteField.show();
            municipioElectoralField.show();
            periodoElectoralField.show();
            partidoField.show();
            protestaField.show();
            
            tipoContendientelabel.show();
            municipioElectoralLabel.show();
            periodoElectoralLabel.show();
            partidoLabel.show();
            protestaLabel.show();

            $("#id_tipo_contendiente").change(function() {
                var selectedContendiente = $(this).val();
          
                // Carga el formulario correspondiente si se selecciona "Informativo"
                if (selectedContendiente === "Diputada Local" || selectedContendiente === "Diputado Local" || selectedContendiente === "Candidata a Diputación Local" || selectedContendiente === "Candidato a Diputación Local") {
                    distritoLocalField.show();
                    distritoLocalLabel.show();
                    distritoFederalField.hide();
                    distritoFederalLabel.hide();
                    municipioElectoralField.hide();
                    municipioElectoralLabel.hide();
                }else if(selectedContendiente === "Diputada Federal" || selectedContendiente === "Diputado Federal" || selectedContendiente === "Candidato a Diputación Federal" || selectedContendiente === "Candidata a Diputación Federal"){
                    distritoFederalField.show();
                    distritoFederalLabel.show();
                    distritoLocalField.hide();
                    distritoLocalLabel.hide();
                    municipioElectoralField.hide();
                    municipioElectoralLabel.hide();
                }
                else{
                    distritoLocalField.hide();
                    distritoLocalLabel.hide();
                    distritoFederalField.hide();
                    distritoFederalLabel.hide();
                    municipioElectoralField.show();
                    municipioElectoralLabel.show();
                }
            });

        } else {
            tipoContendienteField.hide();
            municipioElectoralField.hide();
            periodoElectoralField.hide();
            partidoField.hide();
            protestaField.hide();
            distritoLocalField.hide()
            distritoFederalField.hide();

            tipoContendientelabel.hide();
            municipioElectoralLabel.hide();
            periodoElectoralLabel.hide();
            partidoLabel.hide();
            protestaLabel.hide();
            distritoLocalLabel.hide();
            distritoFederalLabel.hide();
        }
    });

    // $('select[name="municipio"]').select2({
    //     theme: 'bootstrap4',
    //     language: "es",
    //     placeholder: 'Buscar Municipio ...',
    // });
    
    $('select[name="organizaciones"]').select2({
        theme: 'bootstrap4',
        language: "es",
        placeholder: 'Buscar..',
    });

    //Convertir a Mayúsculas
    $('input[name="curp"]').on('input', function(e) {
        $(this).val(function(_, val) {
          return val.toUpperCase();
        });
    });

    $('input[name="rfc"]').on('input', function(e) {
        $(this).val(function(_, val) {
          return val.toUpperCase();
        });
    });

    //MODAL EVENTOS 
    //ABRIR MODAL 
    $('.btnAddEvento').on('click', function () {
        $('#myModalEvento').modal('show');
    });

    //RESET MODAL 
    $('#myModalEvento').on('hidden.bs.modal', function (e) {
        $('#frmEvento').trigger('reset');
    })

    // Captura el evento submit del formulario vehículo con AJAX
    $('#frmEvento').on('submit', function(event) {
        event.preventDefault(); // Evita el envío normal del formulario
        var parameters = new FormData(this);
        parameters.append('action', 'add_evento');

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar registro?',
            pathname,
            parameters,
            function (response) {
                $.ajax({
                    url: '/fichas/cargar_registros/eventos/',  // URL de la vista que carga los registros
                    dataType: 'json',
                    success: function(data) {
                        var selectEventos = $('select[name="eventos"]');
                
                        $.each(data, function(index, registro) {
                            selectEventos.append('<option value="' + registro.id + '">' + registro.fecha_evento + ' ' + registro.nombre + '  </option>');
                        });
                    }
                });
                //Cerrar el modal
                $('#myModalEvento').modal('hide');
        });
    });

    //MODAL DOMICILIOS
    //ABRIR MODAL 
    $('.btnAddDomicilio').on('click', function () {
        $('#myModalDomicilio').modal('show');
    });

    //RESET MODAL 
    $('#myModalDomicilio').on('hidden.bs.modal', function (e) {
        $('#frmDomicilio').trigger('reset');
    })

    // Captura el evento submit del formulario vehículo con AJAX
    $('#frmDomicilio').on('submit', function(event) {
        event.preventDefault(); // Evita el envío normal del formulario
        var parameters = new FormData(this);
        parameters.append('action', 'add_domicilio');

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar registro?',
            pathname,
            parameters,
            function (response) {
                $.ajax({
                    url: '/fichas/cargar_registros/domicilios/',  // URL de la vista que carga los registros
                    dataType: 'json',
                    success: function(data) {
                        var selectDomicilios = $('select[name="domicilios"]');
                
                        $.each(data, function(index, registro) {
                            selectDomicilios.append('<option value="' + registro.id + '">' + registro.abrev + ' ' + registro.calle + ' ' + registro.numero_ext + ' ' + registro.numero_int + ' ' + registro.dpto + ' ' + registro.edificio + ' ' + registro.mzn + ' ' + registro.lote + ' ' + registro.colonia + ' ' + registro.municipio + ' ' + registro.estado + ' ' + registro.cp + ' </option>');
                        });
                    }
                });
                //Cerrar el modal
                $('#myModalDomicilio').modal('hide');
        });
    });

    //MODAL VEHÍCULOS
    //ABRIR MODAL
    $('.btnAddVehiculo').on('click', function () {
        $('#myModalVehiculo').modal('show');
    });

    //RESET MODAL
    $('#myModalVehiculo').on('hidden.bs.modal', function (e) {
        $('#frmvehiculo').trigger('reset');
    })

    // Captura el evento submit del formulario vehículo con AJAX
    $('#frmvehiculo').on('submit', function(event) {
        event.preventDefault(); // Evita el envío normal del formulario
        var parameters = new FormData(this);
        parameters.append('action', 'add_vehiculo');

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar registro?',
            pathname,
            parameters,
            function (response) {
                $.ajax({
                    url: '/fichas/cargar_registros/vehiculos/',  // URL de la vista que carga los registros
                    dataType: 'json',
                    success: function(data) {
                        var selectVehiculo = $('select[name="vehiculos"]');
                
                        $.each(data, function(index, registro) {
                            selectVehiculo.append('<option value="' + registro.id + '">' + registro.marca + ' ' + registro.submarca + '' + registro.modelo + ' ' + registro.color + ' ' + registro.matricula + '</option>');
                        });
                    }
                });

                //Cerrar el modal
                $('#myModalVehiculo').modal('hide');
        });
    });

    //MODAL TEMAS DE ATENCION
    //ABRIR MODAL
    $('.btnAddTemas').on('click', function () {
        $('#myModalTemas').modal('show');
    });

    //RESET MODAL
    $('#myModalTemas').on('hidden.bs.modal', function (e) {
        $('#frmTemas').trigger('reset');
    })

    // Captura el evento submit del formulario vehículo con AJAX
    $('#frmTemas').on('submit', function(event) {
        event.preventDefault(); // Evita el envío normal del formulario
        var parameters = new FormData(this);
        parameters.append('action', 'add_tema');

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar registro?',
            pathname,
            parameters,
            function (response) {
                $.ajax({
                    url: '/fichas/cargar_registros/temas/',  // URL de la vista que carga los registros
                    dataType: 'json',
                    success: function(data) {
                        var selectTema = $('select[name="temas_atencion"]');
                
                        $.each(data, function(index, registro) {
                            selectTema.append('<option value="' + registro.id + '">' + registro.nombre + '</option>');
                        });
                    }
                });

                //Cerrar el modal
                $('#myModalTemas').modal('hide');
        });
    });

    //MODAL EXPERIENCIA LABORAL
    //ABRIR MODAL EXPERIENCIA LABORAL
    $('.btnAddExperiencia').on('click', function () {
        $('#myModalExperiencia').modal('show');
    });

    //RESET MODAL EXPERIENCIA LABORAL
    $('#myModalExperiencia').on('hidden.bs.modal', function (e) {
        $('#frmExperiencia').trigger('reset');
    })

    // Captura el evento submit del formulario vehículo con AJAX
    $('#frmExperiencia').on('submit', function(event) {
        event.preventDefault(); // Evita el envío normal del formulario
        var parameters = new FormData(this);
        parameters.append('action', 'add_experiencia');

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar registro?',
            pathname,
            parameters,
            function (response) {
                $.ajax({
                    url: '/fichas/cargar_registros/experiencia/',  // URL de la vista que carga los registros
                    dataType: 'json',
                    success: function(data) {
                        var selectExperiencia = $('select[name="experiencia_laboral"]');
                
                        $.each(data, function(index, registro) {
                            selectExperiencia.append('<option value="' + registro.id + '">' + registro.nombre + ' ' + registro.dependencia + ' ' + registro.periodo + ' </option>');
                        });
                    }
                });

                //Cerrar el modal
                $('#myModalExperiencia').modal('hide');
        });
    });

    //MODAL CARGOS
    //ABRIR MODAL CARGOS
    $('.btnAddCargo').on('click', function () {
        $('#myModalCargo').modal('show');
    });

    $('#myModalCargo').on('hidden.bs.modal', function (e) {
        $('#frmCargo').trigger('reset');
    })

    // Captura el evento submit del formulario vehículo con AJAX
    $('#frmCargo').on('submit', function(event) {
        event.preventDefault(); // Evita el envío normal del formulario
        var parameters = new FormData(this);
        parameters.append('action', 'add_cargo');

        submit_formdata_with_ajax('Notificación',
            '¿Estas seguro de agregar registro?',
            pathname,
            parameters,
            function (response) {
                               
                $.ajax({
                    url: '/fichas/cargar_registros/cargos/',  // URL de la vista que carga los registros
                    dataType: 'json',
                    success: function(data) {
                        var selectCargos = $('select[name="cargos_populares"]');
                
                        $.each(data, function(index, registro) {
                            selectCargos.append('<option value="' + registro.id + '">' + registro.nombre + ' ' + registro.detalles + ' ' + registro.periodo + ' </option>');
                        });
                    }
                });

                //Cerrar el modal
                $('#myModalCargo').modal('hide');
        });
    });
});

