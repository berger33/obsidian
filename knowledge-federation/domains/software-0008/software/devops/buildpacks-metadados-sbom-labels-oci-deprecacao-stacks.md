---
id: software.devops.tranche09.000860
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/buildpacks/pack/main/README.md", "https://raw.githubusercontent.com/buildpacks/spec/main/platform.md", "https://github.com/buildpacks/pack"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cloud Native Buildpacks: geração integrada de SBOM, labels OCI (io.buildpacks.*) e transição de Stacks para Target Data

## Em uma frase
Os Cloud Native Buildpacks anexam metadados ricos nas labels OCI (`io.buildpacks.build.metadata`, `io.buildpacks.lifecycle.metadata`, `io.buildpacks.project.metadata`), geram Software Bills of Materials (`SBOM` em Syft, CycloneDX e SPDX) registráveis com `pack sbom download` e substituíram o antigo conceito de `stack` por **Target Data** (`os`, `arch`, distro).

## Por que importa
Equipes de segurança de cadeia de suprimentos precisam extrair a lista exata de todas as dependências de compilação e de runtime (SBOM) de cada imagem OCI sem depender de scanners heurísticos externos que erram versões de binários compilados; além disso, entender a depreciação de `io.buildpacks.stack.*` na especificação Platform API moderna evita usar metadados obsoletos. A especificação `platform.md` documenta tanto os arquivos/labels de metadados quanto a depreciação de `stack`.

## Como funciona
Durante o build, cada buildpack grava arquivos SBOM padronizados (`<layer>.sbom.<ext>.json` em formatos CycloneDX, SPDX ou Syft JSON) descrevendo exatamente os pacotes e versões que instalou. O `exporter` empacota esses SBOMs na imagem (extraíveis via **`pack sbom download <imagem>`**) e preenche três labels JSON padronizadas na configuração OCI: (1) `io.buildpacks.build.metadata` (BOM, buildpacks participantes, processos e launcher); (2) `io.buildpacks.lifecycle.metadata` (digests das camadas de app, run image e buildpacks); e (3) `io.buildpacks.project.metadata` (repositório Git e commit). Na Platform API `0.15`, o antigo conceito de **stack** (`io.buildpacks.stack.id`) foi depreciado em favor de **Target Data** padrão da OCI (`os`, `arch`, `arch_variant` e nome/versão da distribuição Linux).

## Exemplo
```bash
# Baixar e inspecionar os arquivos de Software Bill of Materials (SBOM) embutidos pelos buildpacks na imagem OCI
pack sbom download minha-app:v1.0.0 --output-dir ./sbom-out
ls -la ./sbom-out
```

## Limites e trade-offs
Ao atualizar builders ou criar novos buildpacks seguindo a especificação Platform API `0.12+` / `0.15`, não dependa mais da label depreciada `io.buildpacks.stack.id` para validar compatibilidade entre buildpacks e imagens base; utilize os campos de **Target Data** (`targets` em `buildpack.toml` especificando `os = "linux"`, `arch = "amd64"` e `distributions`).

## Como verificar
Execute `pack sbom download <imagem> --output-dir /tmp/sbom` e confirme a presença dos arquivos SBOM detalhados por camada e por buildpack.

## Conexões
- [[buildpacks-criacao-builders-customizados-builder-toml]] — Veja também: Cloud Native Buildpacks: empacotamento de Builders corporativos customizados (builder.toml e pack builder create).
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.
- [[buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter]] — Referência cruzada direta com buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter.
- [[ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade]] — Referência cruzada direta com ko-geracao-automatica-sbom-multiplataforma-reprodutibilidade.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://github.com/buildpacks/pack) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
