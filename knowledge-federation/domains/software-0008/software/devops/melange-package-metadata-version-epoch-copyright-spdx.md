---
id: software.devops.tranche14.001372
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

# melange: Metadados de Pacote (name, version, epoch) e Atestação de Licenças SPDX (copyright)

## Em uma frase
A seção `package` do arquivo de build do `melange` define a identidade do artefato (`<name>-<version>-r<epoch>.apk`), as arquiteturas alvo (`target-architecture`) e a seção obrigatória `copyright` (com `license` SPDX, `paths`, `attestation` e `license-path`) que é embutida no SBOM do pacote.

## Por que importa
Se um pacote é recompilado com um patch de segurança para a mesma versão upstream (`3.10.12`) sem incrementar o campo `epoch`, o gerenciador `apk` não reconhece o novo pacote como uma atualização superior à versão já instalada.

## Como funciona
O campo `epoch` (iniciado em `0` e incrementado monotonicamente a cada alteração do pacote na mesma versão upstream) compõe a versão completa `${{package.full-version}}` (`<version>-r<epoch>`), enquanto `copyright` valida licenças aprovadas pela OSI e permite associar licenças distintas por glob em `paths` (por exemplo, `vendor/foo/**`).

## Exemplo
```yaml
package:
  name: hello
  version: 2.12
  epoch: 0
  description: "the GNU hello world program"
  copyright:
    - license: GPL-3.0-or-later
      paths:
        - "*"
```

## Limites e trade-offs
Alterar qualquer passo de build, flag de compilação ou patch de CVE no YAML do `melange` mantendo a mesma `version` sem incrementar o `epoch` gera colisão de versão no índice `APKINDEX`.

## Como verificar
Incremente `epoch` em `+1` sempre que modificar o build de uma mesma `version` e zere `epoch: 0` quando atualizar `version` para um novo lançamento upstream.

## Conexões
- [[melange-arquitetura-construtor-pacotes-apk-declarativo-pipelines]] — Veja também: melange: Construtor Declarativo de Pacotes APK Baseado em Pipelines para Imagens de Container.
- [[melange-environment-sandbox-hermetico-apko-build-deps]] — Veja também: melange: Ambiente de Build Hermético Declarativo (environment.contents).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
