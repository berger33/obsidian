---
id: software.seguranca.tranche04.000331
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/ffuf/ffuf/master/README.md", "https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example", "https://github.com/ffuf/ffuf/wiki"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ffuf: Arquitetura de Web Fuzzing Rápido em Go, Keyword `FUZZ` e Descoberta de Conteúdo (`-e` e `-D`)

## Em uma frase
`ffuf` (*Fuzz Faster U Fool*, MIT) é um fuzzer web de alta performance escrito em Go que substitui marcadores de posição (`FUZZ` ou keywords customizadas) na URL (`-u`), cabeçalhos HTTP (`-H`) ou corpo de requisição (`-d`) usando goroutines concorrentes.

## Por que importa
Permite descobrir diretórios ocultos, arquivos de backup esquecidos (`.bak`, `.env`, `.git/config`) e endpoints de API não documentados em testes de intrusão autorizados e pipelines de DAST.

## Como funciona
Ao receber `-w wordlist.txt -u https://alvo.corp/FUZZ -e .php,.bak,.json`, o `ffuf` expande cada entrada da wordlist com as extensões especificadas (ou substitui `%EXT%` quando `-D` *DirSearch compatibility mode* está ativo), dispara requisições concorrentes (`-t 40` por padrão) e exibe apenas respostas que satisfazem os *matchers* e não são descartadas pelos *filters*.

## Exemplo
```bash
# Descoberta de diretórios e artefatos sensíveis ignorando comentários da wordlist (-ic)
ffuf -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt \
  -u https://staging.internal.corp/FUZZ \
  -e .json,.yaml,.bak \
  -ic -t 40 -c
```

## Limites e trade-offs
Executar `ffuf` com `-t 40` sem limite de taxa (`-rate`) contra servidores de homologação frágeis ou protegidos por WAF pode causar negação de serviço acidental ou bloqueio imediato do IP de origem.

## Como verificar
Execute `ffuf -V` e rode um teste controlado com `-maxtime 30 -s` contra um ambiente de homologação autorizado, verificando que apenas caminhos existentes são listados na saída.

## Conexões
- [[ffuf-matchers-filters-status-size-words-lines-regex-time]] — Veja também: ffuf: Precisão com Matchers (`-mc`, `-ms`, `-mw`, `-ml`, `-mr`, `-mt`) e Filters (`-fc`, `-fs`, `-fw`, `-fl`, `-fr`, `-ft`).
- [[ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404]] — Referência cruzada direta com ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404.
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — Referência cruzada direta com ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
