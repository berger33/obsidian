---
id: software.devops.tranche09.000853
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

# Cloud Native Buildpacks: arquitetura de Builder, Build Image, Run Image, Launch Layers e processo Launcher

## Em uma frase
Na terminologia oficial da especificação CNB (`platform.md`), um **Builder** empacota os buildpacks, o lifecycle e a **Build Image**, enquanto a **App Image** final combina a **Run Image** com as **Launch Layers**, **App Layers** e o executável **Launcher**.

## Por que importa
Separar estritamente a imagem onde o código é compilado (**Build Image**, que contém compiladores, headers e ferramentas de build) da imagem onde a aplicação roda em produção (**Run Image**, enxuta e endurecida) garante o benefício de multi-stage builds automaticamente, enquanto o **Launcher** gerencia variáveis de ambiente e múltiplos tipos de processos em runtime.

## Como funciona
Conforme a seção `Terminology` de `platform.md`: (1) **Build Image**: imagem OCI que serve como base para o ambiente containerizado de compilação (`build environment`); (2) **Run Image**: imagem OCI que serve como base limpa para a imagem final da aplicação; (3) **Builder**: imagem OCI que agrupa um conjunto ordenado de buildpacks (`order.toml`), o binário do lifecycle, a Build Image e a referência para a Run Image; (4) **Launch Layer** e **App Layer**: camadas na imagem final criadas a partir de `<layers>/<layer>` (ex.: JRE, `node_modules`) e do diretório `<app>`; e (5) **Launcher**: executável do lifecycle empacotado na `launcher layer` da **App Image** como `ENTRYPOINT`, responsável por configurar o ambiente de inicialização (`Launch Environment`) e iniciar o processo padrão (`web`, `worker`, etc.) em tempo de execução.

## Exemplo
```bash
# Inspecionar a composição interna de um Builder (buildpacks incluídos, ordem de detecção, lifecycle e run images)
pack builder inspect paketobuildpacks/builder-jammy-base
```

## Limites e trade-offs
Como o `ENTRYPOINT` da imagem gerada por Cloud Native Buildpacks é o binário **`/cnb/lifecycle/launcher`** (e não `/bin/sh`), ao sobrescrever o comando de inicialização no Docker ou no Kubernetes (`command` / `args`), o `launcher` interpreta os argumentos de acordo com o perfil de processo configurado pelos buildpacks; para descobrir quais tipos de processos (`process types`) foram exportados pela imagem, utilize `pack inspect <imagem>`.

## Como verificar
Execute `pack builder suggest` para listar os builders oficiais recomendados (Paketo, Google, Heroku) e `pack builder inspect <builder>` para auditar suas versões de Lifecycle e Run Image.

## Conexões
- [[buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter]] — Veja também: Cloud Native Buildpacks: as fases do Lifecycle (analyzer, detector, restorer, extender, builder e exporter).
- [[buildpacks-operacao-rebase-atualizacao-rapida-run-image]] — Veja também: Cloud Native Buildpacks: atualização instantânea da imagem base do SO sem recompilar a aplicação (pack rebase).
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://github.com/buildpacks/pack) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
