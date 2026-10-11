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
<tr><td><div id="tag1770" onclick="CopyToClipboard('tag1770');return false;" class="tag-decoration">nightly</div><div id="tag26643" onclick="CopyToClipboard('tag26643');return false;" class="tag-decoration">nightly-02a91e1</div><div id="tag28534" onclick="CopyToClipboard('tag28534');return false;" class="tag-decoration">nightly-5.2.4--37640532677</div><div id="tag24608" onclick="CopyToClipboard('tag24608');return false;" class="tag-decoration">nightly-v5</div><div id="tag21948" onclick="CopyToClipboard('tag21948');return false;" class="tag-decoration">nightly-v5.2</div><div id="tag18326" onclick="CopyToClipboard('tag18326');return false;" class="tag-decoration">nightly-v5.2.4</div></td><td>Nightly snapshot</td><td><a href="https://github.com/edbfi/qflood/commit/02a91e18417863946c63cda934d5c83024247684" target="_blank">fix(nightly): never let the Flood version step back (#33)--version_flood__command took the first run of GitHub's list of successful Flood rolling builds, which GitHub sometimes serves stale, so the nightly version could step back to an older run for an hour. Run ids only grow, so the Flood version is now the largest of the listed runs and the current version_flood, in both version_flood__command and version__command.--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/38130714005" target="_blank">2026-10-11 10:05:37</a></td></tr>
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag3531" onclick="CopyToClipboard('tag3531');return false;" class="tag-decoration">release</div><div id="tag28763" onclick="CopyToClipboard('tag28763');return false;" class="tag-decoration">release-f1737f5</div><div id="tag5508" onclick="CopyToClipboard('tag5508');return false;" class="tag-decoration">release-5.2.4--4.16.2</div><div id="tag14884" onclick="CopyToClipboard('tag14884');return false;" class="tag-decoration">release-v5</div><div id="tag32244" onclick="CopyToClipboard('tag32244');return false;" class="tag-decoration">release-v5.2</div><div id="tag26992" onclick="CopyToClipboard('tag26992');return false;" class="tag-decoration">release-v5.2.4</div></td><td>Releases</td><td><a href="https://github.com/edbfi/qflood/commit/f1737f506060fea0dcb181c703c6522b61f2a0ae" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/37598890699" target="_blank">2026-10-07 09:11:26</a></td></tr>
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
