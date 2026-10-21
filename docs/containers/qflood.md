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
<tr><td><div id="tag7895" onclick="CopyToClipboard('tag7895');return false;" class="tag-decoration">nightly</div><div id="tag17448" onclick="CopyToClipboard('tag17448');return false;" class="tag-decoration">nightly-84564d1</div><div id="tag10334" onclick="CopyToClipboard('tag10334');return false;" class="tag-decoration">nightly-5.2.4--39289591022</div><div id="tag4521" onclick="CopyToClipboard('tag4521');return false;" class="tag-decoration">nightly-v5</div><div id="tag16973" onclick="CopyToClipboard('tag16973');return false;" class="tag-decoration">nightly-v5.2</div><div id="tag12520" onclick="CopyToClipboard('tag12520');return false;" class="tag-decoration">nightly-v5.2.4</div></td><td>Nightly snapshot</td><td><a href="https://github.com/edbfi/qflood/commit/84564d1a6f0bf501ba66a0421cbb2054af522022" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/39307183644" target="_blank">2026-10-19 18:59:32</a></td></tr>
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag28476" onclick="CopyToClipboard('tag28476');return false;" class="tag-decoration">release</div><div id="tag2428" onclick="CopyToClipboard('tag2428');return false;" class="tag-decoration">release-0110dd9</div><div id="tag19453" onclick="CopyToClipboard('tag19453');return false;" class="tag-decoration">release-5.3.0--4.16.3</div><div id="tag23806" onclick="CopyToClipboard('tag23806');return false;" class="tag-decoration">release-v5</div><div id="tag11762" onclick="CopyToClipboard('tag11762');return false;" class="tag-decoration">release-v5.3</div><div id="tag10963" onclick="CopyToClipboard('tag10963');return false;" class="tag-decoration">release-v5.3.0</div></td><td>Releases</td><td><a href="https://github.com/edbfi/qflood/commit/0110dd94ce8677ed5d965ce4c4d0b778e93af727" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/39473752215" target="_blank">2026-10-20 18:19:36</a></td></tr>
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
