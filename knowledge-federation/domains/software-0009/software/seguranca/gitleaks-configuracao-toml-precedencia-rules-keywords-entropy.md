---
id: software.seguranca.tranche01.000002
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
fontes: ["https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml", "https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md", "https://github.com/gitleaks/gitleaks"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gitleaks `gitleaks.toml`: ordem de precedência da configuração e anatomia de tabelas `rules` (`regex`, `keywords`, `entropy`)

## Em uma frase
O motor de detecção do Gitleaks é governado por um arquivo TOML (`.gitleaks.toml`) que combina pré-filtragem ultra-rápida por palavras-chave (**`keywords`**), expressões regulares (**`regex`**) e cálculo de entropia de Shannon (**`entropy`**) em cada bloco de tabela `rules`.

## Por que importa
Avaliar centenas de expressões regulares complexas contra milhões de linhas de histórico Git seria lento; ao filtrar primeiro por `keywords` em minúsculas (como `"ops_"`, `"a3-"` ou `"ghp_"`) via busca de substring Aho-Corasick, o Gitleaks descarta 99% das linhas antes de invocar o motor de regex.

## Como funciona
Conforme documentado no `gitleaks --help`, o Gitleaks resolve a configuração seguindo uma **ordem estrita de precedência em 4 níveis**: 1) flag `-c` / `--config`; 2) variável de ambiente `GITLEAKS_CONFIG` (caminho do arquivo); 3) variável `GITLEAKS_CONFIG_TOML` (conteúdo TOML literal); e 4) arquivo `.gitleaks.toml` na raiz do alvo (caindo para a configuração embutida se nenhum existir).

## Exemplo
```toml
title = "Configuração corporativa estendida do Gitleaks"

[extend]
useDefault = true

[rules.corp_internal_api_token]
id = "corp-internal-api-token"
description = "Token interno de API corporativa"
regex = '''\bcorp_live_[a-zA-Z0-9]{32}\b'''
entropy = 3.5
keywords = ["corp_live_"]
```

## Limites e trade-offs
Ao criar regras customizadas para tokens internos da sua empresa, use o bloco **`[extend]` com `useDefault = true`** para herdar todas as regras oficiais do Gitleaks em vez de sobrescrevê-las acidentalmente.

## Como verificar
Teste sua configuração customizada executando `gitleaks dir -c .gitleaks.toml --enable-rule corp-internal-api-token .`.

## Conexões
- [[gitleaks-arquitetura-deteccao-segredos-git-dir-stdin]] — Veja também: Gitleaks: arquitetura de detecção rápida de segredos em repositórios `git`, diretórios `dir` e `stdin`.
- [[gitleaks-pre-commit-hook-prevencao-commits-locais-skip]] — Veja também: Gitleaks com `pre-commit`: bloqueio preventivo de segredos na máquina do desenvolvedor antes do `git commit`.

## Fontes
- [Gitleaks GitHub — README.md (Subcommands git/dir/stdin, Configuration Precedence, .gitleaksignore, Baseline & Archive Depth)](https://github.com/gitleaks/gitleaks/blob/master/config/gitleaks.toml) — README oficial do gitleaks/gitleaks detalhando instalação, subcomandos git/dir/stdin, precedência de configuração em 4 níveis, uso em pre-commit/GitHub Actions e flags de decodificação; consultado em 2026-10-03.
- [Gitleaks Official Default Config — config/gitleaks.toml (Rules, Regexes, Entropy, Keywords, SecretGroup & Global Allowlists)](https://raw.githubusercontent.com/gitleaks/gitleaks/master/README.md) — Arquivo oficial de regras padrão config/gitleaks.toml com a definição completa de allowlists globais, keywords de pré-filtro, entropia de Shannon e grupos de captura; consultado em 2026-10-03.
- [Gitleaks — Official GitHub Repository](https://github.com/gitleaks/gitleaks) — Repositório oficial open-source do Gitleaks; consultado em 2026-10-03.
