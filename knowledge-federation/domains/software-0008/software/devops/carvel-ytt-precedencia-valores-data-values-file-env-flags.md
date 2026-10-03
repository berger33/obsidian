---
id: software.devops.tranche16.001508
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-16.md"
fontes: ["https://carvel.dev/ytt/docs/v0.52.x/", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel ytt: ordem de precedência e injeção de Data Values via arquivos, variáveis de ambiente e flags CLI

## Em uma frase
O `ytt` resolve entradas de configuração combinando defaults do `#@data/values-schema`, overlays `#@data/values`, arquivos `--data-values-file`, variáveis de ambiente `--data-values-env` e flags individuais `-v` / `--data-value-yaml` segundo uma ordem estrita e determinística.

## Por que importa
Em pipelines multi-ambiente, a configuração base do serviço vem do repositório Git, os parâmetros de região vêm de um arquivo `prod-eu.yml` e segredos ou tags de build efêmeras são injetados via variáveis de ambiente ou flags da CLI no job de CI.

## Como funciona
O `ytt` avalia primeiro o `#@data/values-schema`, aplica em seguida os documentos `#@data/values` na ordem em que foram passados via `-f`, e depois sobrepõe os valores passados pelas flags específicas de dados (`--data-values-file`, `--data-values-env`, `--data-values-env-yaml`, `-v` / `--data-value`, `--data-value-yaml` e `--data-value-file`) exatamente na ordem de aparição na linha de comando.

## Exemplo
```bash
export YTT_DB_HOST="pg-prod.internal"
export YTT_DB_PORT="5432"
ytt -f schema.yml -f deployment.yml \
  --data-values-file env/prod.yml \
  --data-values-env-yaml YTT \
  --data-value-yaml replicas=5
```

## Limites e trade-offs
A flag `-v` (`--data-value`) interpreta o valor fornecido sempre como string pura (por exemplo, `-v replicas=5` passa a string `"5"`), enquanto `--data-value-yaml` faz o parse YAML do valor (passando o inteiro `5` ou booleano `true`).

## Como verificar
Use `ytt -f schema.yml --data-values-env-yaml YTT --data-value-yaml replicas=5 --data-values-inspect` para auditar o mapa final de valores antes de renderizar os manifestos.

## Conexões
- [[carvel-ytt-bibliotecas-embutidas-json-yaml-base64-sha256-regexp]] — Veja também: Carvel ytt: módulos Starlark embutidos (`@ytt:json`, `@ytt:yaml`, `@ytt:base64`, `@ytt:sha256`, `@ytt:regexp`).
- [[carvel-ytt-integracao-executavel-vs-go-module-kapp-controller]] — Veja também: Carvel ytt: padrões de integração como executável externo versus módulo Go in-process.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
