---
id: software.devops.tranche14.001379
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

# melange: Compilação Multi-Arquitetura com QEMU e Transformação de Variáveis (vars e var-transforms)

## Em uma frase
O `melange` compila pacotes para múltiplas arquiteturas (`x86_64`, `aarch64`, `armv7`, `ppc64le`, `s390x`) por padrão usando emulação **QEMU (`binfmt_misc`)** transparente e oferece as seções `vars` e `var-transforms` para transformar strings de versão upstream em formatos exigidos pelos URLs de download.

## Por que importa
Muitos projetos upstream usam tags Git ou nomes de diretórios com underscores (`2_12_0`) ou apenas major.minor (`v2.12`) que diferem da string `package.version: 2.12.0`.

## Como funciona
Com `var-transforms`, aplica-se uma expressão regular (`match` e `replace`) sobre `${{package.version}}` criando uma nova variável `${{vars.mangled-version}}` utilizável no `fetch` e no `copyright`, enquanto o runner QEMU executa o mesmo pipeline para cada arquitetura alvo.

## Exemplo
```yaml
vars:
  major-minor: "2.12"
var-transforms:
  - from: ${{package.version}}
    match: ^(\d+\.\d+)\.\d+$
    replace: $1
    to: short-version
```

## Limites e trade-offs
Esquecer de registrar os manipuladores `binfmt_misc` (`tonistiigi/binfmt`) no runner Linux `x86_64` antes de rodar `melange build --arch aarch64` causa erro `exec format error` ao iniciar binários ARM64 no ambiente de build.

## Como verificar
Configure `binfmt` no host de CI para compilações emuladas ou utilize runners nativos `x86_64` e `aarch64` passando `--arch $(uname -m)`.

## Conexões
- [[melange-assinatura-rsa-keygen-apkindex-repositorio-local]] — Veja também: melange: Assinatura Criptográfica de Pacotes APK (melange keygen, sign-index e --signing-key).
- [[melange-update-automacao-bump-versoes-debugging-set-x]] — Veja também: melange: Atualização Automatizada de Pacotes (update / melange bump) e Depuração de Pipelines (set -x).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
