---
hide:
  - toc
title: edbfi/caddy
---

[:octicons-mark-github-16: GitHub](https://github.com/edbfi/caddy){ class="header-links" target="_blank" rel="noopener" }
[:octicons-container-16: ghcr.io](https://github.com/users/edbfi/packages/container/package/caddy){ class="header-links" target="_blank" rel="noopener" }

[:octicons-link-16: Upstream Project](https://caddyserver.com){ class="header-links" target="_blank" rel="noopener" }

<div class="image-logo"><img src="/img/image-logos/caddy.svg" alt="logo"></div>

!!! question "What is this?"

    A Docker image with [Caddy 2](https://caddyserver.com){: target=_blank rel="noopener" } including DNS modules for [Cloudflare](https://github.com/caddy-dns/cloudflare){: target=_blank rel="noopener" }, [Njalla](https://github.com/caddy-dns/njalla){: target=_blank rel="noopener" }, and [rate limiting](https://github.com/mholt/caddy-ratelimit){: target=_blank rel="noopener" }. The default configuration restricts access to private IP ranges only.

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
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag31316" onclick="CopyToClipboard('tag31316');return false;" class="tag-decoration">release</div><div id="tag25865" onclick="CopyToClipboard('tag25865');return false;" class="tag-decoration">release-f936ee6</div><div id="tag11912" onclick="CopyToClipboard('tag11912');return false;" class="tag-decoration">release-2.11.7</div><div id="tag1716" onclick="CopyToClipboard('tag1716');return false;" class="tag-decoration">release-v2</div><div id="tag31959" onclick="CopyToClipboard('tag31959');return false;" class="tag-decoration">release-v2.11</div><div id="tag5679" onclick="CopyToClipboard('tag5679');return false;" class="tag-decoration">release-v2.11.7</div></td><td>Releases</td><td><a href="https://github.com/edbfi/caddy/commit/f936ee6dd955b32e428b38bcd18179e41a1dbabd" target="_blank">docs(readme): shrink logo and simplify container overview (#27)--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/caddy/actions/runs/43316570713" target="_blank">2026-11-12 22:05:15</a></td></tr>
</tbody>
  </table>
</div>

## Starting the container

=== "cli"

    ```shell linenums="1"
    docker run --rm \
        --name caddy \
        -p 80:8080 \
        -p 443:8443 \
        -e PUID=1000 \
        -e PGID=1000 \
        -e UMASK=002 \
        -e TZ="Etc/UTC" \
        -e CUSTOM_BUILD="" \
        -v /<host_folder_config>:/config \
        ghcr.io/edbfi/caddy
    ```

=== "compose"

    ```yaml linenums="1"
    services:
      caddy:
        container_name: caddy
        image: ghcr.io/edbfi/caddy
        ports:
          - "80:8080"
          - "443:8443"
        environment:
          - PUID=1000
          - PGID=1000
          - UMASK=002
          - TZ=Etc/UTC
          - CUSTOM_BUILD
        volumes:
          - /<host_folder_config>:/config
    ```

## Custom build

If you set the environment variable `CUSTOM_BUILD` to a file location like for example `/config/caddy_linux_amd64_custom`, an attempt is made to start Caddy with that binary. The custom build can be obtained from the Caddy [download](https://caddyserver.com/download){: target=\_blank rel="noopener" } page. This is particularly useful if you need extra modules.

--8<-- "includes/wireguard.md"
