---
id: software.seguranca.tranche09.000876
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
fontes: ["https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md", "https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py", "https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arjun (`-i`): Importação de Múltiplos Alvos a partir de **Arquivos de Texto**, **Itens Exportados do Burp Suite XML** e **Requisições HTTP Brutas (`raw`)**

## Em uma frase
Em vez de rodar o Arjun manualmente em um endpoint por vez, a flag **`-i` (`import_file`)** detecta automaticamente o formato do arquivo de entrada (via `arjun/core/importer.py`) e suporta três fontes de importação: **(1) Arquivo de Texto simples (`.txt`)** com uma URL por linha; **(2) Exportação XML do Burp Suite**; e **(3) Arquivo contendo uma Requisição HTTP Bruta completa (`raw request`)** copiada do `mitmproxy`, OWASP ZAP ou Burp!

## Por que importa
Importar uma **Requisição HTTP Bruta (`-i request.raw`)** é excelente para endpoints autenticados complexos: o Arjun lê automaticamente do arquivo bruto o método (`GET`/`POST`), o caminho, o cabeçalho `Host`, todos os cookies, o cabeçalho `Authorization` e o corpo original da requisição!

## Como funciona
Quando múltiplos endpoints são importados via `-i urls.txt`, o Arjun itera sobre cada URL saudável, realiza a calibração individual de fatores de anomalia e consolida todos os parâmetros descobertos no arquivo de saída (`-oJ` / `-oT`).

## Exemplo
```bash
# Auditar em lote uma lista de endpoints de API (-i endpoints.txt) com wordlist small e exportar tudo em JSON estruturado
arjun -i /cases/pentest/api_endpoints_list.txt \
  -w small \
  -t 5 \
  -oJ /cases/pentest/arjun_batch_results.json
```

## Limites e trade-offs
Se você usar **`-H` / `--headers`** na linha de comando para passar múltiplos cabeçalhos customizados sem arquivo raw, lembre-se da sintaxe do Arjun: separe múltiplos cabeçalhos com **`\n`** (ex.: `--headers "Authorization: Bearer TOKEN\nX-Tenant-ID: 42"`).

## Como verificar
Verifique no JSON `/cases/pentest/arjun_batch_results.json` quais endpoints da lista expuseram parâmetros ocultos.

## Conexões
- [[arjun-conversao-estilo-nomenclatura-casing-camel-snake-kebab]] — Veja também: Arjun **`--casing`**: Adaptação Automática da Wordlist às Convenções de Código do Backend (`snake_case`, `camelCase`, `kebab-case`, `lowercase`).
- [[arjun-controle-taxa-estabilidade-stable-rate-limit-delay-timeout]] — Veja também: Arjun: Controle de Estabilidade e Evasão de Rate-Limit (**`--stable`**, **`--rate-limit`**, **`-d` Delay**, **`-t` Threads**, **`-T` Timeout** e `--disable-redirects`).
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy]] — Referência cruzada direta com arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
