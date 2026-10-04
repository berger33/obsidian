---
id: software.seguranca.tranche09.000873
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

# Arjun (`-m GET|POST|JSON|XML` e `--include`): Descoberta de Atributos Ocultos em **APIs REST JSON (**Mass Assignment / BOPLA**)** e Payloads XML

## Em uma frase
Em APIs REST modernas, vulnerabilidades críticas de **Mass Assignment / BOPLA (*Broken Object Property Level Authorization*, OWASP API3:2023)** ocorrem quando um endpoint `POST /api/v1/profile` ou `PUT /api/v1/users/10` faz binding automático do JSON recebido para o modelo do banco de dados: se o atacante descobrir que o objeto JSON aceita os atributos ocultos `"is_admin": true`, `"role": "superuser"`, `"balance": 99999` ou `"verified": true`, ele escala privilégio instantaneamente!

## Por que importa
A flag **`-m` (`method`)** do Arjun suporta quatro formatos nativos: **`-m GET`** (query string), **`-m POST`** (`application/x-www-form-urlencoded`), **`-m JSON`** (`application/json`, enviando até `500` chaves JSON por chunk!) e **`-m XML`**!

## Como funciona
E quando um endpoint exige que certos parâmetros obrigatórios já estejam presentes em toda requisição para não retornar erro `400 Missing required field` (por exemplo, `id=10` ou `{"user_id": 10}`), a flag **`--include`** injeta esses parâmetros fixos em todos os chunks testados pelo Arjun!

## Exemplo
```bash
# Descobrir atributos JSON ocultos (Mass Assignment / BOPLA) em uma API REST enviando o campo obrigatorio user_id via --include
arjun -u https://api.internal.corp/v1/profile/update \
  -m JSON \
  --include '{"user_id": 1042}' \
  -oJ /cases/pentest/arjun_json_mass_assignment.json
```

## Limites e trade-offs
Conforme definido em `arjun/__main__.py`, quando `-m` é diferente de `GET` (`POST`, `JSON` ou `XML`), o Arjun eleva automaticamente o chunk padrão de `250` para **`500` parâmetros por requisição**, porque o corpo de um `POST` não sofre a limitação de tamanho de URL dos servidores HTTP!

## Como verificar
Para cada atributo JSON oculto descoberto por `-m JSON`, teste-o manualmente no `mitmproxy` enviando tipos booleanos (`true`), inteiros (`1`) e strings para auditar *Mass Assignment*.

## Conexões
- [[arjun-calibracao-fatores-anomalia-define-compare-baseline]] — Veja também: Arjun (`arjun/core/anomaly.py`): Como Funciona a **Calibração dos 8 Fatores de Anomalia** (`define` & `compare`) para Zero Falsos Positivos.
- [[arjun-coleta-passiva-parametros-passive-wayback-commoncrawl-otx]] — Veja também: Arjun **`--passive`**: Extração Passiva de Parâmetros Históricos do **Wayback Machine, CommonCrawl e AlienVault OTX** combinada com Validação Ativa.
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[mitmproxy-replay-cliente-servidor-testes-regressao-idor-bola]] — Referência cruzada direta com mitmproxy-replay-cliente-servidor-testes-regressao-idor-bola.
- [[wapiti-varredura-apis-rest-openapi-swagger-json-payloads]] — Referência cruzada direta com wapiti-varredura-apis-rest-openapi-swagger-json-payloads.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
