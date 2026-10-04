---
id: software.devops.tranche14.001374
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

# melange: Pipelines Reutilizáveis (uses: fetch, autoconf, cmake, go/build e strip) e Substituições

## Em uma frase
A seção `pipeline` do `melange` combina pipelines embutidos reutilizáveis (`uses:` com parâmetros `with:`) e blocos de shell customizados (`runs:`), interpolando variáveis nativas como `${{package.name}}`, `${{package.version}}`, `${{targets.destdir}}`, `${{targets.subpkgdir}}`, `${{build.arch}}` e `${{build.goarch}}`.

## Por que importa
Repetir manualmente comandos `curl`, verificação de SHA-256, `./configure --prefix=/usr`, `make -j$(nproc)` e `strip` em centenas de pacotes introduz inconsistências e erros de segurança.

## Como funciona
Por exemplo, o pipeline `uses: fetch` baixa o código-fonte e valida obrigatoriamente o hash criptográfico `expected-sha256` (ou `expected-sha512`), seguido por `uses: autoconf/configure`, `uses: autoconf/make`, `uses: autoconf/make-install` e `uses: strip` para remover símbolos desnecessários e gravar o resultado em `${{targets.destdir}}`.

## Exemplo
```yaml
pipeline:
  - uses: fetch
    with:
      uri: https://ftp.gnu.org/gnu/hello/hello-${{package.version}}.tar.gz
      expected-sha256: cf04af86dc085268c5f4470fbae49b18afbc221b78096aab842d934a76bad0ab
  - uses: autoconf/configure
  - uses: autoconf/make
  - uses: autoconf/make-install
  - uses: strip
```

## Limites e trade-offs
Instalar os binários compilados no diretório `/usr/bin` da raiz do ambiente de build em vez de instalar dentro de `${{targets.destdir}}/usr/bin` gera um pacote `.apk` completamente vazio.

## Como verificar
Gravar sempre todos os arquivos finais do pacote principal sob o prefixo `${{targets.destdir}}` (ou `${{targets.contextdir}}`).

## Conexões
- [[melange-environment-sandbox-hermetico-apko-build-deps]] — Veja também: melange: Ambiente de Build Hermético Declarativo (environment.contents).
- [[melange-subpackages-split-manpages-dev-headers-runtime-minimo]] — Veja também: melange: Divisão de Artefatos em Subpacotes (subpackages e split/*) para Imagens Enxutas.

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
