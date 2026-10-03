---
id: software.seguranca.tranche01.000010
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md", "https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml", "https://github.com/gitleaks/gitleaks"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gitleaks Diagnóstico de Performance (`--diagnostics`) e Governança: profiling `cpu`/`mem`/`trace`/`http` e evolução para `Betterleaks`

## Em uma frase
Para diagnosticar gargalos de expressão regular ou consumo de memória em repositórios massivos, o Gitleaks oferece as flags **`--diagnostics`** (`cpu`, `mem`, `trace` ou `http` via `net/http/pprof`) e **`--diagnostics-dir`**, além de documentar no README oficial o status *feature-complete* do Gitleaks v8 e a transição de novas funcionalidades para o **Betterleaks**.

## Por que importa
Uma única regra customizada mal escrita com *catastrophic backtracking* pode fazer a varredura de um arquivo grande travar a CPU; o profiling integrado permite identificar exatamente qual função/regra consumiu o tempo.

## Como funciona
Ao passar `--diagnostics=cpu,mem --diagnostics-dir=./prof`, o Gitleaks grava os perfis `pprof` em disco ao final da execução (ou expõe um servidor HTTP `pprof` em tempo real com `--diagnostics=http`), analisáveis diretamente com `go tool pprof`.

## Exemplo
```bash
# Executando varredura com geração de perfis de CPU e memória para análise via go tool pprof:
gitleaks git --diagnostics=cpu,mem --diagnostics-dir=./profiles .
```

## Limites e trade-offs
Conforme o aviso oficial no topo do README do Gitleaks, o Gitleaks v8 encontra-se *feature-complete* (recebendo apenas correções de segurança), enquanto novos recursos de motor estão sendo desenvolvidos no projeto irmão [Betterleaks](https://github.com/betterleaks/betterleaks).

## Como verificar
Verifique as flags de diagnóstico disponíveis com `gitleaks --help | grep diagnostics`.

## Conexões
- [[gitleaks-varredura-commits-especificos-git-log-options-ci-pr]] — Veja também: Gitleaks no CI/CD (`gitleaks git` + opções `git log`): varredura rápida apenas dos commits de um Pull Request.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
