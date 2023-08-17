# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IamServiceAccountIamMemberArgs', 'IamServiceAccountIamMember']

@pulumi.input_type
class IamServiceAccountIamMemberArgs:
    def __init__(__self__, *,
                 member: pulumi.Input[str],
                 role: pulumi.Input[str],
                 service_account_id: pulumi.Input[str],
                 sleep_after: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a IamServiceAccountIamMember resource.
        :param pulumi.Input[str] member: Identity that will be granted the privilege in `role`.
               Entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
               * **group:{group_id}**: A unique group ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `IamServiceAccountIamBinding` can be used per role.
        :param pulumi.Input[str] service_account_id: The service account ID to apply a policy to.
        """
        pulumi.set(__self__, "member", member)
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "service_account_id", service_account_id)
        if sleep_after is not None:
            pulumi.set(__self__, "sleep_after", sleep_after)

    @property
    @pulumi.getter
    def member(self) -> pulumi.Input[str]:
        """
        Identity that will be granted the privilege in `role`.
        Entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
        * **group:{group_id}**: A unique group ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "member")

    @member.setter
    def member(self, value: pulumi.Input[str]):
        pulumi.set(self, "member", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The role that should be applied. Only one
        `IamServiceAccountIamBinding` can be used per role.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Input[str]:
        """
        The service account ID to apply a policy to.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "sleep_after")

    @sleep_after.setter
    def sleep_after(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep_after", value)


@pulumi.input_type
class _IamServiceAccountIamMemberState:
    def __init__(__self__, *,
                 member: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering IamServiceAccountIamMember resources.
        :param pulumi.Input[str] member: Identity that will be granted the privilege in `role`.
               Entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
               * **group:{group_id}**: A unique group ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `IamServiceAccountIamBinding` can be used per role.
        :param pulumi.Input[str] service_account_id: The service account ID to apply a policy to.
        """
        if member is not None:
            pulumi.set(__self__, "member", member)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if service_account_id is not None:
            pulumi.set(__self__, "service_account_id", service_account_id)
        if sleep_after is not None:
            pulumi.set(__self__, "sleep_after", sleep_after)

    @property
    @pulumi.getter
    def member(self) -> Optional[pulumi.Input[str]]:
        """
        Identity that will be granted the privilege in `role`.
        Entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
        * **group:{group_id}**: A unique group ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "member")

    @member.setter
    def member(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "member", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied. Only one
        `IamServiceAccountIamBinding` can be used per role.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The service account ID to apply a policy to.
        """
        return pulumi.get(self, "service_account_id")

    @service_account_id.setter
    def service_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_id", value)

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "sleep_after")

    @sleep_after.setter
    def sleep_after(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep_after", value)


class IamServiceAccountIamMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        When managing IAM roles, you can treat a service account either as a resource or as an identity.
        This resource is used to add IAM policy bindings to a service account resource to configure permissions
        that define who can edit the service account.

        There are three different resources that help you manage your IAM policy for a service account.
        Each of these resources is used for a different use case:

        * yandex_iam_service_account_iam_policy: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.
        * yandex_iam_service_account_iam_binding: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.
        * yandex_iam_service_account_iam_member: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role of the service account are preserved.

        > **Note:** `IamServiceAccountIamPolicy` **cannot** be used in conjunction with `IamServiceAccountIamBinding` and `IamServiceAccountIamMember` or they will conflict over what your policy should be.

        > **Note:** `IamServiceAccountIamBinding` resources **can be** used in conjunction with `IamServiceAccountIamMember` resources **only if** they do not grant privileges to the same role.

        ## yandex\\_service\\_account\\_iam\\_member

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        admin_account_iam = yandex.IamServiceAccountIamMember("admin-account-iam",
            member="userAccount:bar_user_id",
            role="admin",
            service_account_id="your-service-account-id")
        ```

        ## Import

        Service account IAM member resources can be imported using the service account ID, role and member.

        ```sh
         $ pulumi import yandex:index/iamServiceAccountIamMember:IamServiceAccountIamMember admin-account-iam "service_account_id roles/editor foo@example.com"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] member: Identity that will be granted the privilege in `role`.
               Entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
               * **group:{group_id}**: A unique group ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `IamServiceAccountIamBinding` can be used per role.
        :param pulumi.Input[str] service_account_id: The service account ID to apply a policy to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IamServiceAccountIamMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        When managing IAM roles, you can treat a service account either as a resource or as an identity.
        This resource is used to add IAM policy bindings to a service account resource to configure permissions
        that define who can edit the service account.

        There are three different resources that help you manage your IAM policy for a service account.
        Each of these resources is used for a different use case:

        * yandex_iam_service_account_iam_policy: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.
        * yandex_iam_service_account_iam_binding: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.
        * yandex_iam_service_account_iam_member: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role of the service account are preserved.

        > **Note:** `IamServiceAccountIamPolicy` **cannot** be used in conjunction with `IamServiceAccountIamBinding` and `IamServiceAccountIamMember` or they will conflict over what your policy should be.

        > **Note:** `IamServiceAccountIamBinding` resources **can be** used in conjunction with `IamServiceAccountIamMember` resources **only if** they do not grant privileges to the same role.

        ## yandex\\_service\\_account\\_iam\\_member

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        admin_account_iam = yandex.IamServiceAccountIamMember("admin-account-iam",
            member="userAccount:bar_user_id",
            role="admin",
            service_account_id="your-service-account-id")
        ```

        ## Import

        Service account IAM member resources can be imported using the service account ID, role and member.

        ```sh
         $ pulumi import yandex:index/iamServiceAccountIamMember:IamServiceAccountIamMember admin-account-iam "service_account_id roles/editor foo@example.com"
        ```

        :param str resource_name: The name of the resource.
        :param IamServiceAccountIamMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IamServiceAccountIamMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 member: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service_account_id: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IamServiceAccountIamMemberArgs.__new__(IamServiceAccountIamMemberArgs)

            if member is None and not opts.urn:
                raise TypeError("Missing required property 'member'")
            __props__.__dict__["member"] = member
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if service_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_id'")
            __props__.__dict__["service_account_id"] = service_account_id
            __props__.__dict__["sleep_after"] = sleep_after
        super(IamServiceAccountIamMember, __self__).__init__(
            'yandex:index/iamServiceAccountIamMember:IamServiceAccountIamMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            member: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            service_account_id: Optional[pulumi.Input[str]] = None,
            sleep_after: Optional[pulumi.Input[int]] = None) -> 'IamServiceAccountIamMember':
        """
        Get an existing IamServiceAccountIamMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] member: Identity that will be granted the privilege in `role`.
               Entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
               * **group:{group_id}**: A unique group ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. Only one
               `IamServiceAccountIamBinding` can be used per role.
        :param pulumi.Input[str] service_account_id: The service account ID to apply a policy to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IamServiceAccountIamMemberState.__new__(_IamServiceAccountIamMemberState)

        __props__.__dict__["member"] = member
        __props__.__dict__["role"] = role
        __props__.__dict__["service_account_id"] = service_account_id
        __props__.__dict__["sleep_after"] = sleep_after
        return IamServiceAccountIamMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def member(self) -> pulumi.Output[str]:
        """
        Identity that will be granted the privilege in `role`.
        Entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **federatedUser:{federated_user_id}:**: A unique saml federation user account ID.
        * **group:{group_id}**: A unique group ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "member")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. Only one
        `IamServiceAccountIamBinding` can be used per role.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serviceAccountId")
    def service_account_id(self) -> pulumi.Output[str]:
        """
        The service account ID to apply a policy to.
        """
        return pulumi.get(self, "service_account_id")

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "sleep_after")

