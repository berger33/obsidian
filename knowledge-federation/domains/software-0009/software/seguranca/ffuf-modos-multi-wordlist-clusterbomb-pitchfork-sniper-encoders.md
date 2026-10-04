---
id: software.seguranca.tranche04.000336
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

# ffuf: Modos Multi-Wordlist (`clusterbomb`, `pitchfork`, `sniper`) e Encoders (`-enc`)

## Em uma frase
Quando múltiplas wordlists são associadas a keywords distintas (`-w w1.txt:KEY1 -w w2.txt:KEY2`), o `ffuf` opera nos modos `-mode clusterbomb` (produto cartesiano) ou `-mode pitchfork` (pareamento linha a linha), aplicando encoders encadeados (`-enc`).

## Por que importa
Permite testar combinações de `PARAM=VAL` e refletir o valor exato na resposta (`-mr "VAL"`) ou iterar pares sincronizados de credenciais/tokens de teste codificados em URL-encode ou Base64 em tempo real.

## Como funciona
No modo `clusterbomb` (padrão), uma wordlist de 100 parâmetros e outra de 50 valores geram `100 × 50 = 5.000` requisições. No modo `pitchfork`, ambas as wordlists avançam juntas pelo mesmo índice (`1..N`). A flag `-enc 'VAL:urlencode b64encode'` aplica codificações sucessivas sobre a keyword antes da substituição na requisição HTTP.

## Exemplo
```bash
# Testar reflexão de parâmetros (XSS/Open Redirect) combinando nomes de parâmetros e payloads codificados
ffuf -w params.txt:PARAM -w payloads.txt:VAL \
  -mode clusterbomb \
  -enc 'VAL:urlencode' \
  -u "https://app.staging.corp/search?PARAM=VAL" \
  -mr "canary7391"
```

## Limites e trade-offs
O modo `clusterbomb` cresce geometricamente com o número de wordlists: combinar três wordlists de 1.000 linhas gera `1.000.000.000` de requisições; dimensione o produto cartesiano antes de iniciar o job.

## Como verificar
Calcule o número esperado de requisições (`wc -l` das wordlists) e valide no banner de inicialização do `ffuf` o progresso total `[:: Progress: 0/N ::]`.

## Conexões
- [[ffuf-fuzzing-parametros-get-post-json-headers-raw-request]] — Veja também: ffuf: Fuzzing de Parâmetros GET, Payloads POST JSON, Headers Customizados e Requisições Raw (`-request`).
- [[ffuf-recursao-automatica-recursion-depth-strategy-maxtime-job]] — Veja também: ffuf: Varredura Recursiva (`-recursion`, `-recursion-depth`, `-recursion-strategy`) e `-maxtime-job`.
- [[ffuf-matchers-filters-status-size-words-lines-regex-time]] — Referência cruzada direta com ffuf-matchers-filters-status-size-words-lines-regex-time.
- [[ffuf-mutadores-externos-input-cmd-radamsa-ffuf-num]] — Referência cruzada direta com ffuf-mutadores-externos-input-cmd-radamsa-ffuf-num.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
