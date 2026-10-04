---
id: software.devops.tranche14.001380
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

# melange: Atualização Automatizada de Pacotes (update / melange bump) e Depuração de Pipelines (set -x)

## Em uma frase
A seção opcional `update` no arquivo do `melange` (combinada com `melange bump`) automatiza o monitoramento de novos lançamentos upstream (via GitHub Releases ou Release Monitoring) e a atualização de `version`, `epoch` e `expected-sha256`, enquanto `set -x` dentro de blocos `runs:` facilita a depuração detalhada de falhas de build.

## Por que importa
Manter centenas de pacotes livres de CVEs exige detectar novas versões upstream no mesmo dia em que são lançadas e atualizar o hash SHA-256 do tarball sem intervenção manual.

## Como funciona
Com a seção `update` declarada no YAML, ferramentas de automação atualizam a versão e recalculam o digest da fonte; caso um passo de compilação falhe, adicionar `set -x` no início do bloco `runs:` imprime cada comando expandido e as variáveis `${{targets.destdir}}` nos logs.

## Exemplo
```yaml
pipeline:
  - name: Build application with debug trace
    runs: |
      set -x
      mkdir -p "${{targets.destdir}}/usr/bin"
      cp ./bin/app "${{targets.destdir}}/usr/bin/app"
```

## Limites e trade-offs
Deixar o hash `expected-sha256` antigo ao atualizar manualmente `package.version` no YAML faz o passo `uses: fetch` abortar imediatamente por divergência de checksum.

## Como verificar
Use `melange bump` para atualizar simultaneamente a versão e o hash `expected-sha256` do tarball upstream.

## Conexões
- [[melange-multi-arch-qemu-binfmt-vars-var-transforms]] — Veja também: melange: Compilação Multi-Arquitetura com QEMU e Transformação de Variáveis (vars e var-transforms).

## Fontes
- [melange GitHub — README.md (Declarative APK Package Builder, Pipeline Builds, QEMU Multi-Arch, melange keygen, Default Substitutions & Debugging)](https://raw.githubusercontent.com/chainguard-dev/melange/main/README.md) — README oficial do chainguard-dev/melange documentando o arquivo de build, variáveis de substituição (${{package.*}}, ${{targets.destdir}}), assinatura RSA, subpackages e uso conjunto com apko; consultado em 2026-10-03.
- [melange Official Documentation — docs/BUILD-FILE.md (package, version, epoch, copyright SPDX, dependencies.provides, options & environment)](https://raw.githubusercontent.com/chainguard-dev/melange/main/docs/BUILD-FILE.md) — Especificação oficial do arquivo de build do melange detalhando version/epoch, licenças SPDX em copyright, fluxos de versão com provides e controles do gerador SCA em options; consultado em 2026-10-03.
- [Chainguard melange — Official GitHub Repository](https://github.com/chainguard-dev/melange) — Repositório oficial Apache-2.0 do melange; consultado em 2026-10-03.
