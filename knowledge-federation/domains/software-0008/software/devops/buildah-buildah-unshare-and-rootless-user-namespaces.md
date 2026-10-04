---
id: software.devops.tranche06.000534
tipo: tecnica
dominio: software
subdominio: devops
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/containers/buildah/main/README.md", "https://github.com/containers/buildah/tree/main/docs/containertools", "https://github.com/containers/buildah"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Execução sem privilégios de root e manipulação de namespaces com buildah unshare

## Em uma frase
Na tabela oficial de comandos do README, o subcomando **`buildah-unshare(1)`** (`buildah unshare`) é definido como a ferramenta que **inicia um comando dentro de um user namespace com mapeamentos de ID (UID/GID) modificados** (utilizando os intervalos subordinados configurados em `/etc/subuid` e `/etc/subgid`). Dentro desse namespace de usuário isolado, o processo enxerga a si mesmo como UID `0` (root virtual do namespace) embora continue sendo um usuário comum sem privilégios no kernel do host, o que permite montar sistemas de arquivos de camadas (`buildah mount`), alterar permissões `chown` entre diferentes UIDs internos do contêiner e construir imagens multi-usuário com segurança total.

## Por que importa
Compreender o papel do `buildah unshare` explica como o Buildah consegue construir imagens que possuem arquivos pertencentes a múltiplos usuários internos (como `root`, `nginx`, `postgres`) mesmo quando o comando `buildah` é invocado por um usuário comum de CI sem `sudo`.

## Como funciona
Utilize `buildah unshare <script.sh>` sempre que seu script de construção de imagens sem root precisar executar `buildah mount` ou manipular diretamente permissões e arquivos de múltiplos UIDs no rootfs montado.

## Exemplo
Um script de empacotamento rootless precisa montar o rootfs de um contêiner de trabalho, copiar arquivos de configuração e ajustar o dono para o UID `1001`; ao ser executado via `buildah unshare ./build-image.sh`, todas as montagens e chamadas `chown` funcionam perfeitamente sem privilégios no host.

## Limites e trade-offs
Verifique com `buildah info` se o usuário executor possui faixas de UIDs e GIDs subordinados suficientes (tipicamente 65536 IDs em `/etc/subuid` e `/etc/subgid`), pois um mapeamento ausente impedirá que pacotes Linux que criam usuários de sistema sejam instalados na imagem.

## Como verificar
Execute `buildah unshare id` e `buildah unshare cat /proc/self/uid_map` como usuário não-root para verificar o mapeamento de namespace de usuário ativo.

## Conexões
- [[buildah-from-scratch-minimal-images-and-host-package-managers]] — Veja também: Criação de imagens mínimas do zero (buildah from scratch) e montagem direta do rootfs com buildah mount.
- [[buildah-buildah-versus-podman-specialization-and-working-containers]] — Veja também: Diferença arquitetural entre Buildah e Podman e o conceito de Working Containers.

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
