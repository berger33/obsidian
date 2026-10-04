---
id: software.seguranca.tranche09.000878
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

# Arjun (`-oJ`, `-oT`, **`-oB` Proxy Forwarding**): Encaminhamento Automático de Endpoints com Parâmetros Descobertos para **`mitmproxy` / ZAP / Burp**

## Em uma frase
Descobrir que o endpoint `https://api.internal.corp/v1/report` aceita os parâmetros ocultos `format`, `template_path` e `debug_sql` é apenas a metade do trabalho: o próximo passo imediato é **enviar requisições reais contendo esses parâmetros recém-descobertos para o seu proxy de interceptação ou scanner de vulnerabilidades (como `mitmproxy`, OWASP ZAP, Burp Suite, `dalfox` ou `sqlmap`)**!

## Por que importa
Em vez de copiar e colar parâmetros manualmente, a flag **`-oB [host:porta]`** (padrão `127.0.0.1:8080`, implementada em `arjun/core/exporter.py`) faz o Arjun enviar automaticamente ao final da execução uma requisição HTTP limpa contendo todos os parâmetros descobertos através do proxy escutando em `127.0.0.1:8080` (**`mitmproxy`**, **OWASP ZAP** ou **Burp Suite**)!

## Como funciona
Ao mesmo tempo, **`-oJ <arquivo.json>`** grava um dicionário JSON estruturado por URL (contendo `params`, `method` e `headers`), e **`-oT <arquivo.txt>`** grava URLs completas já montadas com os parâmetros (`https://alvo/rota?param1=xxx&param2=xxx`) prontas para alimentar o **`dalfox file`** ou **`sqlmap -m`**!

## Exemplo
```bash
# Descobrir parametros ocultos e exporta-los simultaneamente em formato URL (-oT para Dalfox/sqlmap), JSON (-oJ) e para o proxy 127.0.0.1:8080 (-oB)
arjun -u https://app.internal.corp/search \
  -w medium \
  -oT /cases/pentest/arjun_urls_with_params.txt \
  -oJ /cases/pentest/arjun_params.json \
  -oB 127.0.0.1:8080
```

## Limites e trade-offs
Veja como a saída **`-oT`** foi desenhada sob medida para encadeamento: como o arquivo `arjun_urls_with_params.txt` já sai no formato `https://app.internal.corp/search?q=1&hidden_param=2`, basta rodar em seguida **`dalfox file /cases/pentest/arjun_urls_with_params.txt`** ou **`sqlmap -m /cases/pentest/arjun_urls_with_params.txt --batch`**!

## Como verificar
Verifique na interface do `mitmproxy` ou do OWASP ZAP na porta `8080` a chegada imediata da requisição populada por `-oB`.

## Conexões
- [[arjun-controle-taxa-estabilidade-stable-rate-limit-delay-timeout]] — Veja também: Arjun: Controle de Estabilidade e Evasão de Rate-Limit (**`--stable`**, **`--rate-limit`**, **`-d` Delay**, **`-t` Threads**, **`-T` Timeout** e `--disable-redirects`).
- [[arjun-heuristicas-extracao-html-js-json-special-payloads]] — Veja também: Arjun (`arjun/plugins/heuristic.py` e `db/special.json`): Extração Heurística de Parâmetros no Código-Fonte da Resposta e Payloads Especiais.
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
