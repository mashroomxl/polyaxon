from marshmallow.exceptions import ValidationError as MarshmallowValidationError
from rest_framework.exceptions import ValidationError

from django.core.exceptions import ValidationError as DjangoValidationError

from polyaxon_schemas.exceptions import PolyaxonConfigurationError, PolyaxonfileError
from polyaxon_schemas.polyaxonfile.specification import (
    BuildSpecification,
    ExperimentSpecification,
    GroupSpecification,
    PluginSpecification,
    JobSpecification,
)
from polyaxon_schemas.settings import SettingsConfig


def validate_experiment_spec_config(config, raise_for_rest=False):
    try:
        spec = ExperimentSpecification.read(config)
    except (PolyaxonfileError, PolyaxonConfigurationError) as e:
        message_error = 'Received non valid specification config. %s' % e
        if raise_for_rest:
            raise ValidationError(message_error)
        else:
            raise DjangoValidationError(message_error)

    return spec


def validate_group_spec_content(content, raise_for_rest=False):
    try:
        spec = GroupSpecification.read(content)
    except (PolyaxonfileError, PolyaxonConfigurationError) as e:
        message_error = 'Received non valid specification content. %s' % e
        if raise_for_rest:
            raise ValidationError(message_error)
        else:
            raise DjangoValidationError(message_error)

    return spec


def validate_group_params_config(config, raise_for_rest=False):
    try:
        SettingsConfig.from_dict(config)
    except MarshmallowValidationError as e:
        if raise_for_rest:
            raise ValidationError(e)
        else:
            raise DjangoValidationError(e)


def validate_plugin_spec_config(config, raise_for_rest=False):
    try:
        spec = PluginSpecification.read(config)
    except (PolyaxonfileError, PolyaxonConfigurationError) as e:
        message_error = 'Received non valid plugin specification config. %s' % e
        if raise_for_rest:
            raise ValidationError(message_error)
        else:
            raise DjangoValidationError(message_error)

    return spec


def validate_build_spec_config(config, raise_for_rest=False):
    try:
        spec = BuildSpecification.read(config)
    except (PolyaxonfileError, PolyaxonConfigurationError) as e:
        message_error = 'Received non valid build specification config. %s' % e
        if raise_for_rest:
            raise ValidationError(message_error)
        else:
            raise DjangoValidationError(message_error)

    return spec


def validate_job_spec_config(config, raise_for_rest=False):
    try:
        spec = JobSpecification.read(config)
    except (PolyaxonfileError, PolyaxonConfigurationError) as e:
        message_error = 'Received non valid job specification config. %s' % e
        if raise_for_rest:
            raise ValidationError(message_error)
        else:
            raise DjangoValidationError(message_error)

    return spec
