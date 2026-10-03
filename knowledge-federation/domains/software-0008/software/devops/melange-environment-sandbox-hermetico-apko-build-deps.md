---
id: software.devops.tranche14.001373
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md", "https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md", "https://github.com/chainguard-dev/melange"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# melange: Ambiente de Build Hermético Declarativo (environment.contents)

## Em uma frase
A seção `environment` do `melange` utiliza exatamente o mesmo schema declarativo do **apko** (`contents.repositories`, `contents.packages`, `environment`, `accounts`) para instanciar uma raiz de sistema de arquivos limpa e hermética onde os passos do `pipeline` serão executados.

## Por que importa
Compilar pacotes diretamente no sistema operacional do runner de CI vaza bibliotecas instaladas globalmente no host para dentro do binário resultante, quebrando a reprodutibilidade.

## Como funciona
Antes de iniciar o `pipeline`, o `melange` monta o ambiente efêmero contendo exclusivamente os pacotes de compilação listados em `environment.contents.packages` (como `build-base`, `go`, `rust`, `cmake`, `ca-certificates-bundle` e `busybox`), separando estritamente dependências de tempo de compilação das dependências de tempo de execução (`package.dependencies.runtime`).

## Exemplo
```yaml
environment:
  contents:
    repositories:
      - https://dl-cdn.alpinelinux.org/alpine/edge/main
    packages:
      - alpine-baselayout-data
      - busybox
      - build-base
      - scanelf
      - ca-certificates-bundle
```

## Limites e trade-offs
Colocar compiladores pesados (`build-base`, `gcc`, `cmake`) dentro de `package.dependencies.runtime` em vez de `environment.contents.packages` faz com que o compilador inteiro seja puxado para dentro da imagem final de produção no `apko`.

## Como verificar
Mantenha ferramentas de build apenas em `environment.contents.packages` e declare em `package.dependencies.runtime` somente o que o binário precisa para rodar.

## Conexões
- [[melange-package-metadata-version-epoch-copyright-spdx]] — Veja também: melange: Metadados de Pacote (name, version, epoch) e Atestação de Licenças SPDX (copyright).
- [[melange-pipelines-reutilizaveis-uses-fetch-autoconf-go-strip]] — Veja também: melange: Pipelines Reutilizáveis (uses: fetch, autoconf, cmake, go/build e strip) e Substituições.

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
