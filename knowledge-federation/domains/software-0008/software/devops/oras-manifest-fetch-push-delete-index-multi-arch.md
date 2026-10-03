---
id: software.devops.tranche13.001256
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://oras.land/docs/category/oras-commands/", "https://raw.githubusercontent.com/oras-project/oras/main/README.md", "https://github.com/oras-project/oras"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ORAS: Manipulação Direta de Manifestos e Índices OCI (oras manifest fetch, push, index create e update)

## Em uma frase
A família de comandos `oras manifest` (`fetch`, `fetch-config`, `push`, `delete`, `index create` e `index update`) oferece controle de baixo nível para inspecionar o JSON bruto de manifestos, extrair blobs de configuração e compor ou atualizar índices multi-arquitetura (`OCI Image Index`) em um mesmo repositório.

## Por que importa
Quando builds para `linux/amd64` e `linux/arm64` rodam em runners separados na CI, é preciso combinar os dois manifestos de plataforma em um único `Image Index` sem rebaixar os blobs das camadas.

## Como funciona
Após cada runner fazer push de sua imagem por plataforma, o step de consolidação executa `oras manifest index create <repo:tag> <digest-amd64> <digest-arm64>` para criar e publicar o índice unificado; já `oras manifest fetch --pretty <repo:tag>` e `oras manifest fetch-config <repo:tag>` permitem auditar os descritores e a configuração sem baixar as camadas pesadas.

## Exemplo
```bash
oras manifest fetch --pretty ghcr.io/oras-project/oras:v1.2.0
oras manifest index create ghcr.io/org/app:v1.0.0 \
  ghcr.io/org/app@sha256:1111111111111111111111111111111111111111111111111111111111111111 \
  ghcr.io/org/app@sha256:2222222222222222222222222222222222222222222222222222222222222222
```

## Limites e trade-offs
Tentar incluir em `oras manifest index create` manifestos que residem em repositórios diferentes falha porque a especificação OCI exige que todos os manifestos referenciados pelo índice pertençam ao mesmo repositório.

## Como verificar
Empurre todas as variantes de arquitetura para o mesmo repositório antes de agregar seus digests com `oras manifest index create` ou `oras manifest index update`.

## Conexões
- [[oras-backup-restore-arquivamento-portavel-air-gapped]] — Veja também: ORAS: Backup e Restauração de Artefatos e Grafos OCI para Ambientes Air-Gapped (oras backup e oras restore).
- [[oras-blob-fetch-push-delete-operacoes-camada-digest]] — Veja também: ORAS: Operações Diretas em Blobs Endereçáveis por Conteúdo (oras blob push, fetch e delete).

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://oras.land/docs/category/oras-commands/) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
