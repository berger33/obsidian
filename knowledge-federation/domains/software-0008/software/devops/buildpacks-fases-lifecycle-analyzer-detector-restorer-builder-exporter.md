---
id: software.devops.tranche09.000852
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

# Cloud Native Buildpacks: as fases do Lifecycle (analyzer, detector, restorer, extender, builder e exporter)

## Em uma frase
Conforme a especificação Platform Interface (`platform.md`, Platform API `0.15`), a operação de build dos Cloud Native Buildpacks é executada pelo **lifecycle** em fases ordenadas: `detector`, `analyzer`, `restorer`, `extender` (opcional), `builder` e `exporter` (ou consolidada no binário `creator`).

## Por que importa
Diferentemente de um `Dockerfile` que executa scripts imperativos cegos linha a linha, o lifecycle dos Cloud Native Buildpacks separa a inspeção de metadados de registries, a detecção de dependências, a restauração de cache e a exportação de camadas OCI, permitindo reutilizar camadas em cache mesmo sem baixá-las quando já existem no registry remoto. A especificação oficial `buildpacks/spec/platform.md` define formalmente cada fase.

## Como funciona
Durante uma operação `Build`, a plataforma executa os binários do lifecycle (ou o binário único **`creator`** quando confiável): (1) **`detector`**: executa a fase `bin/detect` dos buildpacks contra o código-fonte para definir o grupo ordenado de buildpacks (`group.toml`) e o plano de build (`plan.toml`); (2) **`analyzer`**: consulta a imagem anterior e o cache para validar metadados (`analyzed.toml`); (3) **`restorer`**: restaura camadas de cache para `<layers>`; (4) **`extender` (opcional)**: aplica Image Extensions (ex.: `Dockerfile`s gerados por extensões) para estender a imagem de build ou de run; (5) **`builder`**: executa `bin/build` de cada buildpack aprovado no grupo; e (6) **`exporter`**: monta a **app image** final sobre a **run image**, grava `report.toml` e adiciona as labels JSON `io.buildpacks.*`.

## Exemplo
```bash
# Executar pack build com logs detalhados (--verbose) para acompanhar a saída de cada fase do lifecycle (detector -> analyzer -> restorer -> builder -> exporter)
pack build minha-app:v1.0.0 --builder paketobuildpacks/builder-jammy-base --verbose
```

## Limites e trade-offs
Quando a plataforma executa o binário consolidado **`creator`** (em vez de invocar containers separados para `detector`, `analyzer`, `restorer`, `builder` e `exporter`), o build é mais rápido por evitar o overhead de iniciar 5 containers sequenciais; contudo, quando há **Image Extensions** (`extender`) ou em plataformas multi-tenant não confiáveis onde as credenciais do registry não devem estar acessíveis durante a execução de `detector`/`builder`, a plataforma deve executar as fases separadamente em containers distintos.

## Como verificar
Inspecione as labels da imagem gerada com `docker inspect minha-app:v1.0.0 --format '{{index .Config.Labels "io.buildpacks.lifecycle.metadata"}}' | jq .` para verificar os metadados gravados pelo `exporter`.

## Conexões
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Veja também: Cloud Native Buildpacks (pack): transformação de código-fonte em imagens OCI sem Dockerfile.
- [[buildpacks-conceitos-builder-build-image-run-image-launcher]] — Veja também: Cloud Native Buildpacks: arquitetura de Builder, Build Image, Run Image, Launch Layers e processo Launcher.
- [[buildpacks-operacao-rebase-atualizacao-rapida-run-image]] — Referência cruzada direta com buildpacks-operacao-rebase-atualizacao-rapida-run-image.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://github.com/buildpacks/pack) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
