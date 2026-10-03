---
id: software.seguranca.tranche04.000339
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

# ffuf: Geração Dinâmica de Payloads e Fuzzing Mutacional com `--input-cmd`, `--input-num` e `$FFUF_NUM`

## Em uma frase
A opção `--input-cmd` substitui wordlists estáticas pela saída padrão de um comando externo invocado para cada caso de teste (de `1` até `--input-num`), expondo o índice atual na variável de ambiente `$FFUF_NUM`.

## Por que importa
Permite acoplar mutadores estruturais como `radamsa`, geradores de tokens sequenciais ou scripts Python customizados diretamente ao motor HTTP concorrente e aos filtros do `ffuf`.

## Como funciona
Para cada iteração, o `ffuf` define `FFUF_NUM=<índice>` (usado como `--seed` reprodutível pelo mutador) ou lê payloads pré-gerados em disco (`cat payloads/$FFUF_NUM.json`). Quando um resultado produz *match*, o `ffuf` exibe a posição numérica e um `FFUFHASH` que pode ser recuperado posteriormente com `ffuf -search <FFUFHASH>`.

## Exemplo
```bash
# Pré-gerar 500 mutações JSON com radamsa e testá-las via --input-cmd filtrando HTTP 400
mkdir -p /tmp/mutated && radamsa -n 500 -o /tmp/mutated/%n.json seed-order.json

ffuf --input-cmd 'cat /tmp/mutated/$FFUF_NUM.json' \
  --input-num 500 \
  -H "Content-Type: application/json" \
  -X POST -u https://api.staging.corp/v1/orders \
  -mc 500,200 -fc 400
```

## Limites e trade-offs
Invocar um binário pesado em `--input-cmd` milhares de vezes cria gargalo de *fork/exec* no sistema operacional; pré-gerar os arquivos antes do scan ou usar wordlists canalizadas é ordens de grandeza mais rápido.

## Como verificar
Recupere o payload exato que causou um erro `HTTP 500` consultando o `FFUFHASH` retornado na saída com `ffuf -search <FFUFHASH>`.

## Conexões
- [[ffuf-rate-limiting-threads-delay-stop-flags-sa-sf-se-interativo]] — Veja também: ffuf: Controle de Taxa (`-rate`, `-p`, `-t`), Circuit Breakers (`-sf`, `-se`, `-sa`) e Modo Interativo.
- [[ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc]] — Veja também: ffuf: Padronização com `ffufrc` (`-config`), Artefatos de Resposta (`-od`), Relatórios (`-of all`) e `-replay-proxy`.
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — Referência cruzada direta com ffuf-fuzzing-parametros-get-post-json-headers-raw-request.
- [[ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders]] — Referência cruzada direta com ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
