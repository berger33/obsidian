---
id: software.devops.tranche09.000859
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

# Cloud Native Buildpacks: empacotamento de Builders corporativos customizados (builder.toml e pack builder create)

## Em uma frase
Operadores de plataforma utilizam um arquivo `builder.toml` e o comando `pack builder create <imagem> --config builder.toml` para empacotar seus próprios buildpacks, a versão do lifecycle, a Build Image e a Run Image em um único **Builder** corporativo padronizado.

## Por que importa
Em ambientes corporativos regolados ou air-gapped, os pipelines de CI/CD não devem buscar dezenas de buildpacks avulsos da internet a cada build: a equipe de plataforma cria e homologa um único Builder interno contendo a imagem base endurecida da empresa, os buildpacks de linguagens aprovados e os buildpacks corporativos de segurança/observabilidade.

## Como funciona
O operador define um arquivo **`builder.toml`** declarando: (1) a lista de tabelas `buildpacks` com as URIs/imagens dos buildpacks incluídos; (2) a lista de grupos `order` (grupos de detecção testados sequencialmente pelo `detector` até que um grupo passe); (3) o bloco `[build]` e `[run]` apontando para a **Build Image** e a(s) **Run Image(s)** homologadas; e (4) opcionalmente a versão de `[lifecycle]`. Ao executar **`pack builder create registry.interno.com/platform/builder:v1 --config builder.toml`**, o `pack` baixa os componentes e monta a imagem do Builder pronta para ser definida como padrão com `pack config default-builder`.

## Exemplo
```bash
# Definir o builder corporativo como padrão na estação ou runner de CI e listar a configuração do pack
pack config default-builder paketobuildpacks/builder-jammy-base
pack config trusted-builders list
```

## Limites e trade-offs
Por segurança, o `pack` só utiliza o binário consolidado rápido **`creator`** se o builder estiver na lista de **Trusted Builders** (`pack config trusted-builders add <builder>` ou `--trust-builder`); se um builder customizado não for marcado como confiável, o `pack` executa as 5 fases do lifecycle em containers separados para isolar as credenciais do registry da execução de código dos buildpacks de terceiros.

## Como verificar
Execute `pack builder inspect <seu-builder-customizado>` para validar a ordem dos grupos de detecção (`Detection Order`), a versão do lifecycle e as imagens de execução incluídas.

## Conexões
- [[buildpacks-autoria-empacotamento-buildpack-toml-pack-package]] — Veja também: Cloud Native Buildpacks: criação e empacotamento de Buildpacks (buildpack.toml, bin/detect, bin/build e pack buildpack package).
- [[buildpacks-metadados-sbom-labels-oci-deprecacao-stacks]] — Veja também: Cloud Native Buildpacks: geração integrada de SBOM, labels OCI (io.buildpacks.*) e transição de Stacks para Target Data.
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.
- [[buildpacks-conceitos-builder-build-image-run-image-launcher]] — Referência cruzada direta com buildpacks-conceitos-builder-build-image-run-image-launcher.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://github.com/buildpacks/pack) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
