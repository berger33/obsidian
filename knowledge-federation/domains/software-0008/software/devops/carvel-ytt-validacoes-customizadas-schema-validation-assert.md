---
id: software.devops.tranche16.001504
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

# Carvel ytt: validações customizadas com `#@schema/validation` e módulo `@ytt:assert`

## Em uma frase
O `ytt` oferece validações declarativas acopladas ao esquema (`#@schema/validation`) e asserções imperativas (`@ytt:assert`) para impor invariantes de negócio e segurança sobre os valores de configuração antes de gerar qualquer manifesto.

## Por que importa
Apenas validar tipos primitivos (como `int` ou `string`) não impede configurações operacionais inválidas, como definir `replicas: 1` em ambiente `production`, configurar `min_tls_version` abaixo de `1.2` ou habilitar dois modos mutuamente exclusivos.

## Como funciona
Com `#@schema/validation`, o autor associa regras como `min_len=1`, `one_of=["dev", "staging", "prod"]` ou funções predicado `(lambda v: v % 2 == 1, "deve ser ímpar para quórum Raft")` diretamente aos nós do `#@data/values-schema`. O motor acumula todas as violações de validação e apresenta um relatório consolidado indicando o campo e a regra violada.

## Exemplo
```yaml
#@ load("@ytt:assert", "assert")
#@data/values-schema
---
#@schema/validation one_of=["staging", "production"]
env: staging
#@schema/validation min=3
etcd_members: 3
#@schema/validation ("deve ser ímpar para quórum", lambda v: v % 2 == 1)
raft_nodes: 3
```

## Limites e trade-offs
Funções lambda dentro de `#@schema/validation` não são executadas quando o valor do campo é `None` (a menos que `when_null=False` seja ajustado), pois a nulidade é tratada separadamente por `not_null=True` ou `#@schema/nullable`.

## Como verificar
Execute `ytt -f schema-validacao.yml -v raft_nodes=4 --data-values-inspect` e confirme que o `ytt` recusa a execução exibindo a mensagem `"deve ser ímpar para quórum"`.

## Conexões
- [[carvel-ytt-overlays-patch-estrutural-matchers-expects]] — Veja também: Carvel ytt: aplicação de patches estruturais declarativos com o módulo `@ytt:overlay`.
- [[carvel-ytt-modularizacao-funcoes-fragmentos-yaml-load]] — Veja também: Carvel ytt: modularização com funções Starlark, fragmentos YAML e `load()`.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
