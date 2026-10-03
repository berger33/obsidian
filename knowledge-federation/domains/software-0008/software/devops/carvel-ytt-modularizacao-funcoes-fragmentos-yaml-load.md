---
id: software.devops.tranche16.001505
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

# Carvel ytt: modularização com funções Starlark, fragmentos YAML e `load()`

## Em uma frase
O `ytt` permite encapsular tanto cálculos Starlark quanto fragmentos completos de estruturas YAML dentro de funções reutilizáveis (`def ...: ... end`) armazenadas em módulos `.star` ou `.lib.yml` importados via `load()`.

## Por que importa
Em plataformas corporativas, dezenas de microsserviços compartilham blocos padronizados de `securityContext`, `livenessProbe`, labels de telemetria e anotações de cofre de segredos. Copiar e colar esses blocos ou usar macros de texto baseadas em indentação manual gera deriva e erros frequentes.

## Como funciona
No `ytt`, uma função definida entre `#@ def pod_security_defaults():` e `#@ end` retorna um fragmento estruturado de mapa ou lista YAML. Qualquer template do projeto pode importar essa função com `#@ load("common.lib.yml", "pod_security_defaults")` e inseri-la em qualquer nível de aninhamento do manifesto sem se preocupar com o número de espaços de recuo.

## Exemplo
```yaml
#@ def restricted_security_context():
runAsNonRoot: true
runAsUser: 65532
allowPrivilegeEscalation: false
seccompProfile:
  type: RuntimeDefault
#@ end
---
apiVersion: v1
kind: Pod
metadata:
  name: worker
spec:
  securityContext: #@ restricted_security_context()
```

## Limites e trade-offs
Arquivos com extensão `.star` contêm código Starlark puro (sem anotações `#@`), enquanto arquivos `.lib.yml` ou `.lib.yaml` permitem misturar estruturas YAML e diretivas `#@` para construir fragmentos YAML.

## Como verificar
Renderize o arquivo com `ytt -f pod.yml` e confirme que o bloco `securityContext` do Pod é expandido como um mapa YAML perfeitamente indentado.

## Conexões
- [[carvel-ytt-validacoes-customizadas-schema-validation-assert]] — Veja também: Carvel ytt: validações customizadas com `#@schema/validation` e módulo `@ytt:assert`.
- [[carvel-ytt-bibliotecas-privadas-ytt-lib-module-instanciacao]] — Veja também: Carvel ytt: bibliotecas privadas (`_ytt_lib`) e instanciação programática via `@ytt:library`.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
