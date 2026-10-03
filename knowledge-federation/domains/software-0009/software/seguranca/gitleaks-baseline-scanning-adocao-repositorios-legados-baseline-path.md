---
id: software.seguranca.tranche01.000005
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

# Gitleaks Baseline Scanning (`--baseline-path`): adoção incremental em repositórios legados sem bloquear o CI com dívida antiga

## Em uma frase
A flag **`-b` / `--baseline-path`** do Gitleaks permite gerar um snapshot JSON inicial dos achados pré-existentes em um repositório legado e instruir varreduras futuras a reportar e falhar **apenas em novos segredos introduzidos após a baseline**.

## Por que importa
Ao ativar o Gitleaks pela primeira vez em um monorepo com 10 anos de histórico e 50.000 commits, a varredura pode encontrar centenas de chaves antigas já expiradas; se o CI quebrar por causa delas, a equipe acaba desligando o scanner.

## Como funciona
O fluxo em duas etapas consiste em: 1) rodar `gitleaks git --report-path gitleaks-baseline.json` uma vez para fotografar o passivo legado (enquanto a equipe de segurança agenda a revogação assíncrona); e 2) rodar nas pipelines subsequentes `gitleaks git --baseline-path gitleaks-baseline.json`, garantindo que nenhuma credencial nova entre a partir daquele dia.

## Exemplo
```bash
# 1. Gerar o arquivo de baseline inicial do repositório legado:
gitleaks git --report-format json --report-path .gitleaks-baseline.json .

# 2. Auditar novos commits ignorando apenas os achados já registrados na baseline:
gitleaks git --baseline-path .gitleaks-baseline.json --report-path new-leaks.json .
```

## Limites e trade-offs
Nunca commite o arquivo `.gitleaks-baseline.json` contendo os segredos em texto claro no repositório sem usar **`--redact`**, para que o próprio arquivo de baseline não se torne um índice fácil de credenciais vazadas.

## Como verificar
Confirme que `gitleaks git --baseline-path .gitleaks-baseline.json .` retorna código de saída `0` quando nenhum segredo novo foi adicionado.

## Conexões
- [[gitleaks-allowlists-gitleaksignore-fingerprints-comentarios-allow]] — Veja também: Gitleaks Controle de Falsos Positivos: `[allowlist]`, comentários `gitleaks:allow` e arquivo `.gitleaksignore` por `Fingerprint`.
- [[gitleaks-decodificacao-recursiva-arquivos-compactados-max-decode-archive-depth]] — Veja também: Gitleaks Inspeção Profunda: decodificação recursiva (`--max-decode-depth`) e varredura de arquivos compactados (`--max-archive-depth`).

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
