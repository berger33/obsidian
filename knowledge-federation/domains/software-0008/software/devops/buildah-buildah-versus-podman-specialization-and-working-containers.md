---
id: software.devops.tranche06.000535
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

# Diferença arquitetural entre Buildah e Podman e o conceito de Working Containers

## Em uma frase
A seção *Buildah and Podman relationship* do README oficial esclarece em detalhes a complementaridade e a diferença fundamental entre os dois projetos da organização `containers`: enquanto o **Buildah se especializa em construir imagens OCI** e o **Podman se especializa em manter, executar e gerenciar contêineres tradicionais de longa duração** (usando a API Go do Buildah por baixo dos panos quando o usuário roda `podman build`), os dois projetos possuem conceitos distintos do que é um "contêiner". Os **contêineres do Buildah (working containers)** são efêmeros e criados exclusivamente para permitir que conteúdo e camadas sejam adicionados de volta a uma imagem (`buildah run` emula a instrução `RUN` de um Dockerfile, enquanto `podman run` emula o `docker run`).

## Por que importa
O README destaca uma consequência operacional direta dessa diferença e de suas estruturas internas de armazenamento: **você não enxerga contêineres em execução do Podman de dentro de `buildah containers`, nem enxerga working containers do Buildah de dentro de `podman ps`** (embora ambos compartilhem o mesmo armazenamento local de **imagens** consolidado em `containers/storage`, visível tanto em `buildah images` quanto em `podman images`).

## Como funciona
Use `buildah` (`from`, `run`, `copy`, `config`, `commit`, `build`) para pipelines e scripts de construção de imagens OCI e use `podman` (`run`, `ps`, `pod`, `kube play`) para executar e gerenciar o ciclo de vida dos contêineres resultantes.

## Exemplo
Um desenvolvedor constrói e faz commit de uma nova imagem com `buildah commit "$ctr" minha-app:dev`; embora o working container `$ctr` só apareça em `buildah containers`, a imagem final `minha-app:dev` fica imediatamente disponível em `podman images` para ser executada com `podman run` sem precisar de push/pull.

## Limites e trade-offs
Não tente usar `buildah run` para manter um serviço de aplicação rodando em segundo plano como um contêiner de produção; `buildah run` serve apenas para executar etapas de build durante a construção da camada da imagem.

## Como verificar
Liste os contêineres de trabalho ativos com `buildah containers` e compare com `buildah images` e `podman images` para comprovar o compartilhamento do store de imagens.

## Conexões
- [[buildah-buildah-unshare-and-rootless-user-namespaces]] — Veja também: Execução sem privilégios de root e manipulação de namespaces com buildah unshare.
- [[buildah-copy-and-add-content-from-files-urls-and-directories]] — Veja também: Adição de arquivos, diretórios e URLs ao contêiner de trabalho com buildah copy e buildah add.

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
