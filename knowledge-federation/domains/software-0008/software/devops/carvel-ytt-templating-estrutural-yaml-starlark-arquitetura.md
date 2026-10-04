---
id: software.devops.tranche16.001501
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
fontes: ["https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md", "https://carvel.dev/ytt/docs/v0.52.x/", "https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Carvel ytt: templating estrutural de YAML guiado por árvore sintática e Starlark

## Em uma frase
O Carvel `ytt` (CNCF Carvel, escrito em Go) é um motor de templating e sobreposição (*overlay*) que opera diretamente sobre a estrutura de dados YAML em vez de manipular strings de texto bruto, combinando anotações comentadas (`#@`) com a linguagem determinística Starlark.

## Por que importa
Ferramentas baseadas em templating textual (como Go templates no Helm) tratam arquivos YAML como texto livre, exigindo contagens manuais de espaços (`nindent`), escapamento frágil de aspas e gerando erros de sintaxe YAML somente após a renderização. O `ytt` elimina essa classe de falhas porque constrói e valida nós de mapas, listas e escalares YAML nativamente durante toda a avaliação.

## Como funciona
Ao processar arquivos com `ytt -f`, o parser converte os documentos YAML anotados em uma representação intermediária estruturada e executa as expressões Starlark em um ambiente *sandboxed* determinístico (sem acesso a rede, relógio ou sistema de arquivos arbitrário). As diretivas `#@` acoplam-se ao nó YAML imediatamente seguinte (ou à linha correspondente), garantindo que qualquer lista, mapa ou escalar injetado preserve tipos e indentação válidos.

## Exemplo
```yaml
#@ load("@ytt:data", "data")
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: #@ data.values.app_name
spec:
  replicas: #@ data.values.replicas
  template:
    spec:
      containers:
        - name: app
          image: #@ data.values.image_repo + ":" + data.values.image_tag
```

## Limites e trade-offs
Comentários comuns que não começam com `#@` (ou `#!`) geram erro no `ytt` para evitar que diretivas mal digitadas passem despercebidas; comentários descritivos em templates `ytt` devem usar a sintaxe explícita `#! comentário`.

## Como verificar
Execute `ytt -f template.yml -v app_name=payments -v replicas=3 -v image_repo=ghcr.io/org/pay -v image_tag=v1.4.0` e valide que o documento YAML é emitido com tipos inteiros e strings corretos.

## Conexões
- [[carvel-ytt-data-values-schema-validacao-tipagem-defaults]] — Veja também: Carvel ytt: declaração de `#@data/values-schema` para tipagem forte e valores padrão.

## Fontes
- [Carvel ytt GitHub — README.md (Structural YAML Templating, Starlark, Custom Validations, Overlays & Sandboxing)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/README.md) — README oficial do carvel-dev/ytt detalhando templating estrutural ciente de YAML, linguagem Starlark determinística, overlays e validações; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — About ytt v0.52.x (Templating, Data Values, Patching/Overlaying & Modularizing)](https://carvel.dev/ytt/docs/v0.52.x/) — Documentação oficial do Carvel ytt explicando anotações #@, Data Values, módulo @ytt:overlay, fragmentos YAML e bibliotecas _ytt_lib; consultado em 2026-10-03.
- [Carvel ytt Official Documentation — Application Programming Interfaces of ytt (Executable vs Go Module Integration)](https://raw.githubusercontent.com/carvel-dev/ytt/develop/examples/integrating-with-ytt/apis.md) — Guia oficial de integração do Carvel ytt comparando invocação como executável externo versus módulo Go in-process; consultado em 2026-10-03.
