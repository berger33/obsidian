---
id: software.seguranca.tranche09.000896
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md", "https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example", "https://epi052.github.io/feroxbuster-docs/overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Feroxbuster: **`--replay-proxy`** e **`--replay-codes`** — Como Enviar Apenas os Achados Válidos (`200`, `301`, `403`) para o **`mitmproxy` / ZAP / Burp**

## Em uma frase
Quando você passa `--proxy http://127.0.0.1:8080` para um fuzzer de diretórios que dispara 100.000 requisições (das quais 99.950 retornam `404 Not Found`), o histórico do seu `mitmproxy`, OWASP ZAP ou Burp Suite fica poluído com 99.950 linhas de lixo `404` e consome gigabytes de RAM!

## Por que importa
O Feroxbuster resolve esse problema operacional com duas flags brilhantes: **`--replay-proxy <URL_DO_PROXY>` (`-P`)** e **`--replay-codes <STATUS_CODES>` (`-R`)**!

## Como funciona
Quando você usa `--replay-proxy http://127.0.0.1:8080 --replay-codes 200,301,302,401,403` (sem usar `--proxy`), o Feroxbuster faz as 100.000 requisições de força bruta **diretamente na velocidade máxima do Rust** (sem passar pelo proxy!) e, **apenas quando encontra uma resposta positiva que passou pelos filtros e bate com `--replay-codes`, ele reenvia aquela única requisição válida através do `--replay-proxy`**!

## Exemplo
```bash
# Varrer na velocidade nativa do Rust e reenviar APENAS os caminhos encontrados (200, 301, 302, 403) para o mitmproxy na porta 8080!
feroxbuster -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt \
  --replay-proxy http://127.0.0.1:8080 \
  --replay-codes 200,301,302,401,403 \
  -o /cases/pentest/ferox_replayed.txt
```

## Limites e trade-offs
O resultado no seu `mitmproxy` / OWASP ZAP / Burp Suite é mágico: em vez de 100.000 requisições `404` lentas, a aba de histórico do proxy recebe em segundos apenas as **35 rotas reais descobertas**, já organizadas na árvore de site (*Site Map*) e prontas para inspeção manual!

## Como verificar
Verifique no `mitmproxy` (`127.0.0.1:8080`) que apenas os códigos listados em `--replay-codes` foram recebidos.

## Conexões
- [[feroxbuster-gerenciamento-estado-state-file-resume-from-time-limit]] — Veja também: Feroxbuster: Persistência de Estado (**`ferox-*.state`**), Retomada Exata (**`--resume-from`**) e Orçamento de Tempo (**`--time-limit`**).
- [[feroxbuster-autenticacao-mtls-request-file-headers-cookies-queries]] — Veja também: Feroxbuster: Auditoria Autenticada via **`--request-file` (Raw HTTP)**, Certificados **mTLS (`--client-cert`, `--client-key`)**, `-H`, `-b` e `-Q`.
- [[feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing]] — Referência cruzada direta com feroxbuster-arquitetura-descoberta-recursiva-rust-tokio-forced-browsing.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy]] — Referência cruzada direta com arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy.

## Fontes
- [Feroxbuster Official GitHub — Fast, Simple, Recursive Content Discovery Tool Written in Rust](https://raw.githubusercontent.com/epi052/feroxbuster/main/README.md) — repositório oficial do Feroxbuster cobrindo descoberta recursiva concorrente em Rust, filtros, coleta dinâmica de palavras/backups e replay proxy; consultado em 2026-10-03.
- [Feroxbuster Official Configuration Reference (`ferox-config.toml.example`)](https://raw.githubusercontent.com/epi052/feroxbuster/main/ferox-config.toml.example) — especificação completa de todas as opções de configuração e flags do Feroxbuster (`auto_tune`, `auto_bail`, `filter_similar`, `scope`, mTLS e estado); consultado em 2026-10-03.
- [Feroxbuster Official Documentation Portal](https://epi052.github.io/feroxbuster-docs/overview/) — documentação técnica oficial do projeto Feroxbuster; consultado em 2026-10-03.
