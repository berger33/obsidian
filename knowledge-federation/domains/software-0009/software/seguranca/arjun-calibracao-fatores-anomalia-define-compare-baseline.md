---
id: software.seguranca.tranche09.000872
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

# Arjun (`arjun/core/anomaly.py`): Como Funciona a **Calibração dos 8 Fatores de Anomalia** (`define` & `compare`) para Zero Falsos Positivos

## Em uma frase
Para saber que um bloco de 250 parâmetros contém pelo menos um parâmetro reconhecido pelo backend, o Arjun não olha apenas o código de status HTTP (`200` vs `500`): antes de iniciar a força bruta, a função `initialize()` envia três requisições de sonda com parâmetros aleatórios inexistentes (`z` + 6 caracteres aleatórios) e executa **`define(response_1, response_2, ...)`** para estabelecer uma **Linha de Base de 8 Fatores de Anomalia**!

## Por que importa
Os fatores monitorados pelo motor `anomaly.py` do Arjun incluem: **(1) Código de Status HTTP (`same_code`)**, **(2) Corpo de Resposta Exato (`same_body`)**, **(3) Texto sem Tags HTML (`same_plaintext`)**, **(4) Número de Linhas (`lines_num`)**, **(5) Diferença de Linhas (`lines_diff`)**, **(6) Nomes dos Cabeçalhos HTTP retornados (`same_headers`)**, **(7) Destino de Redirecionamento (`same_redirect`)** e **(8) Reflexão do Nome ou Valor do Parâmetro (`param_missing` / `value_missing`)**!

## Como funciona
Se um fator variar naturalmente entre duas requisições normais (por exemplo, uma página que muda o número de linhas a cada refresh por causa de um anúncio dinâmico), o loop `while True` de calibração em `initialize()` detecta essa variação e **desativa apenas aquele fator instável (`factors[reason] = None`)**, mantendo os demais fatores ativos!

## Exemplo
```bash
# Executar o Arjun ajustando o tamanho do chunk (-c 100) para servidores com limite restrito de tamanho de URI (HTTP 414)
arjun -u https://api.internal.corp/v1/search \
  -m GET \
  -c 100 \
  -t 5 \
  -oT /cases/pentest/arjun_search_params.txt
```

## Limites e trade-offs
Diagnóstico prático: se durante um scan `-m GET` o servidor retornar erro **`HTTP 414 URI Too Long`** ou **`HTTP 400 Bad Request`** porque a query string com 250 parâmetros ultrapassou o limite `large_client_header_buffers` do Nginx/WAF (ex.: 4 KiB ou 8 KiB), reduza imediatamente o tamanho do chunk com **`-c 50`** ou **`-c 80`**!

## Como verificar
Verifique no início da saída do Arjun se aparece o aviso `Target returned HTTP 414/400, this may cause problems` e ajuste `-c` de acordo.

## Conexões
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Veja também: **Arjun (`s0md3v/Arjun`)**: Arquitetura de Descoberta de **Parâmetros HTTP Ocultos** via **Busca Binária em Chunks (`-c`)** e Detecção de Anomalias.
- [[arjun-metodos-http-get-post-json-xml-include-parametros-fixos]] — Veja também: Arjun (`-m GET|POST|JSON|XML` e `--include`): Descoberta de Atributos Ocultos em **APIs REST JSON (**Mass Assignment / BOPLA**)** e Payloads XML.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
