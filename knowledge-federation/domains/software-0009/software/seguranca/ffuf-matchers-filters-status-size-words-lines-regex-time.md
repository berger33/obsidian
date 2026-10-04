---
id: software.seguranca.tranche04.000332
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

# ffuf: Precisão com Matchers (`-mc`, `-ms`, `-mw`, `-ml`, `-mr`, `-mt`) e Filters (`-fc`, `-fs`, `-fw`, `-fl`, `-fr`, `-ft`)

## Em uma frase
O `ffuf` oferece dois conjuntos simétricos de seleção de respostas HTTP: **Matchers** (o que incluir) e **Filters** (o que excluir), operando sobre status code, tamanho em bytes, contagem de palavras, contagem de linhas, regex no corpo/headers e tempo até o primeiro byte (TTFB).

## Por que importa
Aplicações web modernas (SPAs React/Vue e gateways de API) frequentemente retornam `HTTP 200 OK` para rotas inexistentes (*soft 404*) com tamanho de bytes variável, mas com um número fixo de palavras (`-fw`) ou linhas (`-fl`).

## Como funciona
Por padrão, `-mc 200-299,301,302,307,401,403,405,500` está ativo com operador de conjunto `-mmode or` e `-fmode or`. O analista pode combinar múltiplos filtros (ex.: `-fc 404,403 -fw 128 -fmode or` para descartar respostas que tenham status 404/403 **ou** exatamente 128 palavras) ou usar `-mt >2000` para detectar vulnerabilidades de injeção baseadas em tempo (*time-based blind injection*).

## Exemplo
```bash
# Fazer match em todos os status codes (-mc all), mas filtrar páginas padrão de 42 linhas ou contendo "Route not found"
ffuf -w api-endpoints.txt \
  -u https://api.staging.corp/v2/FUZZ \
  -mc all \
  -fl 42 \
  -fr "Route not found"
```

## Limites e trade-offs
Usar `-fs` (filtro por tamanho exato em bytes) quando a página de erro reflete o próprio caminho requisitado (`Cannot GET /caminho`) falha porque cada palavra da wordlist tem comprimento diferente; nesses casos, filtre por palavras (`-fw`) ou linhas (`-fl`).

## Como verificar
Compare a saída de uma requisição inválida manual e aplique `-fw <palavras>` no `ffuf`, confirmando que 100% dos *soft 404* são suprimidos.

## Conexões
- [[ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos]] — Veja também: ffuf: Arquitetura de Web Fuzzing Rápido em Go, Keyword `FUZZ` e Descoberta de Conteúdo (`-e` e `-D`).
- [[ffuf-auto-calibration-ac-acs-acc-ach-eliminacao-soft-404]] — Veja também: ffuf: Auto-Calibration (`-ac`, `-acs`, `-acc` e `-ach`) para Eliminação Automática de Falso Positivo.
- [[ffuf-descoberta-virtual-hosts-vhost-host-header-sni]] — Referência cruzada direta com ffuf-descoberta-virtual-hosts-vhost-host-header-sni.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
