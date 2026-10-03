---
id: software.seguranca.tranche01.000003
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

# Gitleaks com `pre-commit`: bloqueio preventivo de segredos na máquina do desenvolvedor antes do `git commit`

## Em uma frase
Integrar o Gitleaks ao framework **`pre-commit`** (usando o hook nativo `id: gitleaks` ou o hook containerizado `id: gitleaks-docker`) inspeciona automaticamente as alterações *staged* no momento em que o desenvolvedor executa `git commit`, abortando o commit localmente caso um segredo seja detectado.

## Por que importa
Descobrir um segredo apenas quando a pipeline de CI roda no GitHub/GitLab significa que o commit contendo a credencial já foi enviado (`git push`) para o servidor remoto, exigindo rotação imediata da chave e reescrita do histórico Git.

## Como funciona
Ao configurar o arquivo `.pre-commit-config.yaml` na raiz do repositório e rodar `pre-commit install`, o Gitleaks avalia apenas o diff preparado no índice do Git (`git diff --staged`), executando em frações de segundo a cada commit.

## Exemplo
```yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.24.2
    hooks:
      - id: gitleaks
```

## Limites e trade-offs
Embora o desenvolvedor possa contornar o hook local emergencialmente com `SKIP=gitleaks git commit -m "..."`, mantenha sempre o Gitleaks rodando também no CI (`gitleaks-action`) como controle obrigatório de branch protection.

## Como verificar
Instale o hook com `pre-commit install` e execute `pre-commit run gitleaks --all-files` para validar sua ativação.

## Conexões
- [[gitleaks-configuracao-toml-precedencia-rules-keywords-entropy]] — Veja também: Gitleaks `gitleaks.toml`: ordem de precedência da configuração e anatomia de tabelas `rules` (`regex`, `keywords`, `entropy`).
- [[gitleaks-allowlists-gitleaksignore-fingerprints-comentarios-allow]] — Veja também: Gitleaks Controle de Falsos Positivos: `[allowlist]`, comentários `gitleaks:allow` e arquivo `.gitleaksignore` por `Fingerprint`.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
