# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['LockboxSecretIamBindingArgs', 'LockboxSecretIamBinding']

@pulumi.input_type
class LockboxSecretIamBindingArgs:
    def __init__(__self__, *,
                 members: pulumi.Input[Sequence[pulumi.Input[str]]],
                 role: pulumi.Input[str],
                 secret_id: pulumi.Input[str],
                 sleep_after: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a LockboxSecretIamBinding resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        :param pulumi.Input[str] secret_id: The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        pulumi.set(__self__, "members", members)
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "secret_id", secret_id)
        if sleep_after is not None:
            pulumi.set(__self__, "sleep_after", sleep_after)

    @property
    @pulumi.getter
    def members(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Input[str]:
        """
        The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        return pulumi.get(self, "secret_id")

    @secret_id.setter
    def secret_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret_id", value)

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "sleep_after")

    @sleep_after.setter
    def sleep_after(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep_after", value)


@pulumi.input_type
class _LockboxSecretIamBindingState:
    def __init__(__self__, *,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering LockboxSecretIamBinding resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        :param pulumi.Input[str] secret_id: The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        if members is not None:
            pulumi.set(__self__, "members", members)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if secret_id is not None:
            pulumi.set(__self__, "secret_id", secret_id)
        if sleep_after is not None:
            pulumi.set(__self__, "sleep_after", sleep_after)

    @property
    @pulumi.getter
    def members(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "members")

    @members.setter
    def members(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "members", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> Optional[pulumi.Input[str]]:
        """
        The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        return pulumi.get(self, "secret_id")

    @secret_id.setter
    def secret_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_id", value)

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "sleep_after")

    @sleep_after.setter
    def sleep_after(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "sleep_after", value)


class LockboxSecretIamBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## yandex\\_lockbox\\_secret\\_iam\\_binding

        Allows creation and management of a single binding within IAM policy for
        an existing Yandex Lockbox Secret.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        your_secret = yandex.LockboxSecret("your-secret")
        viewer = yandex.LockboxSecretIamBinding("viewer",
            secret_id=your_secret.id,
            role="viewer",
            members=["userAccount:foo_user_id"])
        ```

        ## Import

        IAM binding imports use space-delimited identifiers; first the resource in question and then the role. These bindings can be imported using the `secret_id` and role, e.g.

        ```sh
         $ pulumi import yandex:index/lockboxSecretIamBinding:lockboxSecretIamBinding viewer "secret_id viewer"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        :param pulumi.Input[str] secret_id: The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LockboxSecretIamBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## yandex\\_lockbox\\_secret\\_iam\\_binding

        Allows creation and management of a single binding within IAM policy for
        an existing Yandex Lockbox Secret.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_yandex as yandex

        your_secret = yandex.LockboxSecret("your-secret")
        viewer = yandex.LockboxSecretIamBinding("viewer",
            secret_id=your_secret.id,
            role="viewer",
            members=["userAccount:foo_user_id"])
        ```

        ## Import

        IAM binding imports use space-delimited identifiers; first the resource in question and then the role. These bindings can be imported using the `secret_id` and role, e.g.

        ```sh
         $ pulumi import yandex:index/lockboxSecretIamBinding:lockboxSecretIamBinding viewer "secret_id viewer"
        ```

        :param str resource_name: The name of the resource.
        :param LockboxSecretIamBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LockboxSecretIamBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 secret_id: Optional[pulumi.Input[str]] = None,
                 sleep_after: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LockboxSecretIamBindingArgs.__new__(LockboxSecretIamBindingArgs)

            if members is None and not opts.urn:
                raise TypeError("Missing required property 'members'")
            __props__.__dict__["members"] = members
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if secret_id is None and not opts.urn:
                raise TypeError("Missing required property 'secret_id'")
            __props__.__dict__["secret_id"] = secret_id
            __props__.__dict__["sleep_after"] = sleep_after
        super(LockboxSecretIamBinding, __self__).__init__(
            'yandex:index/lockboxSecretIamBinding:lockboxSecretIamBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            members: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            role: Optional[pulumi.Input[str]] = None,
            secret_id: Optional[pulumi.Input[str]] = None,
            sleep_after: Optional[pulumi.Input[int]] = None) -> 'LockboxSecretIamBinding':
        """
        Get an existing LockboxSecretIamBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] members: Identities that will be granted the privilege in `role`.
               Each entry can have one of the following values:
               * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
               * **serviceAccount:{service_account_id}**: A unique service account ID.
               * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        :param pulumi.Input[str] role: The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        :param pulumi.Input[str] secret_id: The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LockboxSecretIamBindingState.__new__(_LockboxSecretIamBindingState)

        __props__.__dict__["members"] = members
        __props__.__dict__["role"] = role
        __props__.__dict__["secret_id"] = secret_id
        __props__.__dict__["sleep_after"] = sleep_after
        return LockboxSecretIamBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def members(self) -> pulumi.Output[Sequence[str]]:
        """
        Identities that will be granted the privilege in `role`.
        Each entry can have one of the following values:
        * **userAccount:{user_id}**: A unique user ID that represents a specific Yandex account.
        * **serviceAccount:{service_account_id}**: A unique service account ID.
        * **system:{allUsers|allAuthenticatedUsers}**: see [system groups](https://cloud.yandex.com/docs/iam/concepts/access-control/system-group)
        """
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The role that should be applied. See [roles](https://cloud.yandex.com/docs/lockbox/security/).
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> pulumi.Output[str]:
        """
        The [Yandex Lockbox Secret](https://cloud.yandex.com/docs/lockbox/) Secret ID to apply a binding to.
        """
        return pulumi.get(self, "secret_id")

    @property
    @pulumi.getter(name="sleepAfter")
    def sleep_after(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "sleep_after")

