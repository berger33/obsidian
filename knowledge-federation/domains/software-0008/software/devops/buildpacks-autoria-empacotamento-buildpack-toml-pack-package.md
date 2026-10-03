---
id: software.devops.tranche09.000858
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

# Cloud Native Buildpacks: criação e empacotamento de Buildpacks (buildpack.toml, bin/detect, bin/build e pack buildpack package)

## Em uma frase
Para autores de buildpacks e operadores de plataforma, um buildpack consiste em um arquivo de metadados `buildpack.toml` e dois executáveis (`bin/detect` e `bin/build`), podendo ser inicializado com `pack buildpack new` e empacotado como imagem OCI com `pack buildpack package`.

## Por que importa
Organizações com dezenas de equipes frequentemente desejam padronizar a injeção de certificados internos, agentes de observabilidade, configurações de segurança ou frameworks internos em todas as aplicações sem pedir para cada desenvolvedor editar seu código. Conforme destaca o README oficial do `pack`, a CLI atende diretamente a **Buildpack Authors** e **Operators** para desenvolver e distribuir buildpacks.

## Como funciona
Um buildpack implementa a `Buildpack Interface Specification` (`buildpack.md`) por meio de três elementos: (1) **`buildpack.toml`**: declara o ID, versão, API suportada e alvos compatíveis; (2) **`bin/detect`**: executável (em qualquer linguagem: Go, Rust, Bash) que inspeciona o diretório da aplicação e retorna código `0` se o buildpack deve ser aplicado (gravando o que ele fornece `provides` e o que exige `requires` no Build Plan); e (3) **`bin/build`**: executável que recebe o diretório `<layers>`, cria subdiretórios de camadas (`<layers>/<nome>`), grava `<layers>/<nome>.toml` (`launch`/`build`/`cache`) e define comandos de inicialização em `launch.toml`. Com **`pack buildpack package <registry/meu-bp:v1>`**, o buildpack é empacotado e distribuído como um artefato OCI padrão.

## Exemplo
```bash
# Criar o esqueleto de um novo buildpack customizado e empacotá-lo como imagem OCI usando a CLI pack
pack buildpack new empresa/certificados-corporativos \
  --api 0.10 \
  --path ./bp-certificados \
  --version 1.0.0

pack buildpack package registry.interno.com/buildpacks/certificados:1.0.0 --path ./bp-certificados
```

## Limites e trade-offs
Para manter imagens finais enxutas e rápidas de inicializar, autores de buildpacks em produção (como os Paketo Buildpacks) costumam compilar `bin/detect` e `bin/build` como binários estáticos em Go (usando bibliotecas como `libcnb`) em vez de scripts Bash longos que dependam de ferramentas externas como `jq`, `curl` ou `awk` na Build Image.

## Como verificar
Após criar o buildpack em `./bp-certificados`, teste-o localmente em uma aplicação executando `pack build app-teste --builder paketobuildpacks/builder-jammy-base --buildpack ./bp-certificados`.

## Conexões
- [[buildpacks-image-extensions-extender-dockerfile-dinamico]] — Veja também: Cloud Native Buildpacks: extensão de imagens de build e run com Image Extensions e a fase extender.
- [[buildpacks-criacao-builders-customizados-builder-toml]] — Veja também: Cloud Native Buildpacks: empacotamento de Builders corporativos customizados (builder.toml e pack builder create).
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.
- [[buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter]] — Referência cruzada direta com buildpacks-fases-lifecycle-analyzer-detector-restorer-builder-exporter.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://github.com/buildpacks/pack) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
