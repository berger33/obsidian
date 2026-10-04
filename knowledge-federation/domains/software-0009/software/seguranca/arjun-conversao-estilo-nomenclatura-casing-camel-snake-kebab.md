---
id: software.seguranca.tranche09.000875
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

# Arjun **`--casing`**: Adaptação Automática da Wordlist às Convenções de Código do Backend (`snake_case`, `camelCase`, `kebab-case`, `lowercase`)

## Em uma frase
Linguagens e frameworks de backend seguem convenções estritas de nomenclatura de variáveis: APIs em **Python/Django/FastAPI, Ruby on Rails e PHP** costumam usar **`snake_case` (`user_id`, `access_token`, `is_admin`)**; APIs em **Java/Spring, Node.js/TypeScript e C#/.NET** costumam usar **`camelCase` (`userId`, `accessToken`, `isAdmin`)**; e rotas REST/CLI frequentemente usam **`kebab-case` (`user-id`, `access-token`)**!

## Por que importa
Se a wordlist padrão tiver uma palavra em outro formato, um backend case-sensitive que espera `accessToken` ignorará `access_token`!

## Como funciona
Conforme implementado em `arjun/plugins/wl.py` (`detect_casing` e `covert_to_case`), a flag **`--casing <exemplo>`** do Arjun analisa o exemplo que você passar — literalmente `--casing like_this` (`snake_case`), `--casing likeThis` (`camelCase`), `--casing like-this` (`kebab-case`) ou `--casing likethis` (`flat lowercase`) — e **converte automaticamente todas as 25.890 palavras da wordlist para a convenção exata daquele backend antes do scan**!

## Exemplo
```bash
# Converter automaticamente toda a wordlist do Arjun para camelCase (--casing likeThis) ao auditar uma API Node.js/Spring Boot
arjun -u https://api.internal.corp/v1/accounts \
  -m JSON \
  --casing likeThis \
  -w medium \
  -oJ /cases/pentest/arjun_camelcase_params.json
```

## Limites e trade-offs
Como descobrir qual `--casing` usar em um endpoint? Basta olhar **um único parâmetro já conhecido** daquela API (se a API já usa `?pageSize=10`, passe **`--casing likeThis`**; se já usa `?page_size=10`, passe **`--casing like_this`**)!

## Como verificar
Teste rodar o Arjun com `--casing likeThis` e `--casing like_this` em APIs críticas para garantir 100% de cobertura das convenções do desenvolvedor.

## Conexões
- [[arjun-coleta-passiva-parametros-passive-wayback-commoncrawl-otx]] — Veja também: Arjun **`--passive`**: Extração Passiva de Parâmetros Históricos do **Wayback Machine, CommonCrawl e AlienVault OTX** combinada com Validação Ativa.
- [[arjun-importacao-alvos-burpsuite-raw-request-txt-lote]] — Veja também: Arjun (`-i`): Importação de Múltiplos Alvos a partir de **Arquivos de Texto**, **Itens Exportados do Burp Suite XML** e **Requisições HTTP Brutas (`raw`)**.
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[arjun-metodos-http-get-post-json-xml-include-parametros-fixos]] — Referência cruzada direta com arjun-metodos-http-get-post-json-xml-include-parametros-fixos.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
