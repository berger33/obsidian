---
id: software.devops.tranche01.000100
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md", "https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Guia de contribuição, arquitetura interna (`docs/developers/README.md`) e duplo licenciamento CC-BY-4.0 / Apache 2.0

## Em uma frase
A seção Want to contribute do `README.md` principal e o rodapé de `docs/README.md` reúnem os pontos de entrada para desenvolvedores e o regime de licenças: `CONTRIBUTING.md` (visão geral dos processos), `DEVELOPMENT.md` (como começar e instalar o pipeline a partir de `HEAD` em `DEVELOPMENT.md#install-pipeline`), `./docs/developers/README.md` (leitura avançada desmistificando o funcionamento interno), filtros de issues `good first issue` e `help wanted`, e a divisão de licenças onde o conteúdo da documentação é licenciado sob **Creative Commons Attribution 4.0 (CC-BY-4.0)** e os exemplos de código e software sob **Apache 2.0 License**.

## Por que importa
Quem deseja depurar o controlador do Tekton ou contribuir com o projeto precisa saber como subir uma versão compilada de `HEAD` no seu cluster de desenvolvimento (`DEVELOPMENT.md#install-pipeline`) e onde ler a explicação aprofundada do funcionamento interno dos reconciliadores (`./docs/developers/README.md`).

## Como funciona
Comece por `CONTRIBUTING.md` e `DEVELOPMENT.md` para configurar o ambiente local de desenvolvimento, leia `./docs/developers/README.md` para entender a arquitetura interna dos controladores e escolha uma issue rotulada com `good first issue` ou `help wanted` no GitHub.

## Exemplo
O diretório `/examples` na raiz do repositório (`github.com/tektoncd/pipeline/tree/main/examples`) fornece exemplos práticos atualizados contra `HEAD` para testar recursos novos.

## Limites e trade-offs
Ao reutilizar trechos da documentação oficial ou exemplos de código, observe a distinção explícita no rodapé de `docs/README.md`: texto sob CC-BY-4.0 e código sob Apache 2.0.

## Como verificar
Conferi a seção Want to contribute no `README.md` principal e o final de `docs/README.md` em `tektoncd/pipeline`.

## Conexões
- [[tekton-remote-resolution-and-trusted-resources]] — Veja também: Reutilização remota e segurança da cadeia de suprimentos: `resolution.md` e `trusted-resources.md`.

## Fontes
- [Tekton Pipelines — README oficial](https://raw.githubusercontent.com/tektoncd/pipeline/main/README.md) — README oficial do Tekton Pipelines com os três pilares (Cloud Native, Decoupled e Typed), tabela de versão mínima do Kubernetes (até v0.61.x -> K8s 1.28+), api_compatibility_policy.md, deprecations.md e guias de migração para v1.; consultado em 2026-10-03.
- [Tekton Pipelines — Tasks and Pipelines (docs/README.md)](https://raw.githubusercontent.com/tektoncd/pipeline/main/docs/README.md) — Visão geral oficial em docs/README.md com a tabela das seis entidades (Task, TaskRun, Pipeline, PipelineRun, PipelineResource Deprecated e Run alpha), os 13 guias temáticos e licenças CC-BY-4.0 / Apache 2.0.; consultado em 2026-10-03.
