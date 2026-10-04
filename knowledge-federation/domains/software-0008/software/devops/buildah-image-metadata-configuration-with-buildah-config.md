---
id: software.devops.tranche06.000537
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

# Configuração de metadados OCI (entrypoint, cmd, env, port, user, labels e annotations) com buildah config

## Em uma frase
O subcomando **`buildah-config(1)`** (`buildah config`), demonstrado no exemplo oficial `examples/lighttpd.sh` do README, permite atualizar qualquer configuração de metadados da imagem OCI associada a um working container sem precisar criar camadas adicionais de sistema de arquivos: inclui flags como **`--annotation`**, **`--cmd`**, **`--entrypoint`**, **`--env`**, **`--port`**, **`--user`**, **`--workingdir`**, **`--label`**, **`--author`** e **`--created-by`**.

## Por que importa
Quando se constrói uma imagem do zero (`from scratch`) ou via script sem `Dockerfile`, os metadados de execução do contêiner (qual binário executar por padrão, qual porta expor, sob qual UID não-root rodar e quais anotações OCI registrar) são definidos inteiramente através de chamadas `buildah config` antes do `buildah commit`.

## Como funciona
Sempre defina um usuário não-root explícito (`buildah config --user 1000:1000 "$ctr"`), o comando de inicialização (`--entrypoint` / `--cmd`) e anotações de rastreabilidade (`--annotation "org.opencontainers.image.revision=$GIT_SHA"`) com `buildah config` antes de consolidar a imagem.

## Exemplo
No script de release, antes de executar `buildah commit`, o pipeline roda `buildah config --user 65532:65532 --port 8080 --entrypoint '["/app/server"]' "$ctr"` e verifica a configuração gerada com `buildah inspect "$ctr"`.

## Limites e trade-offs
Lembre-se de que alterações feitas com `buildah config` modificam o estado do working container em aberto; você deve executar **`buildah commit`** em seguida para gravar essas configurações em uma nova imagem.

## Como verificar
Execute `buildah inspect --type container "$ctr"` após rodar `buildah config` para confirmar os campos `Config.Env`, `Config.Cmd`, `Config.User` e `Annotations` antes do commit.

## Conexões
- [[buildah-copy-and-add-content-from-files-urls-and-directories]] — Veja também: Adição de arquivos, diretórios e URLs ao contêiner de trabalho com buildah copy e buildah add.
- [[buildah-pull-push-tag-and-local-storage-lifecycle]] — Veja também: Gerenciamento de ciclo de vida de imagens e registros com buildah pull, push, tag, rm e rmi.

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
