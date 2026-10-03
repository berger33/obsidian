---
id: software.devops.tranche10.000994
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/stern/stern/master/README.md", "https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md", "https://github.com/stern/stern"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Stern: modos de saída (--output default, raw, json, extjson, ppextjson) e templates Go customizados (--template)

## Em uma frase
O Stern oferece cinco formatos predefinidos de saída via **`--output` (`-o`)** — `default`, `raw`, `json`, `extjson` e `ppextjson` — e permite compilar templates Go customizados via **`--template`** (ou `--template-file` / `-T`) com funções embutidas de parsing de JSON e cores (`extractJSONParts`, `prettyJSON`, `levelColor`).

## Por que importa
Quando os microsserviços emitem logs estruturados em JSON (contendo 20 campos internos como `trace_id`, `span_id`, `level`, `msg`, `http.status`), você às vezes quer canalizar apenas o JSON puro para o `jq` (`-o raw` ou `--only-log-lines`), e às vezes quer que o próprio Stern extraia e imprima apenas `[level] msg (trace_id)` colorido diretamente no terminal sem precisar do `jq`.

## Como funciona
Conforme documenta a seção `templates` do README oficial: (1) **Modos `--output` (`-o`)**: `default` (exibe `pod container mensagem` colorido), `raw` (imprime apenas `Message`, ideal para pipe no `jq`), `json` (serializa a struct completa do Stern com `nodeName`, `namespace`, `podName`, `containerName`, `message`, `labels` e `annotations` em JSON), `extjson` e `ppextjson` (JSON estendido/pretty-printed com nomes coloridos); e (2) **Templates Go (`--template`)**: recebe a struct com `.Message`, `.Timestamp`, `.NodeName`, `.Namespace`, `.PodName`, `.ContainerName`, `.Labels` e `.Annotations`, disponibilizando funções auxiliares como **`parseJSON`**, **`tryExtractJSONParts`**, **`prettyJSON`**, **`toRFC3339Nano`**, **`toTimestamp`**, **`levelColor`** e **`bunyanLevelColor`**.

## Exemplo
```bash
# Extrair campos específicos (level e msg) de logs JSON estruturados diretamente com a função tryExtractJSONParts do Stern
stern deployment/api --template '{{color .PodColor .PodName}} {{tryExtractJSONParts .Message "level" "msg"}}{{"\n"}}'
```

## Limites e trade-offs
Prefira usar as funções tolerantes a falhas **`tryParseJSON`**, **`tryExtractJSONParts`** ou **`prettyJSON`** dentro do `--template` em vez de `parseJSON` ou `extractJSONParts` estritas: se um container emitir uma única linha de stack trace ou pânico que não seja JSON válido (por exemplo, um log de boot ou `panic:` do runtime), `parseJSON` falhará naquela linha, enquanto `tryExtractJSONParts` e `prettyJSON` imprimirão o texto original sem interromper a formatação.

## Como verificar
Execute `stern . -n kube-system --tail 3 -o json | jq .` para inspecionar todos os metadados (`nodeName`, `podName`, `containerName`, `message`) exportados pelo modo JSON do Stern.

## Conexões
- [[stern-filtragem-linhas-include-exclude-highlight-timestamps]] — Veja também: Stern: filtragem e destaque de conteúdo de logs por Regex (--include, --exclude, --highlight) e formatação de timestamps (-t).
- [[stern-processamento-logs-locais-stdin-no-follow-condition]] — Veja também: Stern: leitura de logs via entrada padrão (--stdin), execução única (--no-follow) e filtro por condição (--condition).
- [[stern-tail-logs-multi-pod-multi-container-kubernetes]] — Referência cruzada direta com stern-tail-logs-multi-pod-multi-container-kubernetes.

## Fontes
- [Stern GitHub — README.md (Multi-Pod & Container Log Tailing, CLI Flags Table, ~/.config/stern/config.yaml & Go Templates/JSON Functions)](https://raw.githubusercontent.com/stern/stern/master/README.md) — README oficial do stern/stern (Apache-2.0) detalhando pod-query por regex ou <resource>/<name>, tabela completa de flags da CLI, arquivo ~/.config/stern/config.yaml, modos --output e funções de template Go/JSON; consultado em 2026-10-03.
- [Stern GitHub — CONTRIBUTING.md & Official Repository Guidelines](https://raw.githubusercontent.com/stern/stern/master/CONTRIBUTING.md) — Diretrizes oficiais do repositório stern/stern; consultado em 2026-10-03.
- [Stern — Official GitHub Repository](https://github.com/stern/stern) — Repositório oficial do Stern; consultado em 2026-10-03.
