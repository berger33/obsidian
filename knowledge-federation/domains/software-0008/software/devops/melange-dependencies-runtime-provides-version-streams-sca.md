---
id: software.devops.tranche14.001376
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
fontes: ["https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md", "https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md", "https://github.com/chainguard-dev/melange"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# melange: Resolução Automática de Dependências (SCA), provides para Version Streams e options

## Em uma frase
O `melange` inclui um analisador embutido de composição de software (**SCA**) que inspeciona binários ELF (`so:` para bibliotecas compartilhadas e `cmd:` para executáveis) para gerar dependências e provedores automaticamente, além de suportar `dependencies.provides` para fluxos paralelos de versões (como `php-8.1` e `php-8.2` provendo `php=${{package.full-version}}`) e controles em `options` (`no-provides`, `no-depends`, `no-commands`).

## Por que importa
Em distribuições como Wolfi, manter múltiplas versões principais de linguagens (`python-3.11`, `python-3.12` ou `php-8.1`, `php-8.2`) no mesmo repositório exige que pacotes dependentes possam solicitar tanto uma linha específica quanto o alias genérico.

## Como funciona
Configurando `provides: [php=${{package.full-version}}]` em `php-8.1.yaml` e `php-8.2.yaml`, `apk add php-8.1` instala a série 8.1, enquanto `apk add php` resolve automaticamente para a versão mais recente; já `options.no-commands: true` evita que pacotes secundários registrem provedores de comandos conflitantes.

## Exemplo
```yaml
package:
  name: php-8.2
  version: 8.2.10
  epoch: 1
  dependencies:
    provides:
      - php=${{package.full-version}}
```

## Limites e trade-offs
Fixar uma versão literal estática em `provides` (como `php=8.2.10` em vez de `php=${{package.full-version}}`) faz com que futuras atualizações do pacote esquecem de atualizar o valor do `provides`.

## Como verificar
Use sempre a variável `${{package.full-version}}` nas declarações de `dependencies.provides`.

## Conexões
- [[melange-subpackages-split-manpages-dev-headers-runtime-minimo]] — Veja também: melange: Divisão de Artefatos em Subpacotes (subpackages e split/*) para Imagens Enxutas.
- [[melange-test-pipelines-verificacao-funcional-pacotes-subpackages]] — Veja também: melange: Testes Automatizados de Pacotes e Subpacotes (test.pipeline e melange test).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
