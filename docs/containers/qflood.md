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
<tr><td><div id="tag11442" onclick="CopyToClipboard('tag11442');return false;" class="tag-decoration">nightly</div><div id="tag11069" onclick="CopyToClipboard('tag11069');return false;" class="tag-decoration">nightly-e5bcb74</div><div id="tag853" onclick="CopyToClipboard('tag853');return false;" class="tag-decoration">nightly-5.2.4--38399927091</div><div id="tag32209" onclick="CopyToClipboard('tag32209');return false;" class="tag-decoration">nightly-v5</div><div id="tag31839" onclick="CopyToClipboard('tag31839');return false;" class="tag-decoration">nightly-v5.2</div><div id="tag28125" onclick="CopyToClipboard('tag28125');return false;" class="tag-decoration">nightly-v5.2.4</div></td><td>Nightly snapshot</td><td><a href="https://github.com/edbfi/qflood/commit/e5bcb74548566515b5faaa7189f10bc7b4ff72e5" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/38442646104" target="_blank">2026-10-13 17:55:54</a></td></tr>
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag29850" onclick="CopyToClipboard('tag29850');return false;" class="tag-decoration">release</div><div id="tag27349" onclick="CopyToClipboard('tag27349');return false;" class="tag-decoration">release-fdea43c</div><div id="tag16990" onclick="CopyToClipboard('tag16990');return false;" class="tag-decoration">release-5.2.4--4.16.3</div><div id="tag2658" onclick="CopyToClipboard('tag2658');return false;" class="tag-decoration">release-v5</div><div id="tag30255" onclick="CopyToClipboard('tag30255');return false;" class="tag-decoration">release-v5.2</div><div id="tag5994" onclick="CopyToClipboard('tag5994');return false;" class="tag-decoration">release-v5.2.4</div></td><td>Releases</td><td><a href="https://github.com/edbfi/qflood/commit/fdea43c1ce8b0f310a83b2a078a52f05ba7b4502" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/qflood/actions/runs/39056814076" target="_blank">2026-10-17 18:08:45</a></td></tr>
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
