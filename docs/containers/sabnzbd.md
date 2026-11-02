---
hide:
  - toc
title: edbfi/sabnzbd
---

[:octicons-mark-github-16: GitHub](https://github.com/edbfi/sabnzbd){ class="header-links" target="_blank" rel="noopener" }
[:octicons-container-16: ghcr.io](https://github.com/users/edbfi/packages/container/package/sabnzbd){ class="header-links" target="_blank" rel="noopener" }

[:octicons-link-16: Upstream Project](https://sabnzbd.org){ class="header-links" target="_blank" rel="noopener" }

<div class="image-logo"><img src="/img/image-logos/sabnzbd.svg" alt="logo"></div>

!!! question "What is this?"

    This is a fork of Hotio's [SABnzbd](https://hotio.dev/containers/sabnzbd) Docker image, that includes ffprobe, at `/app/bin/ffprobe`. Useful for scripts.

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
<tr><td><div id="tag19388" onclick="CopyToClipboard('tag19388');return false;" class="tag-decoration">nightly</div><div id="tag30685" onclick="CopyToClipboard('tag30685');return false;" class="tag-decoration">nightly-37a9551</div><div id="tag3940" onclick="CopyToClipboard('tag3940');return false;" class="tag-decoration">nightly-ac75c14084705c9e66d3df21bf74c7617ade7ee3</div></td><td>Every commit to develop</td><td><a href="https://github.com/edbfi/sabnzbd/commit/37a95514aeb8fe25abcb5f9e31ceb9bc421385c1" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/sabnzbd/actions/runs/37649795125" target="_blank">2026-10-07 16:09:07</a></td></tr>
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag5680" onclick="CopyToClipboard('tag5680');return false;" class="tag-decoration">release</div><div id="tag32133" onclick="CopyToClipboard('tag32133');return false;" class="tag-decoration">release-05c2c1c</div><div id="tag6421" onclick="CopyToClipboard('tag6421');return false;" class="tag-decoration">release-5.1.3</div><div id="tag29858" onclick="CopyToClipboard('tag29858');return false;" class="tag-decoration">release-v5</div><div id="tag16877" onclick="CopyToClipboard('tag16877');return false;" class="tag-decoration">release-v5.1</div><div id="tag13349" onclick="CopyToClipboard('tag13349');return false;" class="tag-decoration">release-v5.1.3</div></td><td>Releases</td><td><a href="https://github.com/edbfi/sabnzbd/commit/05c2c1c6ac55ecbe094ae25ed8e228e298140ccf" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/sabnzbd/actions/runs/37598337724" target="_blank">2026-10-07 09:06:39</a></td></tr>
<tr><td><div id="tag30719" onclick="CopyToClipboard('tag30719');return false;" class="tag-decoration">testing</div><div id="tag20154" onclick="CopyToClipboard('tag20154');return false;" class="tag-decoration">testing-b55ac39</div><div id="tag808" onclick="CopyToClipboard('tag808');return false;" class="tag-decoration">testing-5.2.0Beta2</div></td><td>Pre-releases</td><td><a href="https://github.com/edbfi/sabnzbd/commit/b55ac39b5cf3a8f8384568b54da2d020436f393e" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/sabnzbd/actions/runs/37598340991" target="_blank">2026-10-07 09:06:40</a></td></tr>
</tbody>
  </table>
</div>

The `release` (also `latest`), `testing` and `nightly` images are published for amd64 and arm64 after native validation and review. Testing currently contains the same 5.1.3 release; nightly is a pinned 5.2.0 development snapshot. Updates and publication are manual.

## Starting the container

=== "cli"

    ```shell linenums="1"
    docker run --rm \
        --name sabnzbd \
        -p 8080:8080 \
        -e PUID=1000 \
        -e PGID=1000 \
        -e UMASK=002 \
        -e WEBUI_PORTS="8080/tcp,8080/udp" \
        -e ARGS="" \
        -e TZ="Etc/UTC" \
        -v /<host_folder_config>:/config \
        -v /<host_folder_data>:/data \
        ghcr.io/edbfi/sabnzbd
    ```

=== "compose"

    ```yaml linenums="1"
    services:
      sabnzbd:
        container_name: sabnzbd
        image: ghcr.io/edbfi/sabnzbd
        ports:
          - "8080:8080"
        environment:
          - PUID=1000
          - PGID=1000
          - UMASK=002
          - TZ=Etc/UTC
          - WEBUI_PORTS=8080/tcp,8080/udp
          - ARGS
        volumes:
          - /<host_folder_config>:/config
          - /<host_folder_data>:/data
    ```

--8<-- "includes/wireguard.md"
