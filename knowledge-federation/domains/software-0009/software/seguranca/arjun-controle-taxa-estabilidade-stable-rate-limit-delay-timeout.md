---
id: software.seguranca.tranche09.000877
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

# Arjun: Controle de Estabilidade e Evasão de Rate-Limit (**`--stable`**, **`--rate-limit`**, **`-d` Delay**, **`-t` Threads**, **`-T` Timeout** e `--disable-redirects`)

## Em uma frase
Servidores protegidos por WAFs sensíveis ou rate-limiters por IP (como Cloudflare, AWS WAF ou Nginx `limit_req_zone`) podem retornar `HTTP 429 Too Many Requests` quando recebem requisições de 250 parâmetros em 5 threads simultâneas (`-t 5`); e se uma resposta no meio da busca binária retornar `429`, o algoritmo de divisão pode confundir o bloqueio de rate-limit com uma anomalia de parâmetro!

## Por que importa
Para evitar completamente falsos positivos ou bloqueios em alvos sensíveis, o Arjun oferece três controles em `arjun/__main__.py`: **(1) `--stable`** (reduz automaticamente `threads = 1` e adiciona pausas adaptativas para priorizar estabilidade máxima sobre velocidade!), **(2) `--rate-limit <req_por_seg>`** e **(3) `-d <segundos>`** (atraso fixo entre requisições, que também força `threads = 1`)!

## Como funciona
Adicionalmente, a flag **`--disable-redirects`** impede que o Arjun siga redirecionamentos `301`/`302` quando você quer detectar anomalias diretamente na primeira resposta do endpoint.

## Exemplo
```bash
# Executar o Arjun em modo de estabilidade maxima (--stable) com limite de 3 requisicoes por segundo e sem seguir redirecionamentos
arjun -u https://app.internal.corp/admin/config \
  --stable \
  --rate-limit 3 \
  --timeout 20 \
  --disable-redirects \
  -oJ /cases/pentest/arjun_stable_admin.json
```

## Limites e trade-offs
Sempre que você suspeitar que um endpoint possui um parâmetro oculto de **Open Redirect** (`?next=`, `?url=`, `?return_to=`, `?redirect_uri=`), passe **`--disable-redirects`** para que o Arjun detecte imediatamente a mudança no cabeçalho `Location` da resposta `302` sem precisar carregar o site de destino!

## Como verificar
Monitore se o Arjun reporta timeouts e aumente `-T` (timeout em segundos, padrão `15`) em endpoints de relatórios lentos.

## Conexões
- [[arjun-importacao-alvos-burpsuite-raw-request-txt-lote]] — Veja também: Arjun (`-i`): Importação de Múltiplos Alvos a partir de **Arquivos de Texto**, **Itens Exportados do Burp Suite XML** e **Requisições HTTP Brutas (`raw`)**.
- [[arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy]] — Veja também: Arjun (`-oJ`, `-oT`, **`-oB` Proxy Forwarding**): Encaminhamento Automático de Endpoints com Parâmetros Descobertos para **`mitmproxy` / ZAP / Burp**.
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[arjun-calibracao-fatores-anomalia-define-compare-baseline]] — Referência cruzada direta com arjun-calibracao-fatores-anomalia-define-compare-baseline.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
