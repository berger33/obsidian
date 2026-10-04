---
id: software.seguranca.tranche04.000338
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

# ffuf: Controle de Taxa (`-rate`, `-p`, `-t`), Circuit Breakers (`-sf`, `-se`, `-sa`) e Modo Interativo

## Em uma frase
O `ffuf` controla a pressão sobre o servidor alvo através de limite estrito de requisições por segundo (`-rate`), atraso com jitter (`-p "0.1-0.5"`), goroutines (`-t`) e disjuntores de parada automática (`-sf`, `-se`, `-sa`).

## Por que importa
Impede que o scanner continue disparando milhares de requisições inúteis após ser bloqueado por um WAF (quando >95% das respostas passam a retornar `403 Forbidden`) ou quando o serviço alvo sofre *timeouts* em cascata.

## Como funciona
A flag `-sf` interrompe a execução se mais de 95% das respostas retornarem `HTTP 403`; `-se` para em caso de erros espúrios de rede/TLS; e `-sa` combina ambos. Durante a execução, pressionar `ENTER` pausa o processo e abre o shell interativo, permitindo ajustar `rate 20`, adicionar filtros em tempo real (`afs 1042`, `afc 429`) e retomar (`resume`) sem perder o progresso.

## Exemplo
```bash
# Executar fuzzing controlado a 25 req/s com parada automática em bloqueio de WAF (-sf) ou erros (-se)
ffuf -w endpoints.txt \
  -u https://portal.staging.corp/FUZZ \
  -t 10 -rate 25 -p "0.05-0.15" \
  -sf -se -ac
```

## Limites e trade-offs
Em pipelines de CI/CD ou scripts automatizados sem terminal anexado, lembre-se de passar `-noninteractive` para desabilitar o listener de teclado do console interativo.

## Como verificar
Teste o ajuste dinâmico em terminal local pressionando `ENTER`, executando `rate 10` e `show`, e confirmando que a taxa de disparo se estabiliza em 10 req/s.

## Conexões
- [[ffuf-recursao-automatica-recursion-depth-strategy-maxtime-job]] — Veja também: ffuf: Varredura Recursiva (`-recursion`, `-recursion-depth`, `-recursion-strategy`) e `-maxtime-job`.
- [[ffuf-mutadores-externos-input-cmd-radamsa-ffuf-num]] — Veja também: ffuf: Geração Dinâmica de Payloads e Fuzzing Mutacional com `--input-cmd`, `--input-num` e `$FFUF_NUM`.
- [[ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos]] — Referência cruzada direta com ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos.
- [[ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc]] — Referência cruzada direta com ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
