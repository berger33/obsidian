---
id: software.devops.tranche04.000357
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/moby/buildkit/master/README.md", "https://pkg.go.dev/github.com/moby/buildkit/client/llb", "https://github.com/moby/buildkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Exportação e importação de cache de build (inline, registry, local, GitHub Actions, S3 e Azure Blob)

## Em uma frase
Para compartilhar cache de instruções LLB entre runners efêmeros de CI, o BuildKit oferece `--export-cache` e `--import-cache` com múltiplos backends documentados no README: **Inline** (`--export-cache type=inline`, que embute os metadados de cache na própria imagem publicada e é importado com `--import-cache type=registry,ref=...`), **Registry** (publica imagem e manifesto de cache separadamente no registro OCI), **Local directory** (`--export-cache type=local`), além dos backends experimentais **GitHub Actions cache**, **Amazon S3** e **Azure Blob Storage**.

## Por que importa
Em runners efêmeros de CI/CD que começam com disco vazio a cada execução, não exportar e importar o cache do BuildKit força a recompilação integral de todas as camadas a cada pull request.

## Como funciona
Para fluxos simples de estágio único, utilize `--export-cache type=inline` junto com `--import-cache type=registry,ref=<imagem>`; para builds multi-stage complexos onde camadas intermediárias não vão para a imagem final, exporte o cache completo para um ref dedicado no registro (`type=registry,mode=max`), S3 ou cache do GitHub Actions.

## Exemplo
No pipeline de build, o comando `buildctl build ... --output type=image,name=ghcr.io/org/app,push=true --export-cache type=inline --import-cache type=registry,ref=ghcr.io/org/app` reutiliza instantaneamente as camadas inalteradas da última build publicada.

## Limites e trade-offs
Note que `--export-cache type=inline` exporta apenas o cache das camadas que fazem parte da imagem final gerada; estágios intermediários de compilação (`builder`) exigem exportação dedicada (`type=registry` ou `type=local`/`gha`/`s3`) para serem cacheados entre runners.

## Como verificar
Execute dois builds consecutivos em ambientes limpos importando o cache com `--import-cache` e confirme nos logs do segundo build que as etapas aparecem como `CACHED`.

## Conexões
- [[buildkit-local-directory-and-tarball-outputs]] — Veja também: Exportação de artefatos para diretório local (type=local) e tarballs OCI ou Docker no BuildKit.
- [[buildkit-automatic-garbage-collection-and-storage-management]] — Veja também: Coleta de lixo automática (automatic garbage collection) do cache interno no BuildKit.

## Fontes
- [Moby BuildKit GitHub — README.md (Architecture, LLB, Frontends, Outputs & Caching)](https://raw.githubusercontent.com/moby/buildkit/master/README.md) — README oficial do Moby BuildKit detalhando arquitetura buildkitd e buildctl, formato intermediário binário LLB em Protobuf, gateway.v0 e dockerfile.v0, backends OCI (runc/crun) e containerd, opções de output (image, local, compression gzip/estargz/zstd, SOURCE_DATE_EPOCH) e export/import de cache.; consultado em 2026-10-03.
- [Go Package Documentation — github.com/moby/buildkit/client/llb](https://pkg.go.dev/github.com/moby/buildkit/client/llb) — Documentação oficial da biblioteca Go client/llb do BuildKit para construção programática de grafos de dependência LLB.; consultado em 2026-10-03.
- [Moby BuildKit — Official GitHub Repository](https://github.com/moby/buildkit) — Repositório oficial Apache-2.0 do Moby BuildKit.; consultado em 2026-10-03.
