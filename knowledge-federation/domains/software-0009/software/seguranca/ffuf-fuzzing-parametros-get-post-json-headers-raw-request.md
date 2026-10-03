---
id: software.seguranca.tranche04.000335
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

# ffuf: Fuzzing de Parâmetros GET, Payloads POST JSON, Headers Customizados e Requisições Raw (`-request`)

## Em uma frase
O `ffuf` permite testar descoberta de parâmetros ocultos (`?FUZZ=1`), valores de parâmetros (`?id=FUZZ`), campos de objetos JSON via `-X POST -d` e requisições HTTP brutas exportadas de proxies interceptadores via `-request`.

## Por que importa
Permite identificar parâmetros de depuração esquecidos (`?debug=true`, `?admin=1`, `X-Forwarded-For`), *Mass Assignment* em APIs REST/GraphQL e vulnerabilidades de *Insecure Direct Object Reference* (IDOR).

## Como funciona
Com a flag `-request req.txt -request-proto https`, o analista salva uma requisição complexa autenticada (com múltiplos cookies, headers CSRF e corpo multipart ou GraphQL) em um arquivo texto, insere a keyword `FUZZ` nos pontos desejados e executa o `ffuf` sem precisar reconstruir dezenas de flags `-H` e `-b` na linha de comando.

## Exemplo
```bash
# Fuzzing de propriedades ocultas em um endpoint POST JSON usando requisição raw
ffuf -request /tmp/api-patch-user.http \
  -request-proto https \
  -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
  -ac -mc all -fc 400
```

## Limites e trade-offs
Ao realizar fuzzing de parâmetros de escrita (`POST`, `PUT`, `DELETE`) em ambientes compartilhados, payloads bem-sucedidos podem alterar estados de contas ou disparar notificações em massa; prefira métodos idempotentes ou contas de teste isoladas.

## Como verificar
Verifique com `-replay-proxy http://127.0.0.1:8080` que apenas as requisições que produziram *match* são reenviadas para inspeção detalhada.

## Conexões
- [[ffuf-descoberta-virtual-hosts-vhost-host-header-sni]] — Veja também: ffuf: Descoberta de Virtual Hosts (`Host: FUZZ`) sem Registros DNS Públicos e TLS SNI (`-sni`).
- [[ffuf-modos-multi-wordlist-clusterbomb-pitchfork-sniper-encoders]] — Veja também: ffuf: Modos Multi-Wordlist (`clusterbomb`, `pitchfork`, `sniper`) e Encoders (`-enc`).
- [[ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos]] — Referência cruzada direta com ffuf-arquitetura-web-fuzzer-go-keyword-fuzz-diretorios-arquivos.
- [[ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc]] — Referência cruzada direta com ffuf-auditoria-relatorios-json-html-csv-od-replay-proxy-ffufrc.

## Fontes
- [ffuf GitHub — README.md (Fast Web Fuzzer in Go, Content/Vhost/Parameter/POST Fuzzing, Matchers, Filters & Interactive Mode)](https://raw.githubusercontent.com/ffuf/ffuf/master/README.md) — README oficial do ffuf/ffuf documentando todos os modos de operação, flags de matcher/filter, auto-calibração, recursão e mutadores externos; consultado em 2026-10-03.
- [ffuf GitHub — ffufrc.example (Declarative TOML Configuration Reference for HTTP, General, Input, Output, Filter & Matcher Sections)](https://raw.githubusercontent.com/ffuf/ffuf/master/ffufrc.example) — Arquivo oficial de exemplo de configuração ffufrc detalhando todas as opções declarativas do ffuf; consultado em 2026-10-03.
- [ffuf Official Wiki — Advanced Usage & Configuration Guide](https://github.com/ffuf/ffuf/wiki) — Documentação oficial da wiki do projeto ffuf; consultado em 2026-10-03.
