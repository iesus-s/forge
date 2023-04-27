# forge

On-premises Universal Blue

This repo is intended to provide the service units necessary to set up a
self-hosted OS forge for custom images.

## Vision

Imagine something like a home lab or a university lab:

1. Deploy forge
2. Go into the WebUI, clone in your favorite uBlue repo and make changes
3. Forge automatically starts to build the images
4. PXE boot the clients, select ublue in the menu
5. Eat tacos
6. Return to a fully deployed lab with centralized package management

## What we have so far

We are still working on making the vision a reality. The following has been
implemented so far:

### Certificate Authority

We use a [Minica](https://github.com/jsha/minica) as simple CA to generate a
key pair and a root certificate for `*.ublue.local`. The wildcard certificate is
then made available to all other components and are valid for 2 years and 30 days.

### Container Registry

As container registry we make use of the [Docker Registry 2.0](https://hub.docker.com/_/registry/)
implementation for storing and distributing container images

The container registry is available at `registry.ublue.local:9001`

## Firing Up the Forge

To heat up the forge run `podman play kube forge-pod.yml --build`.
