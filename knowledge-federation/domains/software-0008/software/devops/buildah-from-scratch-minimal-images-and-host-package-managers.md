---
id: software.devops.tranche06.000533
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

# Criação de imagens mínimas do zero (buildah from scratch) e montagem direta do rootfs com buildah mount

## Em uma frase
O README oficial destaca que o Buildah permite criar um contêiner de trabalho **totalmente do zero (`buildah from scratch`)** e **montar o sistema de arquivos raiz (rootfs) desse contêiner diretamente no host (`buildah mount` / `buildah umount`)** para manipulação externa. Ao montar o rootfs vazio do contêiner em um diretório local (ex.: `mnt=$(buildah mount $ctr)`), o engenheiro pode usar o gerenciador de pacotes ou compilador da própria máquina host (como `dnf --installroot=$mnt` ou `apt`/`apk`) para instalar apenas o binário da aplicação e suas bibliotecas essenciais dentro de `$mnt`, sem jamais incluir o próprio gerenciador de pacotes (`dnf`/`apt`), o shell (`/bin/sh`) ou utilitários de sistema na imagem final.

## Por que importa
Em um `Dockerfile` comum, para rodar `RUN dnf install -y pacote`, a imagem base já precisa conter o `dnf`, o Python e um shell bash dentro dela. Com `buildah from scratch` + `buildah mount`, usa-se o `dnf` de fora (do host de build) para popular o rootfs do contêiner, gerando imagens mínimas e endurecidas (distroless/micro) com superfície de ataque mínima contra CVEs.

## Como funciona
Em modo rootless, entre primeiro no user namespace do Buildah com **`buildah unshare`**, monte o rootfs do contêiner com `mnt=$(buildah mount "$ctr")`, popule os arquivos ou pacotes com `--installroot="$mnt"`, desmonte com `buildah umount "$ctr"` e gere a imagem com `buildah commit`.

## Exemplo
Para criar uma imagem de produção enxuta sem shell nem gerenciador de pacotes, o pipeline executa `ctr=$(buildah from scratch)`, monta o rootfs com `mnt=$(buildah mount "$ctr")`, instala apenas o binário estático e certificados CA em `$mnt`, desmonta com `buildah umount "$ctr"` e faz `buildah commit`.

## Limites e trade-offs
Observe que, ao executar `buildah mount` como um usuário comum sem privilégios (rootless), é obrigatório estar dentro de uma sessão iniciada por **`buildah unshare`** (que cria o user namespace com mapeamento de IDs modificado), caso contrário o kernel Linux negará a operação de montagem.

## Como verificar
Execute `buildah unshare` para testar `ctr=$(buildah from scratch)`, `mnt=$(buildah mount "$ctr")`, `buildah umount "$ctr"` e `buildah rm "$ctr"` validando o ciclo completo sem root.

## Conexões
- [[buildah-building-images-without-dockerfiles-from-run-config-commit]] — Veja também: Construção programática de imagens sem Dockerfile com buildah from, run, config e commit.
- [[buildah-buildah-unshare-and-rootless-user-namespaces]] — Veja também: Execução sem privilégios de root e manipulação de namespaces com buildah unshare.

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
