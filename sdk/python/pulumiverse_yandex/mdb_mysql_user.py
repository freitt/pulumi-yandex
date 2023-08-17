# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['MdbMysqlUserArgs', 'MdbMysqlUser']

@pulumi.input_type
class MdbMysqlUserArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 password: pulumi.Input[str],
                 authentication_plugin: Optional[pulumi.Input[str]] = None,
                 connection_limits: Optional[pulumi.Input['MdbMysqlUserConnectionLimitsArgs']] = None,
                 global_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]]] = None):
        """
        The set of arguments for constructing a MdbMysqlUser resource.
        :param pulumi.Input[str] password: The password of the user.
        :param pulumi.Input[str] authentication_plugin: Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        :param pulumi.Input['MdbMysqlUserConnectionLimitsArgs'] connection_limits: User's connection limits. The structure is documented below.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] global_permissions: List user's global permissions     
               Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]] permissions: Set of permissions granted to the user. The structure is documented below.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "password", password)
        if authentication_plugin is not None:
            pulumi.set(__self__, "authentication_plugin", authentication_plugin)
        if connection_limits is not None:
            pulumi.set(__self__, "connection_limits", connection_limits)
        if global_permissions is not None:
            pulumi.set(__self__, "global_permissions", global_permissions)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        """
        The password of the user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="authenticationPlugin")
    def authentication_plugin(self) -> Optional[pulumi.Input[str]]:
        """
        Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        """
        return pulumi.get(self, "authentication_plugin")

    @authentication_plugin.setter
    def authentication_plugin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_plugin", value)

    @property
    @pulumi.getter(name="connectionLimits")
    def connection_limits(self) -> Optional[pulumi.Input['MdbMysqlUserConnectionLimitsArgs']]:
        """
        User's connection limits. The structure is documented below.
        If the attribute is not specified there will be no changes.
        """
        return pulumi.get(self, "connection_limits")

    @connection_limits.setter
    def connection_limits(self, value: Optional[pulumi.Input['MdbMysqlUserConnectionLimitsArgs']]):
        pulumi.set(self, "connection_limits", value)

    @property
    @pulumi.getter(name="globalPermissions")
    def global_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List user's global permissions     
        Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
        If the attribute is not specified there will be no changes.
        """
        return pulumi.get(self, "global_permissions")

    @global_permissions.setter
    def global_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "global_permissions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]]]:
        """
        Set of permissions granted to the user. The structure is documented below.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]]]):
        pulumi.set(self, "permissions", value)


@pulumi.input_type
class _MdbMysqlUserState:
    def __init__(__self__, *,
                 authentication_plugin: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 connection_limits: Optional[pulumi.Input['MdbMysqlUserConnectionLimitsArgs']] = None,
                 global_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]]] = None):
        """
        Input properties used for looking up and filtering MdbMysqlUser resources.
        :param pulumi.Input[str] authentication_plugin: Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        :param pulumi.Input['MdbMysqlUserConnectionLimitsArgs'] connection_limits: User's connection limits. The structure is documented below.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] global_permissions: List user's global permissions     
               Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password of the user.
        :param pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]] permissions: Set of permissions granted to the user. The structure is documented below.
        """
        if authentication_plugin is not None:
            pulumi.set(__self__, "authentication_plugin", authentication_plugin)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if connection_limits is not None:
            pulumi.set(__self__, "connection_limits", connection_limits)
        if global_permissions is not None:
            pulumi.set(__self__, "global_permissions", global_permissions)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter(name="authenticationPlugin")
    def authentication_plugin(self) -> Optional[pulumi.Input[str]]:
        """
        Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        """
        return pulumi.get(self, "authentication_plugin")

    @authentication_plugin.setter
    def authentication_plugin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_plugin", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="connectionLimits")
    def connection_limits(self) -> Optional[pulumi.Input['MdbMysqlUserConnectionLimitsArgs']]:
        """
        User's connection limits. The structure is documented below.
        If the attribute is not specified there will be no changes.
        """
        return pulumi.get(self, "connection_limits")

    @connection_limits.setter
    def connection_limits(self, value: Optional[pulumi.Input['MdbMysqlUserConnectionLimitsArgs']]):
        pulumi.set(self, "connection_limits", value)

    @property
    @pulumi.getter(name="globalPermissions")
    def global_permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List user's global permissions     
        Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
        If the attribute is not specified there will be no changes.
        """
        return pulumi.get(self, "global_permissions")

    @global_permissions.setter
    def global_permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "global_permissions", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the user.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]]]:
        """
        Set of permissions granted to the user. The structure is documented below.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MdbMysqlUserPermissionArgs']]]]):
        pulumi.set(self, "permissions", value)


