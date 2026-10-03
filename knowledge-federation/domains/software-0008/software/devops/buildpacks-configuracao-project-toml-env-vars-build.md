---
id: software.devops.tranche09.000856
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
fontes: ["https://raw.githubusercontent.com/buildpacks/pack/main/README.md", "https://raw.githubusercontent.com/buildpacks/spec/main/platform.md", "https://buildpacks.io/docs/for-app-developers/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Cloud Native Buildpacks: configuração declarativa do build com project.toml, variáveis BP_* e BPE_*

## Em uma frase
O comportamento do build e dos buildpacks pode ser parametrizado via flags da CLI (`--env`, `--buildpack`, `--path`) ou versionado declarativamente no repositório através do arquivo **`project.toml`**, utilizando variáveis de tempo de build (como `BP_JVM_VERSION`) e modificadores de ambiente de lançamento.

## Por que importa
Em vez de exigir que cada desenvolvedor decore parâmetros de linha de comando para definir a versão do Java/Node, flags de compilação do Go, arquivos a incluir/excluir ou buildpacks extras (como agentes de APM/OpenTelemetry), a equipe pode codificar essas configurações no arquivo `project.toml` na raiz do repositório. O guia `Configure build inputs` (`buildpacks.io/docs/for-app-developers/`) documenta esse padrão.

## Como funciona
Quando o `pack build` é executado em um diretório que contém um arquivo **`project.toml`** (ou apontado via `--descriptor`), o `pack` lê as tabelas `[project]` e `[build]`: (1) o bloco de lista `io.buildpacks.build.env` (`build.env`) injeta variáveis de ambiente na fase de build (por exemplo, nos Paketo Buildpacks, variáveis prefixadas com `BP_*` configuram o build, como `BP_JVM_VERSION="21"` ou `BP_GO_TARGETS="./cmd/api"`, enquanto variáveis `BPE_*` configuram variáveis da imagem final em runtime); (2) o bloco `io.buildpacks.build.buildpacks` (`build.buildpacks`) define a lista explícita de buildpacks a executar; e (3) `[io.buildpacks]` (`include` / `exclude`) filtra quais arquivos do repositório entram no contexto de build.

## Exemplo
```toml
# Exemplo de arquivo project.toml versionado na raiz do repositório para parametrizar o pack build
[_]
schema-version = "0.2"

[io.buildpacks]
exclude = ["README.md", "docs/", ".git/"]

[io.buildpacks.build]
env = [
  { name = "BP_JVM_VERSION", value = "21" }
]
```

## Limites e trade-offs
Variáveis passadas para a fase de compilação via `--env` ou na tabela `io.buildpacks.build.env` ficam visíveis aos processos `bin/detect` e `bin/build` dos buildpacks (e não devem conter segredos permanentes se um buildpack as gravar em camadas); para configurar variáveis que só devem existir quando o container iniciar em produção, configure-as no manifesto do Deployment Kubernetes (onde o `launcher` CNB as processa em tempo de inicialização).

## Como verificar
Crie um `project.toml` definindo `BP_JVM_VERSION="21"` (ou equivalente da linguagem) e execute `pack build minha-app:v1` verificando nos logs da fase `builder` a seleção da versão 21.

## Conexões
- [[buildpacks-reprodutibilidade-timestamps-caching-camadas]] — Veja também: Cloud Native Buildpacks: builds reprodutíveis (SOURCE_DATE_EPOCH / --creation-time) e cache granular de camadas.
- [[buildpacks-image-extensions-extender-dockerfile-dinamico]] — Veja também: Cloud Native Buildpacks: extensão de imagens de build e run com Image Extensions e a fase extender.
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.
- [[buildpacks-conceitos-builder-build-image-run-image-launcher]] — Referência cruzada direta com buildpacks-conceitos-builder-build-image-run-image-launcher.
- [[earthly-automacao-build-containers-earthfile-reprodutivel]] — Referência cruzada direta com earthly-automacao-build-containers-earthfile-reprodutivel.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://buildpacks.io/docs/for-app-developers/) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
