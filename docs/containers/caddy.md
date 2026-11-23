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
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag1477" onclick="CopyToClipboard('tag1477');return false;" class="tag-decoration">release</div><div id="tag272" onclick="CopyToClipboard('tag272');return false;" class="tag-decoration">release-9720fe1</div><div id="tag30906" onclick="CopyToClipboard('tag30906');return false;" class="tag-decoration">release-2.11.7</div><div id="tag21054" onclick="CopyToClipboard('tag21054');return false;" class="tag-decoration">release-v2</div><div id="tag17053" onclick="CopyToClipboard('tag17053');return false;" class="tag-decoration">release-v2.11</div><div id="tag31903" onclick="CopyToClipboard('tag31903');return false;" class="tag-decoration">release-v2.11.7</div></td><td>Releases</td><td><a href="https://github.com/edbfi/caddy/commit/9720fe117e3a9f0e1f84a630021944251e8f6b3e" target="_blank">docs: add CI status to README badges (#28)--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/caddy/actions/runs/43399089185" target="_blank">2026-11-13 09:10:21</a></td></tr>
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
