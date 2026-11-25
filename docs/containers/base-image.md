---
hide:
  - toc
title: edbfi/base-image
---

[:octicons-mark-github-16: GitHub](https://github.com/edbfi/base-image){ class="header-links" target="_blank" rel="noopener" }
[:octicons-container-16: ghcr.io](https://github.com/users/edbfi/packages/container/package/base-image){ class="header-links" target="_blank" rel="noopener" }

[:octicons-link-16: Upstream Project](https://github.com/hotio/base){ class="header-links" target="_blank" rel="noopener" }

<div class="image-logo"><img src="/img/image-logos/base-image.svg" alt="logo"></div>

!!! question "What is this?"

    This is a fork of Hotio's Docker image. It's used for my other Docker images. It's basically the same as Hotio's except that it's tailored to my containers.

<div id="tags-table">
  <table>
    <thead>
      <tr>
        <th>Tags <span class="twemoji" title="Click Tag to Copy"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M11 9h2V7h-2m1 13c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8m0-18A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2m-1 15h2v-6h-2z"></path></svg></span></th>
        <th>Description</th>
        <th>Commit</th>
        <th>Last Updated</th>
      </tr>
    </thead>
    <tbody id="tags-table-body">
<tr><td><div id="tag24374" onclick="CopyToClipboard('tag24374');return false;" class="tag-decoration">alpinevpn</div><div id="tag4812" onclick="CopyToClipboard('tag4812');return false;" class="tag-decoration">alpinevpn-ef2e1cf</div></td><td>Alpine 3.23</td><td><a href="https://github.com/edbfi/base-image/commit/ef2e1cfdaf796742325433a0f69cb6108c153968" target="_blank">Modified: packages.txt</a></td><td><a href="https://github.com/edbfi/base-image/actions/runs/45641302580" target="_blank">2026-11-25 15:05:52</a></td></tr>
<tr><td><div id="tag19278" onclick="CopyToClipboard('tag19278');return false;" class="tag-decoration">noblevpn</div><div id="tag27933" onclick="CopyToClipboard('tag27933');return false;" class="tag-decoration">noblevpn-379c932</div></td><td>Ubuntu 24.04</td><td><a href="https://github.com/edbfi/base-image/commit/379c9321658d32cd6deed3f574c47c5e001dd391" target="_blank">Modified: packages.txt</a></td><td><a href="https://github.com/edbfi/base-image/actions/runs/45724495028" target="_blank">2026-11-25 23:51:24</a></td></tr>
</tbody>
  </table>
</div>

## Starting the container

=== "cli"

    ```shell linenums="1"
    docker run --rm \
        --name base-image \
        -e PUID=1000 \
        -e PGID=1000 \
        -e UMASK=002 \
        -e TZ="Etc/UTC" \
        -v /<host_folder_config>:/config \
        ghcr.io/edbfi/base-image:alpinevpn
    ```

=== "compose"

    ```yaml linenums="1"
    services:
      base-image:
        container_name: base-image
        image: ghcr.io/edbfi/base-image:alpinevpn
        environment:
          - PUID=1000
          - PGID=1000
          - UMASK=002
          - TZ=Etc/UTC
        volumes:
          - /<host_folder_config>:/config
    ```

This image is the base-image image for all other application images, however it can be used as a standalone VPN image for other images to attach to.

--8<-- "includes/wireguard.md"
