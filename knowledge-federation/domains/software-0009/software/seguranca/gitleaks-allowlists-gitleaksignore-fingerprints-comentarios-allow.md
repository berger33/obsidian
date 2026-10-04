---
id: software.seguranca.tranche01.000004
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

# Gitleaks Controle de Falsos Positivos: `[allowlist]`, comentários `gitleaks:allow` e arquivo `.gitleaksignore` por `Fingerprint`

## Em uma frase
Para tratar chaves de exemplo em documentação, fixtures de testes unitários e falsos positivos sem desativar regras inteiras, o Gitleaks oferece três mecanismos granulares: blocos **`[allowlist]`** no `.gitleaks.toml` (`paths`, `regexes`, `stopwords`, `commits`), comentários inline **`# gitleaks:allow`** e o arquivo **`.gitleaksignore`** baseado em **`Fingerprint`**.

## Por que importa
Se uma equipe desabilitar a regra `generic-api-key` inteira apenas porque um teste unitário contém uma string fictícia, qualquer chave real vazada no código de produção deixará de ser detectada.

## Como funciona
Cada achado do Gitleaks gera um identificador único e determinístico no formato **`Fingerprint: <commit>:<caminho-do-arquivo>:<rule-id>:<linha>`** (ex.: `cd5226711335c68be1e720b318b7bc3135a30eb2:cmd/rules/sidekiq.go:sidekiq-secret:23`). Adicionar esse fingerprint ao arquivo `.gitleaksignore` na raiz do projeto silencia exclusivamente aquela ocorrência histórica específica.

## Exemplo
```bash
# Executando o Gitleaks respeitando o arquivo .gitleaksignore (ou forçando auditoria ignorando gitleaks:allow):
gitleaks git --gitleaks-ignore-path .gitleaksignore .

# Em auditorias estritas de segurança, ignorando comentários inline "gitleaks:allow":
gitleaks git --ignore-gitleaks-allow .
```

## Limites e trade-offs
A flag `--ignore-gitleaks-allow` permite que a equipe de AppSec audite periodicamente todas as linhas onde desenvolvedores adicionaram comentários `gitleaks:allow`.

## Como verificar
Verifique no relatório JSON gerado por `gitleaks git -r findings.json` o campo `Fingerprint` exato de cada ocorrência.

## Conexões
- [[gitleaks-pre-commit-hook-prevencao-commits-locais-skip]] — Veja também: Gitleaks com `pre-commit`: bloqueio preventivo de segredos na máquina do desenvolvedor antes do `git commit`.
- [[gitleaks-baseline-scanning-adocao-repositorios-legados-baseline-path]] — Veja também: Gitleaks Baseline Scanning (`--baseline-path`): adoção incremental em repositórios legados sem bloquear o CI com dívida antiga.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
