---
id: software.devops.tranche09.000854
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

# Cloud Native Buildpacks: atualização instantânea da imagem base do SO sem recompilar a aplicação (pack rebase)

## Em uma frase
A operação **Rebase** (`pack rebase <imagem>`, executada pela fase `rebaser` do lifecycle) substitui em segundos as camadas da **Run Image** subjacente de uma **App Image** por uma versão corrigida mais recente sem recompilar nem tocar nas camadas da aplicação.

## Por que importa
Quando uma vulnerabilidade crítica (CVE) é descoberta em uma biblioteca base do sistema operacional (como `openssl`, `glibc` ou `libcrypto`) em uma empresa com 500 microsserviços, reconstruir 500 `Dockerfile`s do zero (baixando dependências Maven/npm e rodando compiladores) leva horas de fila nos runners de CI. Com o `rebase` dos Cloud Native Buildpacks, a atualização da base de uma imagem ocorre em segundos apenas trocando os ponteiros de manifesto no registry.

## Como funciona
Graças à separação estrita garantida pela ABI entre as **run image layers** (na base da imagem) e as **launch/app layers** (no topo da imagem) registrada na label `io.buildpacks.lifecycle.metadata`, quando o operador executa **`pack rebase minha-app:v1.0.0`** (ou `pack rebase --publish` diretamente contra o registry OCI), a fase **`rebaser`** do lifecycle inspeciona o manifesto da imagem, busca a versão atualizada da **Run Image** compatível com o mesmo alvo de SO/arquitetura e gera um novo manifesto OCI que aponta para as novas camadas da Run Image mantendo intactas todas as camadas superiores da aplicação (mesmos SHAs de camada, zero recompilação).

## Exemplo
```bash
# Atualizar a Run Image base de uma imagem de aplicação existente sem recompilar o código-fonte
pack rebase minha-app:v1.0.0
```

## Limites e trade-offs
A operação `pack rebase` atualiza exclusivamente as camadas pertencentes à **Run Image** (pacotes do sistema operacional base); se a vulnerabilidade CVE estiver dentro de uma dependência da própria aplicação (como um pacote `npm`, `pip`, crate Rust ou `.jar` do Maven) ou na versão da JVM/Node fornecida por uma Launch Layer de um buildpack, ainda será necessário executar `pack build` para atualizar as Launch Layers.

## Como verificar
Antes e depois de executar `pack rebase minha-app:v1.0.0`, rode `pack inspect minha-app:v1.0.0` e verifique que o digest da `Base Image` (`Run Image`) foi atualizado mantendo os mesmos digests das camadas dos buildpacks.

## Conexões
- [[buildpacks-conceitos-builder-build-image-run-image-launcher]] — Veja também: Cloud Native Buildpacks: arquitetura de Builder, Build Image, Run Image, Launch Layers e processo Launcher.
- [[buildpacks-reprodutibilidade-timestamps-caching-camadas]] — Veja também: Cloud Native Buildpacks: builds reprodutíveis (SOURCE_DATE_EPOCH / --creation-time) e cache granular de camadas.
- [[buildpacks-cli-pack-build-lifecycle-builders-oci]] — Referência cruzada direta com buildpacks-cli-pack-build-lifecycle-builders-oci.

## Fontes
- [Cloud Native Buildpacks pack GitHub — README.md (CLI for App Developers, Buildpack Authors & Platform Operators)](https://raw.githubusercontent.com/buildpacks/pack/main/README.md) — README oficial do buildpacks/pack (projeto CNCF) descrevendo o papel do pack para desenvolvedores, autores de buildpacks e operadores de plataforma; consultado em 2026-10-03.
- [Cloud Native Buildpacks Platform Specification — platform.md (Platform API 0.15, Lifecycle Phases, Rebase, SBOM & Reproducibility)](https://raw.githubusercontent.com/buildpacks/spec/main/platform.md) — Especificação oficial Platform Interface (0.15) definindo Builder, Build Image, Run Image, Launcher, fases detector/analyzer/restorer/extender/builder/exporter/creator/rebaser, Image Extensions, caching, reprodutibilidade, SBOM e transição de stacks para Target Data; consultado em 2026-10-03.
- [Cloud Native Buildpacks — App Developer Guide & Official Repository](https://buildpacks.io/docs/for-app-developers/) — Documentação oficial para desenvolvedores de aplicações e repositório buildpacks/pack; consultado em 2026-10-03.
