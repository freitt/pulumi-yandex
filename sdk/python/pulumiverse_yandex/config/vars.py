# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('yandex')


class _ExportableConfig(types.ModuleType):
    @property
    def cloud_id(self) -> Optional[str]:
        """
        ID of Yandex.Cloud tenant.
        """
        return __config__.get('cloudId')

    @property
    def endpoint(self) -> Optional[str]:
        """
        The API endpoint for Yandex.Cloud SDK client.
        """
        return __config__.get('endpoint')

    @property
    def folder_id(self) -> Optional[str]:
        """
        The default folder ID where resources will be placed.
        """
        return __config__.get('folderId')

    @property
    def insecure(self) -> Optional[bool]:
        """
        Explicitly allow the provider to perform "insecure" SSL requests. If omitted,default value is `false`.
        """
        return __config__.get_bool('insecure')

    @property
    def max_retries(self) -> Optional[int]:
        """
        The maximum number of times an API request is being executed. If the API request still fails, an error is thrown.
        """
        return __config__.get_int('maxRetries')

    @property
    def organization_id(self) -> Optional[str]:
        return __config__.get('organizationId')

    @property
    def plaintext(self) -> Optional[bool]:
        """
        Disable use of TLS. Default value is `false`.
        """
        return __config__.get_bool('plaintext')

    @property
    def profile(self) -> Optional[str]:
        """
        Profile to use in the shared credentials file. Default value is `default`.
        """
        return __config__.get('profile')

    @property
    def region_id(self) -> Optional[str]:
        return __config__.get('regionId')

    @property
    def service_account_key_file(self) -> Optional[str]:
        """
        Either the path to or the contents of a Service Account key file in JSON format.
        """
        return __config__.get('serviceAccountKeyFile')

    @property
    def shared_credentials_file(self) -> Optional[str]:
        """
        Path to shared credentials file.
        """
        return __config__.get('sharedCredentialsFile')

    @property
    def storage_access_key(self) -> Optional[str]:
        """
        Yandex.Cloud storage service access key. Used when a storage data/resource doesn't have an access key explicitly
        specified.
        """
        return __config__.get('storageAccessKey')

    @property
    def storage_endpoint(self) -> Optional[str]:
        """
        Yandex.Cloud storage service endpoint. Default is storage.yandexcloud.net
        """
        return __config__.get('storageEndpoint')

    @property
    def storage_secret_key(self) -> Optional[str]:
        """
        Yandex.Cloud storage service secret key. Used when a storage data/resource doesn't have a secret key explicitly
        specified.
        """
        return __config__.get('storageSecretKey')

    @property
    def token(self) -> Optional[str]:
        """
        The access token for API operations.
        """
        return __config__.get('token')

    @property
    def ymq_access_key(self) -> Optional[str]:
        """
        Yandex.Cloud Message Queue service access key. Used when a message queue resource doesn't have an access key explicitly
        specified.
        """
        return __config__.get('ymqAccessKey')

    @property
    def ymq_endpoint(self) -> Optional[str]:
        """
        Yandex.Cloud Message Queue service endpoint. Default is message-queue.api.cloud.yandex.net
        """
        return __config__.get('ymqEndpoint')

    @property
    def ymq_secret_key(self) -> Optional[str]:
        """
        Yandex.Cloud Message Queue service secret key. Used when a message queue resource doesn't have a secret key explicitly
        specified.
        """
        return __config__.get('ymqSecretKey')

    @property
    def zone(self) -> Optional[str]:
        """
        The zone where operations will take place. Examples are ru-central1-a, ru-central2-c, etc.
        """
        return __config__.get('zone')
