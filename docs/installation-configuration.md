---
title: Yandex Installation & Configuration
meta_desc: Information on how to install the Yandex provider.
layout: installation
---

## Installation

The Pulumi Yandex provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@pulumiverse/yandex`](https://www.npmjs.com/package/@pulumiverse/yandex)
* Python: [`pulumiverse_yandex`](https://pypi.org/project/pulumiverse_yandex/)
* Go: [`github.com/freitt/pulumi-yandex/sdk/go/yandex`](https://pkg.go.dev/github.com/freitt/pulumi-yandex/sdk/go/yandex)
* .NET: [`Pulumiverse.Yandex`](https://www.nuget.org/packages/Pulumiverse.Yandex)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `yandex` provider:

- `yandex:apiKey` (environment: `yandex_API_KEY`) - the API key for `yandex`
- `yandex:region` (environment: `yandex_REGION`) - the region in which to deploy resources

### Provider Binary

The Yandex provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource yandex <version>
```

Replace the version string `<version>` with your desired version.