class MdbMysqlUser(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_plugin: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 connection_limits: Optional[pulumi.Input[pulumi.InputType['MdbMysqlUserConnectionLimitsArgs']]] = None,
                 global_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbMysqlUserPermissionArgs']]]]] = None,
                 __props__=None):
        """
        Manages a MySQL user within the Yandex.Cloud. For more information, see
        [the official documentation](https://cloud.yandex.com/docs/managed-mysql/).

        ## Import

        A MySQL user can be imported using the following format

        ```sh
         $ pulumi import yandex:index/mdbMysqlUser:mdbMysqlUser foo {{cluster_id}}:{{username}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_plugin: Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        :param pulumi.Input[pulumi.InputType['MdbMysqlUserConnectionLimitsArgs']] connection_limits: User's connection limits. The structure is documented below.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] global_permissions: List user's global permissions     
               Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password of the user.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbMysqlUserPermissionArgs']]]] permissions: Set of permissions granted to the user. The structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MdbMysqlUserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a MySQL user within the Yandex.Cloud. For more information, see
        [the official documentation](https://cloud.yandex.com/docs/managed-mysql/).

        ## Import

        A MySQL user can be imported using the following format

        ```sh
         $ pulumi import yandex:index/mdbMysqlUser:mdbMysqlUser foo {{cluster_id}}:{{username}}
        ```

        :param str resource_name: The name of the resource.
        :param MdbMysqlUserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MdbMysqlUserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_plugin: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 connection_limits: Optional[pulumi.Input[pulumi.InputType['MdbMysqlUserConnectionLimitsArgs']]] = None,
                 global_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbMysqlUserPermissionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MdbMysqlUserArgs.__new__(MdbMysqlUserArgs)

            __props__.__dict__["authentication_plugin"] = authentication_plugin
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["connection_limits"] = connection_limits
            __props__.__dict__["global_permissions"] = global_permissions
            __props__.__dict__["name"] = name
            if password is None and not opts.urn:
                raise TypeError("Missing required property 'password'")
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["permissions"] = permissions
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(MdbMysqlUser, __self__).__init__(
            'yandex:index/mdbMysqlUser:mdbMysqlUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            authentication_plugin: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            connection_limits: Optional[pulumi.Input[pulumi.InputType['MdbMysqlUserConnectionLimitsArgs']]] = None,
            global_permissions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbMysqlUserPermissionArgs']]]]] = None) -> 'MdbMysqlUser':
        """
        Get an existing MdbMysqlUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_plugin: Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        :param pulumi.Input[pulumi.InputType['MdbMysqlUserConnectionLimitsArgs']] connection_limits: User's connection limits. The structure is documented below.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] global_permissions: List user's global permissions     
               Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
               If the attribute is not specified there will be no changes.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password of the user.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['MdbMysqlUserPermissionArgs']]]] permissions: Set of permissions granted to the user. The structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MdbMysqlUserState.__new__(_MdbMysqlUserState)

        __props__.__dict__["authentication_plugin"] = authentication_plugin
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["connection_limits"] = connection_limits
        __props__.__dict__["global_permissions"] = global_permissions
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["permissions"] = permissions
        return MdbMysqlUser(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authenticationPlugin")
    def authentication_plugin(self) -> pulumi.Output[str]:
        """
        Authentication plugin. Allowed values: `MYSQL_NATIVE_PASSWORD`, `CACHING_SHA2_PASSWORD`, `SHA256_PASSWORD` (for version 5.7 `MYSQL_NATIVE_PASSWORD`, `SHA256_PASSWORD`)
        """
        return pulumi.get(self, "authentication_plugin")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="connectionLimits")
    def connection_limits(self) -> pulumi.Output['outputs.MdbMysqlUserConnectionLimits']:
        """
        User's connection limits. The structure is documented below.
        If the attribute is not specified there will be no changes.
        """
        return pulumi.get(self, "connection_limits")

    @property
    @pulumi.getter(name="globalPermissions")
    def global_permissions(self) -> pulumi.Output[Sequence[str]]:
        """
        List user's global permissions     
        Allowed permissions:  `REPLICATION_CLIENT`, `REPLICATION_SLAVE`, `PROCESS` for clear list use empty list.
        If the attribute is not specified there will be no changes.
        """
        return pulumi.get(self, "global_permissions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        The password of the user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Sequence['outputs.MdbMysqlUserPermission']]:
        """
        Set of permissions granted to the user. The structure is documented below.
        """
        return pulumi.get(self, "permissions")

