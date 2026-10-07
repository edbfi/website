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
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag28326" onclick="CopyToClipboard('tag28326');return false;" class="tag-decoration">release</div><div id="tag14260" onclick="CopyToClipboard('tag14260');return false;" class="tag-decoration">release-83df0ae</div><div id="tag12452" onclick="CopyToClipboard('tag12452');return false;" class="tag-decoration">release-2.11.7</div><div id="tag15807" onclick="CopyToClipboard('tag15807');return false;" class="tag-decoration">release-v2</div><div id="tag30325" onclick="CopyToClipboard('tag30325');return false;" class="tag-decoration">release-v2.11</div><div id="tag18673" onclick="CopyToClipboard('tag18673');return false;" class="tag-decoration">release-v2.11.7</div></td><td>Releases</td><td><a href="https://github.com/edbfi/caddy/commit/83df0ae7919f838179d193f7ad1f2ad90df9dd14" target="_blank">ci: add monthly immortality workflow (#25)--GitHub disables scheduled workflows in a public repository after 60 days without activity. This workflow re-enables the repository's workflows once a month with the IMMORTALITY_TOKEN personal token, which resets that counter. Owner-approved addition to the Hotio callers (2026-10-07).--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/caddy/actions/runs/37594085976" target="_blank">2026-10-07 08:29:18</a></td></tr>
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
