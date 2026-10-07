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
<tr><td><div id="tag23709" onclick="CopyToClipboard('tag23709');return false;" class="tag-decoration">nightly</div><div id="tag18221" onclick="CopyToClipboard('tag18221');return false;" class="tag-decoration">nightly-8061d96</div><div id="tag14933" onclick="CopyToClipboard('tag14933');return false;" class="tag-decoration">nightly-cbda9451bb3c4143fa4d9d5c1c2b1ab8e5eb3d4d</div></td><td>Every commit to develop</td><td><a href="https://github.com/edbfi/sabnzbd/commit/8061d96390fb3ccd9face275cc2e815fe5f18b42" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/sabnzbd/actions/runs/37538193156" target="_blank">2026-10-06 22:04:10</a></td></tr>
<tr><td><div class="tag-decoration-latest">latest</div><div id="tag27498" onclick="CopyToClipboard('tag27498');return false;" class="tag-decoration">release</div><div id="tag27454" onclick="CopyToClipboard('tag27454');return false;" class="tag-decoration">release-2af0f2a</div><div id="tag23090" onclick="CopyToClipboard('tag23090');return false;" class="tag-decoration">release-5.1.3</div><div id="tag5233" onclick="CopyToClipboard('tag5233');return false;" class="tag-decoration">release-v5</div><div id="tag30755" onclick="CopyToClipboard('tag30755');return false;" class="tag-decoration">release-v5.1</div><div id="tag30815" onclick="CopyToClipboard('tag30815');return false;" class="tag-decoration">release-v5.1.3</div></td><td>Releases</td><td><a href="https://github.com/edbfi/sabnzbd/commit/2af0f2a05c7ecbe67fe39d25178e077a77c490b4" target="_blank">ci: add monthly immortality workflow (#37)--GitHub disables scheduled workflows in a public repository after 60 days without activity. This workflow re-enables the repository's workflows once a month with the IMMORTALITY_TOKEN personal token, which resets that counter. Owner-approved addition to the Hotio callers (2026-10-07).--Signed-off-by: edbfi <326875205+edbfi@users.noreply.github.com></a></td><td><a href="https://github.com/edbfi/sabnzbd/actions/runs/37594116659" target="_blank">2026-10-07 08:29:35</a></td></tr>
<tr><td><div id="tag11550" onclick="CopyToClipboard('tag11550');return false;" class="tag-decoration">testing</div><div id="tag17757" onclick="CopyToClipboard('tag17757');return false;" class="tag-decoration">testing-b55ac39</div><div id="tag2839" onclick="CopyToClipboard('tag2839');return false;" class="tag-decoration">testing-5.2.0Beta2</div></td><td>Pre-releases</td><td><a href="https://github.com/edbfi/sabnzbd/commit/b55ac39b5cf3a8f8384568b54da2d020436f393e" target="_blank">Modified: meta.json</a></td><td><a href="https://github.com/edbfi/sabnzbd/actions/runs/37598340991" target="_blank">2026-10-07 09:06:40</a></td></tr>
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
