---
id: software.devops.tranche14.001375
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

# melange: Divisão de Artefatos em Subpacotes (subpackages e split/*) para Imagens Enxutas

## Em uma frase
A seção `subpackages` do `melange` permite que uma única compilação produza múltiplos pacotes `.apk` derivados — separando, por exemplo, a biblioteca compartilhada de runtime, os headers C (`-dev`), as páginas de manual (`-doc` via `uses: split/manpages`) e binários auxiliares.

## Por que importa
Se a documentação, páginas `man`, arquivos estáticos `.a` e headers `.h` ficarem dentro do pacote principal, todas as imagens de container de produção ficarão maiores sem necessidade.

## Como funciona
Cada entrada em `subpackages` possui seu próprio `name`, `description`, `dependencies.runtime` e `pipeline` (que move arquivos de `${{targets.destdir}}` para `${{targets.subpkgdir}}` usando pipelines como `split/manpages` ou `split/dev`), permitindo que o `apko` instale na imagem final apenas o pacote principal.

## Exemplo
```yaml
subpackages:
  - name: "hello-doc"
    description: "Documentation for hello"
    pipeline:
      - uses: split/manpages
    test:
      pipeline:
        - uses: test/docs
```

## Limites e trade-offs
Escrever um comando customizado em um `subpackage` que copia (`cp`) arquivos de `${{targets.destdir}}` para `${{targets.subpkgdir}}` em vez de movê-los (`mv`) duplica os arquivos tanto no pacote principal quanto no subpacote.

## Como verificar
Mova (`mv`) os arquivos (ou use os helpers `split/*` nativos) ao extrair subpacotes para que o pacote principal permaneça enxuto.

## Conexões
- [[melange-pipelines-reutilizaveis-uses-fetch-autoconf-go-strip]] — Veja também: melange: Pipelines Reutilizáveis (uses: fetch, autoconf, cmake, go/build e strip) e Substituições.
- [[melange-dependencies-runtime-provides-version-streams-sca]] — Veja também: melange: Resolução Automática de Dependências (SCA), provides para Version Streams e options.

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
