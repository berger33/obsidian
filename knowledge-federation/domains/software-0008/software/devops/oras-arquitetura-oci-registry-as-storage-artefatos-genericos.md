---
id: software.devops.tranche13.001251
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
fontes: ["https://raw.githubusercontent.com/oras-project/oras/main/README.md", "https://oras.land/docs/category/oras-commands/", "https://github.com/oras-project/oras"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# ORAS: Arquitetura OCI Registry As Storage e Distribuição de Artefatos Genéricos

## Em uma frase
O **ORAS (OCI Registry As Storage)** é um projeto CNCF Sandbox (com CLI e bibliotecas cliente em Go, Python e .NET) que permite armazenar, publicar, baixar e gerenciar artefatos arbitrários — como SBOMs, assinaturas criptográficas, charts Helm, módulos Terraform/OPA, binários WASM e configurações — em qualquer registro compatível com a especificação **OCI Distribution**.

## Por que importa
Manter servidores de armazenamento diferentes para imagens de container, pacotes de política OPA, bundles WASM, SBOMs SPDX/CycloneDX e binários de release multiplica custos de infraestrutura, autenticação e governança de acesso.

## Como funciona
O ORAS empacota arquivos em manifestos OCI padrão definindo um `--artifact-type` explícito (por exemplo, `application/vnd.example.config.v1+json` ou `application/spdx+json`) e media types customizados por arquivo (`arquivo:media-type`). As imagens oficiais da CLI são publicadas em `ghcr.io/oras-project/oras` com tags SemVer imutáveis (`:vX.Y.Z`) e tags rolantes protegidas contra regressão em backports.

## Exemplo
```bash
oras version
oras login ghcr.io -u "$GITHUB_USER" --password-stdin
oras push ghcr.io/org/policies:v1.0.0 \
  --artifact-type application/vnd.cncf.openpolicyagent.config.v1+json \
  ./bundle.tar.gz:application/gzip
```

## Limites e trade-offs
Empurrar arquivos arbitrários com `oras push` sem definir `--artifact-type` usa um tipo genérico padrão que dificulta a filtragem e descoberta automatizada do tipo de artefato por consumidores downstream.

## Como verificar
Defina sempre `--artifact-type` com um media type IANA/vendor descritivo ao publicar artefatos não-container com `oras push`.

## Conexões
- [[oras-push-pull-media-types-annotations-oci-image-layout]] — Veja também: ORAS: Operações de Push e Pull de Arquivos, Media Types, Anotações e OCI Image Layout Local.

## Fontes
- [ORAS CLI Official Documentation — Commands Reference (push, pull, attach, discover, cp, backup, restore, manifest, blob & repo)](https://raw.githubusercontent.com/oras-project/oras/main/README.md) — Documentação oficial de comandos da CLI do ORAS detalhando manipulação de artefatos, OCI Image Layout (--oci-layout), árvore de referrers OCI 1.1 e cópia recursiva entre registros; consultado em 2026-10-03.
- [ORAS GitHub — README.md (OCI Registry As Storage Overview, Multi-Arch Container Images & Immutable Release Tag Policy)](https://oras.land/docs/category/oras-commands/) — README oficial do oras-project/oras documentando a governança de tags de release (:vX.Y.Z, :vX.Y, :vX, :latest) e instalação; consultado em 2026-10-03.
- [ORAS Project — Official GitHub Repository](https://github.com/oras-project/oras) — Repositório oficial CNCF Sandbox do ORAS; consultado em 2026-10-03.
