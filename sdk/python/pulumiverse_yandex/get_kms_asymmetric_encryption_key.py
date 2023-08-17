# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetKmsAsymmetricEncryptionKeyResult',
    'AwaitableGetKmsAsymmetricEncryptionKeyResult',
    'get_kms_asymmetric_encryption_key',
    'get_kms_asymmetric_encryption_key_output',
]

@pulumi.output_type
class GetKmsAsymmetricEncryptionKeyResult:
    """
    A collection of values returned by getKmsAsymmetricEncryptionKey.
    """
    def __init__(__self__, asymmetric_encryption_key_id=None, created_at=None, deletion_protection=None, description=None, encryption_algorithm=None, folder_id=None, id=None, labels=None, name=None, status=None):
        if asymmetric_encryption_key_id and not isinstance(asymmetric_encryption_key_id, str):
            raise TypeError("Expected argument 'asymmetric_encryption_key_id' to be a str")
        pulumi.set(__self__, "asymmetric_encryption_key_id", asymmetric_encryption_key_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encryption_algorithm and not isinstance(encryption_algorithm, str):
            raise TypeError("Expected argument 'encryption_algorithm' to be a str")
        pulumi.set(__self__, "encryption_algorithm", encryption_algorithm)
        if folder_id and not isinstance(folder_id, str):
            raise TypeError("Expected argument 'folder_id' to be a str")
        pulumi.set(__self__, "folder_id", folder_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="asymmetricEncryptionKeyId")
    def asymmetric_encryption_key_id(self) -> str:
        return pulumi.get(self, "asymmetric_encryption_key_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[bool]:
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptionAlgorithm")
    def encryption_algorithm(self) -> Optional[str]:
        return pulumi.get(self, "encryption_algorithm")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> str:
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, str]]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")


class AwaitableGetKmsAsymmetricEncryptionKeyResult(GetKmsAsymmetricEncryptionKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKmsAsymmetricEncryptionKeyResult(
            asymmetric_encryption_key_id=self.asymmetric_encryption_key_id,
            created_at=self.created_at,
            deletion_protection=self.deletion_protection,
            description=self.description,
            encryption_algorithm=self.encryption_algorithm,
            folder_id=self.folder_id,
            id=self.id,
            labels=self.labels,
            name=self.name,
            status=self.status)


def get_kms_asymmetric_encryption_key(asymmetric_encryption_key_id: Optional[str] = None,
                                      deletion_protection: Optional[bool] = None,
                                      description: Optional[str] = None,
                                      encryption_algorithm: Optional[str] = None,
                                      folder_id: Optional[str] = None,
                                      labels: Optional[Mapping[str, str]] = None,
                                      name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKmsAsymmetricEncryptionKeyResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['asymmetricEncryptionKeyId'] = asymmetric_encryption_key_id
    __args__['deletionProtection'] = deletion_protection
    __args__['description'] = description
    __args__['encryptionAlgorithm'] = encryption_algorithm
    __args__['folderId'] = folder_id
    __args__['labels'] = labels
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('yandex:index/getKmsAsymmetricEncryptionKey:getKmsAsymmetricEncryptionKey', __args__, opts=opts, typ=GetKmsAsymmetricEncryptionKeyResult).value

    return AwaitableGetKmsAsymmetricEncryptionKeyResult(
        asymmetric_encryption_key_id=__ret__.asymmetric_encryption_key_id,
        created_at=__ret__.created_at,
        deletion_protection=__ret__.deletion_protection,
        description=__ret__.description,
        encryption_algorithm=__ret__.encryption_algorithm,
        folder_id=__ret__.folder_id,
        id=__ret__.id,
        labels=__ret__.labels,
        name=__ret__.name,
        status=__ret__.status)


@_utilities.lift_output_func(get_kms_asymmetric_encryption_key)
def get_kms_asymmetric_encryption_key_output(asymmetric_encryption_key_id: Optional[pulumi.Input[str]] = None,
                                             deletion_protection: Optional[pulumi.Input[Optional[bool]]] = None,
                                             description: Optional[pulumi.Input[Optional[str]]] = None,
                                             encryption_algorithm: Optional[pulumi.Input[Optional[str]]] = None,
                                             folder_id: Optional[pulumi.Input[Optional[str]]] = None,
                                             labels: Optional[pulumi.Input[Optional[Mapping[str, str]]]] = None,
                                             name: Optional[pulumi.Input[Optional[str]]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKmsAsymmetricEncryptionKeyResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...