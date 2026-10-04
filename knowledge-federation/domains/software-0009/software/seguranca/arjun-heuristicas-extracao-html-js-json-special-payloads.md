---
id: software.seguranca.tranche09.000879
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

# Arjun (`arjun/plugins/heuristic.py` e `db/special.json`): Extração Heurística de Parâmetros no Código-Fonte da Resposta e Payloads Especiais

## Em uma frase
Um detalhe pouco conhecido da arquitetura interna do Arjun (em `arjun/plugins/heuristic.py`) é que antes mesmo de dividir a wordlist em chunks, ele executa uma **Análise Heurística Passiva sobre a primeira resposta HTTP (`response_1`)** recebida do próprio endpoint alvo!

## Por que importa
O módulo `heuristic.py` analisa o corpo da resposta em busca de quatro fontes de nomes de parâmetros específicos daquela página: **(1)** atributos `name=` e `id=` de tags HTML `<input>`, `<textarea>` e `<select>`; **(2)** nomes de variáveis JavaScript declaradas com `var`, `let` ou `const` dentro de blocos `<script>`; **(3)** todas as chaves de objetos JSON presentes na resposta; e **(4)** palavras mencionadas em mensagens de erro do servidor (ex.: `"Missing parameter: customer_tax_id"`)!

## Como funciona
Qualquer palavra encontrada no HTML/JS/JSON da página é promovida para o topo da fila de testes, e os parâmetros especiais do arquivo **`db/special.json`** (que testam valores booleanos/debug como `debug=true`, `test=1`, `admin=1`) são mesclados automaticamente!

## Exemplo
```bash
# Executar o Arjun em um endpoint que retorna mensagens de erro JSON ou formularios HTML para acionar a extracao heuristica
arjun -u https://app.internal.corp/api/v1/export \
  -m POST \
  -w small \
  -oJ /cases/pentest/arjun_heuristic_export.json
```

## Limites e trade-offs
Preste muita atenção na linha `[+] Extracted N parameters from response for testing: ...` impressa pelo Arjun logo no início da execução: esses parâmetros vieram diretamente do código-fonte/erros da própria aplicação alvo e têm altíssima probabilidade de revelar funções ocultas!

## Como verificar
Inspecione manualmente qualquer variável JavaScript extraída pela heurística do Arjun que contenha termos como `debug`, `internal`, `mock`, `bypass` ou `role`.

## Conexões
- [[arjun-exportacao-resultados-json-txt-proxy-burp-zap-mitmproxy]] — Veja também: Arjun (`-oJ`, `-oT`, **`-oB` Proxy Forwarding**): Encaminhamento Automático de Endpoints com Parâmetros Descobertos para **`mitmproxy` / ZAP / Burp**.
- [[arjun-integracao-pipeline-katana-arjun-dalfox-sqlmap-nuclei]] — Veja também: Pipeline de Caça a Vulnerabilidades em Parâmetros Ocultos: **`katana` -> `arjun` -> `dalfox` / `sqlmap` / `nuclei -dast`**.
- [[arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias]] — Referência cruzada direta com arjun-arquitetura-descoberta-parametros-http-busca-binaria-anomalias.
- [[arjun-calibracao-fatores-anomalia-define-compare-baseline]] — Referência cruzada direta com arjun-calibracao-fatores-anomalia-define-compare-baseline.

## Fontes
- [Arjun Official GitHub — HTTP Parameter Discovery Suite](https://raw.githubusercontent.com/s0md3v/Arjun/master/README.md) — repositório oficial do Arjun cobrindo descoberta de parâmetros HTTP ocultos e suporte a GET/POST/JSON/XML; consultado em 2026-10-03.
- [Arjun Official Core Source (`arjun/__main__.py`) — Binary Search Narrower, Anomaly Calibration & CLI Flags](https://raw.githubusercontent.com/s0md3v/Arjun/master/arjun/__main__.py) — código-fonte oficial do motor do Arjun mostrando a calibração dos fatores de anomalia (`define`/`compare`), busca binária em chunks e flags CLI; consultado em 2026-10-03.
- [Arjun Official Wiki — How Arjun Works & Usage Guide](https://github.com/s0md3v/Arjun/wiki/How-Arjun-works%3F) — wiki técnica oficial do projeto Arjun detalhando o algoritmo de detecção de anomalias, extração heurística e coleta passiva; consultado em 2026-10-03.
