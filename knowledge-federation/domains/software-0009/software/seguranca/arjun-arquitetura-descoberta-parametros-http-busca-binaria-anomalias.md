---
id: software.seguranca.tranche09.000871
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

# **Arjun (`s0md3v/Arjun`)**: Arquitetura de Descoberta de **Parâmetros HTTP Ocultos** via **Busca Binária em Chunks (`-c`)** e Detecção de Anomalias

## Em uma frase
Criado por Somdev Sangwan (`s0md3v/Arjun`, licença GPLv3, escrito em Python), o **Arjun** é a suíte especializada em descobrir **parâmetros HTTP não-documentados ou ocultos** (`?debug=1`, `?admin=true`, `?role=`, `?redirect=`, `?file=`, `?template=`) em endpoints web e APIs.

## Por que importa
Por que testar uma wordlist de **25.890 nomes de parâmetros** um por um com um fuzzer tradicional exigiria **25.890 requisições HTTP por endpoint**, enquanto o Arjun descobre os parâmetros válidos do mesmo endpoint fazendo apenas **50 a 60 requisições em menos de 10 segundos**? A resposta arquitetural (visível em `arjun/__main__.py` e `arjun/core/anomaly.py`) é o uso de **Agrupamento em Chunks (`-c`, padrão `250` em GET e `500` em POST/JSON) combinado com Busca Binária (`narrower` / `slicer`)**!

## Como funciona
Como a maioria dos servidores aceita centenas de parâmetros na mesma requisição HTTP (`?p1=v1&p2=v2...&p250=v250`), o Arjun envia **250 parâmetros de uma só vez**: se a resposta HTTP não mudar em relação à linha de base (*baseline*), **todos os 250 parâmetros são descartados em 1 única requisição**! Se houver qualquer anomalia na resposta, o Arjun divide aquele bloco de 250 ao meio (`125 -> 62 -> 31 -> 16 -> 8 -> 4 -> 2 -> 1`) até isolar em $\approx \log_2(250) = 8$ requisições o parâmetro exato que alterou o comportamento do servidor!

## Exemplo
```bash
# Verificar a instalacao do Arjun e descobrir parametros GET ocultos em um endpoint usando a wordlist padrao de 25.890 nomes
arjun -u https://api.internal.corp/v1/userinfo -oJ /cases/pentest/arjun_userinfo_params.json
```

## Limites e trade-offs
Além da busca binária sobre o dicionário `db/large.txt`, na fase inicial (`heuristic()` em `arjun/__main__.py`) o Arjun analisa o próprio HTML/JS/JSON da resposta do endpoint para extrair nomes de variáveis, inputs e chaves JSON e testá-los prioritariamente, além de injetar payloads especiais de `db/special.json`!

## Como verificar
Inspecione o arquivo `/cases/pentest/arjun_userinfo_params.json` para ver os parâmetros descobertos, o método e os cabeçalhos utilizados.

## Conexões
- [[arjun-calibracao-fatores-anomalia-define-compare-baseline]] — Veja também: Arjun (`arjun/core/anomaly.py`): Como Funciona a **Calibração dos 8 Fatores de Anomalia** (`define` & `compare`) para Zero Falsos Positivos.
- [[arjun-metodos-http-get-post-json-xml-include-parametros-fixos]] — Referência cruzada direta com arjun-metodos-http-get-post-json-xml-include-parametros-fixos.
- [[gobuster-modo-fuzz-marcador-customizado-url-headers-body-parametros]] — Referência cruzada direta com gobuster-modo-fuzz-marcador-customizado-url-headers-body-parametros.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
