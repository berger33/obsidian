---
id: software.devops.tranche16.001510
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

# Carvel ytt: pós-processamento seguro de gráficos Helm de terceiros sem fork de templates

## Em uma frase
O `ytt` atua como pós-processador estrutural em pipelines que consomem gráficos Helm de terceiros (`helm template ... | ytt -f - -f overlay.yml`), permitindo injetar sidecars, políticas de rede ou ajustes de recursos sem fazer fork do chart upstream.

## Por que importa
Muitos charts Helm comunitários não expõem variáveis em `values.yaml` para todos os campos do PodSpec (como `topologySpreadConstraints`, `securityContext` customizado ou anotações específicas de malha de serviço). Fazer fork do chart inteiro inviabiliza atualizações rápidas de segurança.

## Como funciona
O operador renderiza o chart upstream com `helm template` para `stdout` e canaliza o YAML resultante para `ytt -f - -f custom-overlay.yml`. O módulo `@ytt:overlay` localiza os recursos gerados pelo Helm por `kind` e `metadata.name`, valida que os alvos esperados existem (`expects=1`) e aplica cirurgicamente as modificações antes de entregar o resultado ao `kbld` e ao `kapp`.

## Exemplo
```bash
helm template ingress-nginx ingress-nginx/ingress-nginx --version 4.11.2 \
  | ytt -f - -f overlays/enforce-topology-spread.yml \
  > rendered-ingress.yml
```

## Limites e trade-offs
Se uma atualização futura do chart Helm renomear o container ou remover o recurso alvo do patch, o `ytt` interromperá imediatamente o pipeline graças à verificação padrão `expects=1` do overlay, prevenindo deploys silenciosamente incompletos.

## Como verificar
Execute o pipeline com `ytt -f rendered-helm.yml -f overlays/enforce-topology-spread.yml` e confirme a presença de `topologySpreadConstraints` no manifesto final.

## Conexões
- [[carvel-ytt-integracao-executavel-vs-go-module-kapp-controller]] — Veja também: Carvel ytt: padrões de integração como executável externo versus módulo Go in-process.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://carvel.dev/ytt/docs/v0.52.x/) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
