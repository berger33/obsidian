---
id: software.devops.tranche16.001502
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

# Carvel ytt: declaração de `#@data/values-schema` para tipagem forte e valores padrão

## Em uma frase
A anotação `#@data/values-schema` do `ytt` define o contrato de entrada (*Data Values Schema*) de um pacote de configuração, inferindo automaticamente os tipos esperados (string, int, bool, map, array) a partir dos valores padrão declarados no próprio documento de esquema.

## Por que importa
Sem um esquema estrito, passar `"true"` (string) onde um template espera `true` (booleano) ou omitir uma chave aninhada crítica pode produzir manifestos Kubernetes inválidos que só falham na admissão da API. O `#@data/values-schema` rejeita tipos incompatíveis e chaves desconhecidas imediatamente no início da execução do `ytt`.

## Como funciona
O autor cria um arquivo `schema.yml` iniciado por `#@data/values-schema`, onde cada chave declara seu valor default e, opcionalmente, modificadores como `#@schema/nullable`, `#@schema/type any=True` ou `#@schema/desc`. Quando o usuário fornece arquivos `--data-values-file` ou flags `-v` / `--data-value-yaml`, o `ytt` valida cada campo contra a árvore do schema antes de avaliar os templates.

## Exemplo
```yaml
#@data/values-schema
---
environment: production
replicas: 2
resources:
  cpu: "500m"
  memory: "512Mi"
#@schema/nullable
ingress_host: null
```

## Limites e trade-offs
Por padrão, no modo schema, qualquer chave passada em um arquivo de valores que não tenha sido declarada previamente no `#@data/values-schema` é rejeitada como erro de chave desconhecida.

## Como verificar
Execute `ytt -f schema.yml --data-values-inspect` para inspecionar os valores efetivos resolvidos e teste passar `-v replicas=invalido` para confirmar o bloqueio imediato por conflito de tipo.

## Conexões
- [[carvel-ytt-templating-estrutural-yaml-starlark-arquitetura]] — Veja também: Carvel ytt: templating estrutural de YAML guiado por árvore sintática e Starlark.
- [[carvel-ytt-overlays-patch-estrutural-matchers-expects]] — Veja também: Carvel ytt: aplicação de patches estruturais declarativos com o módulo `@ytt:overlay`.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
