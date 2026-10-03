---
id: software.devops.tranche06.000538
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

# Gerenciamento de ciclo de vida de imagens e registros com buildah pull, push, tag, rm e rmi

## Em uma frase
A tabela de comandos do README oficial documenta o conjunto completo de operações de armazenamento e transporte integradas ao próprio Buildah: **`buildah-pull(1)`** (baixar uma imagem de um registro ou transporte especificado), **`buildah-push(1)`** (enviar uma imagem do armazenamento local para um registro remoto, arquivo tar, diretório OCI ou daemon Docker), **`buildah-tag(1)`** (adicionar nomes/tags extras a uma imagem local), **`buildah-images(1)`** (listar imagens locais), **`buildah-containers(1)`** (listar working containers), **`buildah-rename(1)`**, **`buildah-rm(1)`** (remover working containers) e **`buildah-rmi(1)`** (remover imagens do armazenamento local).

## Por que importa
Como o Buildah utiliza a biblioteca `containers/image` e `containers/storage` (compartilhada com Podman, Skopeo e CRI-O), o comando `buildah push` não se limita a enviar para registros remotos `docker://`: ele pode exportar diretamente para diretórios `oci:`, arquivos `docker-archive:` ou armazenamento local sem precisar de outro utilitário.

## Como funciona
Em pipelines de CI, construa a imagem, aplique as tags necessárias com `buildah tag`, envie para o registro corporativo com `buildah push` (capturando o digest com `--digestfile`) e limpe os working containers com `buildah rm --all`.

## Exemplo
Após concluir `buildah build -t registry.corp/app:1.4.0 .`, o job de CI executa `buildah push --digestfile /tmp/digest.txt registry.corp/app:1.4.0` e alimenta o digest SHA-256 gerado diretamente na etapa de assinatura com `cosign sign`.

## Limites e trade-offs
Em runners de CI persistentes (stateful), execute periodicamente `buildah rm --all` e `buildah rmi --prune` para limpar working containers esquecidos e imagens intermediárias órfãs do armazenamento `/var/lib/containers` ou `~/.local/share/containers`.

## Como verificar
Teste o ciclo local executando `buildah pull alpine`, `buildah tag`, `buildah push alpine oci:/tmp/alpine-oci:latest` e `buildah rmi` verificando o funcionamento de ponta a ponta.

## Conexões
- [[buildah-image-metadata-configuration-with-buildah-config]] — Veja também: Configuração de metadados OCI (entrypoint, cmd, env, port, user, labels e annotations) com buildah config.
- [[buildah-containerfiles-and-dockerfiles-with-buildah-build]] — Veja também: Construção declarativa a partir de Containerfiles e Dockerfiles com buildah build (buildah bud).

## Fontes
- [Buildah GitHub — README.md (Daemonless OCI Image Building, Working Containers, Podman Relationship & CLI Commands)](https://raw.githubusercontent.com/containers/buildah/main/README.md) — README oficial do Buildah detalhando criação de working containers do zero (from scratch) ou de imagens base, construção com ou sem Dockerfile nos formatos OCI e Docker, montagem direta do rootfs (buildah mount/umount), modelo fork-exec sem daemon e sem exigir root, relação arquitetural com Podman, script de exemplo lighttpd.sh e tabela completa dos 21 subcomandos CLI.; consultado em 2026-10-03.
- [Buildah GitHub — Container Tools Guide (Buildah, Podman & Skopeo Integration)](https://github.com/containers/buildah/tree/main/docs/containertools) — Guia oficial de integração entre Buildah, Podman e Skopeo no repositório containers/buildah.; consultado em 2026-10-03.
- [Buildah — Official GitHub Repository](https://github.com/containers/buildah) — Repositório oficial Apache-2.0 do Buildah na organização containers.; consultado em 2026-10-03.
