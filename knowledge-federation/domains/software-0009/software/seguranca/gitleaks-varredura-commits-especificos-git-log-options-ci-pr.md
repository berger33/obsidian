---
id: software.seguranca.tranche01.000009
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

# Gitleaks no CI/CD (`gitleaks git` + opções `git log`): varredura rápida apenas dos commits de um Pull Request

## Em uma frase
O subcomando `gitleaks git` aceita flags nativas de filtragem de histórico (`--log-opts`) para inspecionar exclusivamente o intervalo de commits de um Pull Request (ex.: `origin/main..HEAD`), reduzindo o tempo de execução no CI de minutos para poucos milissegundos.

## Por que importa
Em um repositório com 100.000 commits, reescanear toda a história desde o primeiro commit de 2015 a cada Pull Request desperdiça runners de CI; o PR precisa validar apenas os commits sendo introduzidos naquela branch.

## Como funciona
Passando `--log-opts="origin/main..HEAD"` (ou `--staged` em verificações locais), o Gitleaks instrui o `git log -p` subjacente a emitir somente os patches do intervalo solicitado, mantendo uma varredura completa agendada semanalmente na branch principal.

## Exemplo
```bash
# Em um job de Pull Request, escaneando apenas os commits entre a branch base e o HEAD atual:
gitleaks git --log-opts="origin/main..HEAD" --redact=100 -v .
```

## Limites e trade-offs
No GitHub Actions ou GitLab CI, lembre-se de configurar `fetch-depth: 0` (ou buscar os commits da base do PR) no passo de checkout, pois um *shallow clone* (`fetch-depth: 1`) não terá a referência `origin/main` para calcular o intervalo de commits.

## Como verificar
Execute `gitleaks git --log-opts="-n 5" -v .` para testar a varredura restrita aos últimos 5 commits do repositório.

## Conexões
- [[gitleaks-allowlist-global-paths-regexes-stopwords-padroes]] — Veja também: Gitleaks Anatomia da `[allowlist]` Global: exclusão de lockfiles (`go.sum`, `package-lock.json`), binários e `stopwords`.
- [[gitleaks-diagnostico-performance-pprof-cpu-mem-trace-betterleaks]] — Veja também: Gitleaks Diagnóstico de Performance (`--diagnostics`) e Governança: profiling `cpu`/`mem`/`trace`/`http` e evolução para `Betterleaks`.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
