---
id: software.devops.tranche09.000857
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

# Cloud Native Buildpacks: extensão de imagens de build e run com Image Extensions e a fase extender

## Em uma frase
Conforme a especificação Platform Interface (`platform.md`), as **Image Extensions** participam da fase `detector` e são executadas na fase opcional **`extender`** antes dos buildpacks para instalar pacotes de sistema operacional adicionais na Build Image ou na Run Image usando Dockerfiles gerados dinamicamente.

## Por que importa
Historicamente, uma limitação clássica dos Buildpacks era quando uma aplicação em Python, Ruby ou Node.js precisava de uma biblioteca C específica do sistema operacional (ex.: `libpq-dev`, `ffmpeg`, `imagemagick` ou `curl`) que não vinha pré-instalada na Build Image ou na Run Image padrão; antes das Image Extensions, a equipe era obrigada a criar e manter uma imagem de Stack/Builder customizada inteira. A especificação `platform.md` resolve isso com `Image Extensions` e a fase `extender`.

## Como funciona
Uma **Image Extension** segue a especificação `image_extension.md` e reside no diretório de extensões do builder. Durante a fase **`detector`**, as extensões rodam junto aos buildpacks para verificar se são necessárias e geram `build.Dockerfile` e/ou `run.Dockerfile`. Caso alguma extensão seja ativada no plano, a plataforma executa a fase **`extender`** (utilizando kaniko/buildkit embutido no lifecycle) para aplicar o `build.Dockerfile` sobre a Build Image (antes de rodar a fase `builder` dos buildpacks) e/ou aplicar o `run.Dockerfile` para trocar ou estender a Run Image final.

## Exemplo
```bash
# Inspecionar um builder com pack builder inspect para verificar se ele inclui image extensions e suporte à Platform API moderna
pack builder inspect paketobuildpacks/builder-jammy-base --output json | jq '.remote_info.buildpacks'
```

## Limites e trade-offs
Quando uma **Image Extension** modifica as camadas da **Run Image** adicionando pacotes via `run.Dockerfile` durante a fase `extender`, a imagem final passa a depender daquelas camadas estendidas; dependendo de como a extensão foi aplicada, a operação rápida `pack rebase` pode exigir restrições ou reconstrução se a extensão alterou a estrutura base da Run Image.

## Como verificar
Consulte a seção `Image Extensions` e `extender (optional)` na especificação `buildpacks/spec/platform.md` e verifique a versão da Platform API suportada pelo seu binário `pack version`.

## Conexões
- [[buildpacks-configuracao-project-toml-env-vars-build]] — Veja também: Cloud Native Buildpacks: configuração declarativa do build com project.toml, variáveis BP_* e BPE_*.
- [[buildpacks-autoria-empacotamento-buildpack-toml-pack-package]] — Veja também: Cloud Native Buildpacks: criação e empacotamento de Buildpacks (buildpack.toml, bin/detect, bin/build e pack buildpack package).
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.
- [[buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter]] — Referência cruzada direta com buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://github.com/buildpacks/pack) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
