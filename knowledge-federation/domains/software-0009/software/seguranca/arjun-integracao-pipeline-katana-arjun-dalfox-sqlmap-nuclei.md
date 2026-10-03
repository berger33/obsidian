---
id: software.seguranca.tranche09.000880
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

# Pipeline de Caça a Vulnerabilidades em Parâmetros Ocultos: **`katana` -> `arjun` -> `dalfox` / `sqlmap` / `nuclei -dast`**

## Em uma frase
Scanners automatizados comuns testam apenas os parâmetros visíveis nos links públicos da aplicação (`?id=1`), onde outros 50 pesquisadores ou ferramentas de SAST/DAST já testaram; as vulnerabilidades críticas de **XSS, SQL Injection, SSRF e LFI** que passam despercebidas em aplicações maduras estão quase sempre em **parâmetros ocultos descobertos pelo Arjun**!

## Por que importa
Construir um pipeline de quatro estágios une o melhor de cada ferramenta: **(1) `katana`** faz o crawling profundo (incluindo JS/Headless) e descobre todos os endpoints da aplicação; **(2) `arjun -i endpoints.txt -oT params_discovered.txt`** descobre os parâmetros ocultos aceitos por cada endpoint usando busca binária rápida; e **(3) `dalfox file`**, **`sqlmap -m`** e **`nuclei -l params_discovered.txt -dast`** testam injeções exclusivamente sobre os parâmetros recém-descobertos!

## Como funciona
Isso multiplica a superfície real testada pela equipe de AppSec/Pentest com um número mínimo de requisições de rede.

## Exemplo
```bash
# Pipeline completo: descobrir endpoints com Katana -> descobrir parametros ocultos com Arjun -> testar XSS/SQLi com Dalfox e Nuclei DAST
katana -u https://app.internal.corp -jc -silent -o /cases/pentest/discovered_endpoints.txt
arjun -i /cases/pentest/discovered_endpoints.txt -w small -oT /cases/pentest/arjun_populated_urls.txt
dalfox file /cases/pentest/arjun_populated_urls.txt --silence -o /cases/pentest/dalfox_hidden_param_xss.txt
```

## Limites e trade-offs
Ao alimentar o Arjun a partir da saída do `katana`, filtre primeiro arquivos estáticos (`.css`, `.png`, `.woff2`, `.svg`) usando `grep -Ev '\.(css|png|jpg|jpeg|gif|svg|woff2?)($|\?)'` para que o Arjun gaste tempo apenas em rotas dinâmicas e endpoints de API.

## Como verificar
Documente todo parâmetro oculto não-documentado encontrado em produção e recomende à equipe de engenharia usar validação estrita de schema (ex.: `additionalProperties: false` no JSON Schema / Pydantic `extra='forbid'`).

## Conexões
- [[arjun-heuristicas-extracao-html-js-json-special-payloads]] — Veja também: Arjun (`arjun/plugins/heuristic.py` e `db/special.json`): Extração Heurística de Parâmetros no Código-Fonte da Resposta e Payloads Especiais.
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy]] — Referência cruzada direta com arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
