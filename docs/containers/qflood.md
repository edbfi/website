---
hide:
  - toc
title: edbfi/qflood
---

[:octicons-mark-github-16: GitHub](https://github.com/edbfi/qflood){ class="header-links" target="_blank" rel="noopener" }
[:octicons-container-16: ghcr.io](https://github.com/users/edbfi/packages/container/package/qflood){ class="header-links" target="_blank" rel="noopener" }

[:octicons-link-16: Upstream Project](https://github.com/jesec/flood){ class="header-links" target="_blank" rel="noopener" }

<div class="image-logo"><img src="/img/image-logos/qflood.svg" alt="logo"></div>

!!! question "What is this?"

    This is a fork of Hotio's [rflood](https://hotio.dev/containers/rflood) Docker image, that uses qBittorrent instead of rtorrent. The qflood image provides a release build and a pinned nightly snapshot. The included [qBittorrent](https://github.com/userdocs/qbittorrent-nox-static) uses libtorrent v2.x.

???+ info "What is nightly?"

    Nightly uses a pinned snapshot from the [Flood rolling build](https://github.com/jesec/flood/actions/workflows/publish-rolling.yml). Updates are reviewed and tested on both architectures before manual publication.

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
<tr><td><div id="tag23421" onclick="CopyToClipboard('tag23421');return false;" class="tag-decoration">nightly</div><div id="tag11510" onclick="CopyToClipboard('tag11510');return false;" class="tag-decoration">nightly-17b1787</div><div id="tag26313" onclick="CopyToClipboard('tag26313');return false;" class="tag-decoration">nightly-5.3.0--43020125678</div><div id="tag28733" onclick="CopyToClipboard('tag28733');return false;" class="tag-decoration">nightly-v5</div><div id="tag11647" onclick="CopyToClipboard('tag11647');return false;" class="tag-decoration">nightly-v5.3</div><div id="tag1607" onclick="CopyToClipboard('tag1607');return false;" class="tag-decoration">nightly-v5.3.0</div></td><td>Nightly snapshot</td><td><a href="https://github.com/edbfi/qflood/commit/17b178783dda5f17573a47e6ef13c0ea3cb4ce4c" target="_blank">docs(readme): refine nightly qflood header and setup prose (#37)--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/43328685231" target="_blank">2026-11-12 23:25:04</a></td></tr>
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag18468" onclick="CopyToClipboard('tag18468');return false;" class="tag-decoration">release</div><div id="tag30173" onclick="CopyToClipboard('tag30173');return false;" class="tag-decoration">release-545a38e</div><div id="tag16444" onclick="CopyToClipboard('tag16444');return false;" class="tag-decoration">release-5.3.0--4.16.4</div><div id="tag3567" onclick="CopyToClipboard('tag3567');return false;" class="tag-decoration">release-v5</div><div id="tag31446" onclick="CopyToClipboard('tag31446');return false;" class="tag-decoration">release-v5.3</div><div id="tag10518" onclick="CopyToClipboard('tag10518');return false;" class="tag-decoration">release-v5.3.0</div></td><td>Releases</td><td><a href="https://github.com/edbfi/qflood/commit/545a38e8c229c2bc286d3a5f95222e4dfeceb9c1" target="_blank">docs: add CI status to README badges (#38)--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/43399065472" target="_blank">2026-11-13 09:10:11</a></td></tr>
</tbody>
  </table>
</div>

## Starting the container

=== "cli"

    ```shell linenums="1"
    docker run --rm \
        --name qflood \
        -p 8080:8080 \
        -p 3000:3000 \
        -e PUID=1000 \
        -e PGID=1000 \
        -e UMASK=002 \
        -e TZ="Etc/UTC" \
        -e LIBTORRENT="v2" \
        -e FLOOD_AUTH="true" \
        -e ARGS="" \
        -e FLOOD_ARGS="" \
        -v /<host_folder_config>:/config \
        -v /<host_folder_data>:/data \
        ghcr.io/edbfi/qflood
    ```

=== "compose"

    ```yaml linenums="1"
    services:
      qflood:
        container_name: qflood
        image: ghcr.io/edbfi/qflood
        ports:
          - "8080:8080"
          - "3000:3000"
        environment:
          - PUID=1000
          - PGID=1000
          - UMASK=002
          - TZ=Etc/UTC
          - LIBTORRENT=v2
          - FLOOD_AUTH=true
          - ARGS
          - FLOOD_ARGS
        volumes:
          - /<host_folder_config>:/config
          - /<host_folder_data>:/data
    ```

## Connecting Flood to qBittorrent

With `FLOOD_AUTH=true`, create a Flood account and configure its qBittorrent connection at `http://127.0.0.1:8080` using the qBittorrent Web UI credentials. qBittorrent prints its temporary initial password in the container logs; set a persistent password in its preferences.

The optional `FLOOD_AUTH=false` mode expects qBittorrent to allow localhost access. This is an explicit configuration choice; the image does not change qBittorrent authentication settings automatically.

## Changing the WebUI port

Under certain circumstances it's required to run the WebUI on a different internal port, you can do that by modifying the environment variable `WEBUI_PORTS` accordingly. Use `8080/tcp,3000/tcp` by default: the first port is qBittorrent and the second is Flood. Update the published Docker ports to match any changes.

--8<-- "includes/wireguard.md"
