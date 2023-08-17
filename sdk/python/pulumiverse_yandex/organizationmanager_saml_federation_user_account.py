# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['OrganizationmanagerSamlFederationUserAccountArgs', 'OrganizationmanagerSamlFederationUserAccount']

@pulumi.input_type
class OrganizationmanagerSamlFederationUserAccountArgs:
    def __init__(__self__, *,
                 federation_id: pulumi.Input[str],
                 name_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a OrganizationmanagerSamlFederationUserAccount resource.
        :param pulumi.Input[str] federation_id: ID of a SAML Federation.
        :param pulumi.Input[str] name_id: Name ID of the SAML federated user.
               *
        """
        pulumi.set(__self__, "federation_id", federation_id)
        pulumi.set(__self__, "name_id", name_id)

    @property
    @pulumi.getter(name="federationId")
    def federation_id(self) -> pulumi.Input[str]:
        """
        ID of a SAML Federation.
        """
        return pulumi.get(self, "federation_id")

    @federation_id.setter
    def federation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "federation_id", value)

    @property
    @pulumi.getter(name="nameId")
    def name_id(self) -> pulumi.Input[str]:
        """
        Name ID of the SAML federated user.
        *
        """
        return pulumi.get(self, "name_id")

    @name_id.setter
    def name_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "name_id", value)


@pulumi.input_type
class _OrganizationmanagerSamlFederationUserAccountState:
    def __init__(__self__, *,
                 federation_id: Optional[pulumi.Input[str]] = None,
                 name_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OrganizationmanagerSamlFederationUserAccount resources.
        :param pulumi.Input[str] federation_id: ID of a SAML Federation.
        :param pulumi.Input[str] name_id: Name ID of the SAML federated user.
               *
        """
        if federation_id is not None:
            pulumi.set(__self__, "federation_id", federation_id)
        if name_id is not None:
            pulumi.set(__self__, "name_id", name_id)

    @property
    @pulumi.getter(name="federationId")
    def federation_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of a SAML Federation.
        """
        return pulumi.get(self, "federation_id")

    @federation_id.setter
    def federation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "federation_id", value)

    @property
    @pulumi.getter(name="nameId")
    def name_id(self) -> Optional[pulumi.Input[str]]:
        """
        Name ID of the SAML federated user.
        *
        """
        return pulumi.get(self, "name_id")

    @name_id.setter
    def name_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_id", value)


class OrganizationmanagerSamlFederationUserAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 federation_id: Optional[pulumi.Input[str]] = None,
                 name_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        account = yandex.OrganizationmanagerSamlFederationUserAccount("account",
            federation_id="some_federation_id",
            name_id="example@example.org")
        ```

        ## Import

        A Yandex SAML Federation user account can be imported using the `id` of the resource, e.g.

        ```sh
         $ pulumi import yandex:index/organizationmanagerSamlFederationUserAccount:organizationmanagerSamlFederationUserAccount account "user_id"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] federation_id: ID of a SAML Federation.
        :param pulumi.Input[str] name_id: Name ID of the SAML federated user.
               *
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrganizationmanagerSamlFederationUserAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        account = yandex.OrganizationmanagerSamlFederationUserAccount("account",
            federation_id="some_federation_id",
            name_id="example@example.org")
        ```

        ## Import

        A Yandex SAML Federation user account can be imported using the `id` of the resource, e.g.

        ```sh
         $ pulumi import yandex:index/organizationmanagerSamlFederationUserAccount:organizationmanagerSamlFederationUserAccount account "user_id"
        ```

        :param str resource_name: The name of the resource.
        :param OrganizationmanagerSamlFederationUserAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrganizationmanagerSamlFederationUserAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 federation_id: Optional[pulumi.Input[str]] = None,
                 name_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrganizationmanagerSamlFederationUserAccountArgs.__new__(OrganizationmanagerSamlFederationUserAccountArgs)

            if federation_id is None and not opts.urn:
                raise TypeError("Missing required property 'federation_id'")
            __props__.__dict__["federation_id"] = federation_id
            if name_id is None and not opts.urn:
                raise TypeError("Missing required property 'name_id'")
            __props__.__dict__["name_id"] = name_id
        super(OrganizationmanagerSamlFederationUserAccount, __self__).__init__(
            'yandex:index/organizationmanagerSamlFederationUserAccount:organizationmanagerSamlFederationUserAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            federation_id: Optional[pulumi.Input[str]] = None,
            name_id: Optional[pulumi.Input[str]] = None) -> 'OrganizationmanagerSamlFederationUserAccount':
        """
        Get an existing OrganizationmanagerSamlFederationUserAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] federation_id: ID of a SAML Federation.
        :param pulumi.Input[str] name_id: Name ID of the SAML federated user.
               *
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OrganizationmanagerSamlFederationUserAccountState.__new__(_OrganizationmanagerSamlFederationUserAccountState)

        __props__.__dict__["federation_id"] = federation_id
        __props__.__dict__["name_id"] = name_id
        return OrganizationmanagerSamlFederationUserAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="federationId")
    def federation_id(self) -> pulumi.Output[str]:
        """
        ID of a SAML Federation.
        """
        return pulumi.get(self, "federation_id")

    @property
    @pulumi.getter(name="nameId")
    def name_id(self) -> pulumi.Output[str]:
        """
        Name ID of the SAML federated user.
        *
        """
        return pulumi.get(self, "name_id")
