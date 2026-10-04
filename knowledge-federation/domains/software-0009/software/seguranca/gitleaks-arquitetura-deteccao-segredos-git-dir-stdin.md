---
id: software.seguranca.tranche01.000001
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

# Gitleaks: arquitetura de detecção rápida de segredos em repositórios `git`, diretórios `dir` e `stdin`

## Em uma frase
O **Gitleaks** (licenciado sob MIT) é uma ferramenta estática escrita em Go para **detectar segredos hardcoded** — como senhas, chaves de API, tokens de acesso e chaves privadas — em repositórios Git históricos ou atuais (`gitleaks git`), diretórios/arquivos avulsos (`gitleaks dir`) e fluxos de entrada padrão (`gitleaks stdin`).

## Por que importa
Deixar uma credencial de nuvem, token de bot ou senha de banco em um commit Git — mesmo em uma branch temporária ou revertida no commit seguinte — expõe o segredo permanentemente nos objetos `.git` do repositório.

## Como funciona
Conforme a documentação oficial da v8.19.0+, o Gitleaks substituiu os comandos legados `detect` e `protect` por três modos explícitos de varredura: 1) **`gitleaks git`**: varre o histórico de commits de um repositório Git (aceitando intervalos ou `--staged`); 2) **`gitleaks dir`**: varre diretórios ou arquivos diretamente no filesystem sem depender do Git; e 3) **`gitleaks stdin`**: lê fluxos enviados via pipe.

## Exemplo
```bash
# Varrendo um repositório Git completo com saída detalhada e ocultando 100% do valor do segredo:
gitleaks git -v --redact=100 .

# Varrendo um diretório de artefatos sem histórico Git:
gitleaks dir --report-format sarif --report-path gitleaks-findings.sarif ./build-artifacts
```

## Limites e trade-offs
Por segurança em pipelines de CI/CD compartilhados, utilize a flag **`--redact`** (por exemplo `--redact=100` ou `--redact=80`) para evitar que o próprio log público da pipeline imprima em texto claro o segredo recém-detectado.

## Como verificar
Execute `gitleaks version` e `gitleaks git --no-banner -v .` na raiz de um repositório para auditar todos os commits.

## Conexões
- [[gitleaks-configuracao-toml-precedencia-rules-keywords-entropy]] — Veja também: Gitleaks `gitleaks.toml`: ordem de precedência da configuração e anatomia de tabelas `rules` (`regex`, `keywords`, `entropy`).

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
