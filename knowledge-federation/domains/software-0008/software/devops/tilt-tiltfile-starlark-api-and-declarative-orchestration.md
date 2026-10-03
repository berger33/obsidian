---
id: software.devops.tranche06.000524
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/tilt-dev/tilt/master/README.md", "https://docs.tilt.dev/tutorial/index.html", "https://github.com/tilt-dev/tilt"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Autoria de Tiltfiles com Starlark e referência da API (docs.tilt.dev/api.html)

## Em uma frase
O README oficial e o guia de autoria apontam para a referência completa de funções do **`Tiltfile`** em **`docs.tilt.dev/api.html`**. O `Tiltfile` é um programa de configuração escrito em **Starlark** (um dialeto determinístico de Python criado para sistemas de build como o Bazel), no qual a equipe declara como construir imagens (`docker_build`, `custom_build`), quais manifestos Kubernetes, Kustomize ou Helm aplicar (`k8s_yaml`, `kustomize`, `helm`), como agrupar e expor recursos (`k8s_resource`) e quais comandos locais executar (`local_resource`).

## Por que importa
Por ser escrito em Starlark (uma linguagem real com funções, listas, dicionários e condicionais, mas sem efeitos colaterais arbitrários descontrolados) em vez de um YAML rígido, o `Tiltfile` permite parametrizar quais subconjuntos de serviços cada equipe deseja subir no seu laptop sem duplicar arquivos de configuração.

## Como funciona
Consulte `docs.tilt.dev/api.html` para utilizar funções nativas do `Tiltfile` que leem seus próprios manifestos existentes de produção/homologação (`k8s_yaml`, `helm`, `kustomize`), evitando manter uma definição de infraestrutura paralela apenas para desenvolvimento.

## Exemplo
Em um monorepo com 25 microsserviços, o `Tiltfile` lê um arquivo local opcional `tilt_config.json` do desenvolvedor e carrega via loop Starlark apenas os 4 serviços da squad daquele desenvolvedor, economizando memória RAM do laptop.

## Limites e trade-offs
Evite executar chamadas de rede externas lentas ou comandos shell pesados diretamente no escopo global de avaliação do `Tiltfile`; delegue tarefas assíncronas e builds aos objetos `local_resource` e `custom_build` gerenciados pelo grafo do Tilt.

## Como verificar
Execute `tilt dump engine` ou valide o carregamento do `Tiltfile` com `tilt ci --dry-run` / `tilt up` para confirmar que todas as funções Starlark avaliaram sem erros.

## Conexões
- [[tilt-tilt-ui-aggregated-logs-and-resource-status]] — Veja também: Visibilidade centralizada e agregação de logs multi-serviço na interface Tilt UI.
- [[tilt-tilt-extensions-reusable-community-modules]] — Veja também: Reutilização de funcionalidades no Tiltfile com o ecossistema Tilt Extensions (tilt-dev/tilt-extensions).

## Fontes
- [Tilt GitHub — README.md (Kubernetes for Prod, Tilt for Dev, tilt up, Tiltfile API, Extensions & Security)](https://raw.githubusercontent.com/tilt-dev/tilt/master/README.md) — README oficial do Tilt (Apache-2.0) detalhando o lema Kubernetes for Prod, Tilt for Dev, o comando tilt up para automação de observação de arquivos, build de imagens e atualização do ambiente, guias por linguagem (HTML, NodeJS, Python, Go, Java, C#), referência da API do Tiltfile, repositório tilt-extensions, telemetria anônima e reporte privado de segurança para security@docker.com.; consultado em 2026-10-03.
- [Tilt Official Documentation — First Look at Tilt Tutorial (Control Loop, Tilt UI, Smart Rebuilds & Live Update)](https://docs.tilt.dev/tutorial/index.html) — Tutorial oficial de introdução ao Tilt detalhando o loop de controle do tilt up, a interface agregadora Tilt UI, rebuilds inteligentes e o mecanismo de Live Update para sincronização instantânea de alterações em contêineres sem rebuild completo.; consultado em 2026-10-03.
- [Tilt — Official GitHub Repository](https://github.com/tilt-dev/tilt) — Repositório oficial Apache-2.0 do Tilt.; consultado em 2026-10-03.
