---
id: software.devops.tranche12.001176
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://docs.botkube.io/plugins/", "https://raw.githubusercontent.com/kubeshop/botkube/main/README.md", "https://github.com/kubeshop/botkube"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Botkube: Repositórios de Plugins (botkube e botkubeExtra) e Desenvolvimento de Plugins Customizados

## Em uma frase
O sistema de plugins do Botkube consome índices declarativos (`plugins-index.yaml`) distribuídos nos repositórios oficiais `botkube` (`kubeshop/botkube`) e `botkubeExtra` (`kubeshop/botkube-plugins`), além de permitir que equipes de plataforma desenvolvam e hospedem seus próprios plugins Source ou Executor em Go.

## Por que importa
Quando uma organização precisa executar verificações internas no chat (como consultar status de feature flags, acionar um script de diagnóstico de rede interno ou buscar metadados de deploy), não é necessário fazer fork do código-fonte do Botkube.

## Como funciona
Durante a instalação ou upgrade, o bloco `plugins.repositories` aponta para as URLs dos arquivos `plugins-index.yaml` da versão correspondente (ou de um repositório interno). O agente baixa e gerencia o ciclo de vida dos binários de cada plugin habilitado como processos gRPC isolados.

## Exemplo
```yaml
plugins:
  repositories:
    botkube:
      url: https://github.com/kubeshop/botkube/releases/download/v1.14.0/plugins-index.yaml
    botkubeExtra:
      url: https://github.com/kubeshop/botkube-plugins/releases/download/v1.14.0/plugins-index.yaml
```

## Limites e trade-offs
Apontar `plugins.repositories` para URLs externas no GitHub em um cluster corporativo air-gapped (sem acesso de saída à internet) faz o pod do Botkube falhar na inicialização ao tentar baixar os binários dos plugins.

## Como verificar
Em clusters com saída restrita, espelhe os binários dos plugins e o `plugins-index.yaml` em um servidor HTTP/artefatos interno acessível dentro da VPC.

## Conexões
- [[botkube-integracoes-bots-sinks-slack-discord-mattermost-elasticsearch]] — Veja também: Botkube: Comparação de Integrações Bidirecionais (Bots) e Unidirecionais (Sinks).
- [[botkube-automated-actions-autodiagnostico-eventos-kubectl]] — Veja também: Botkube: Ações Automatizadas (Actions) Disparadas por Eventos de Source Plugins.

## Fontes
- [Botkube GitHub — README.md & Official Documentation Overview (Bots vs Sinks Feature Map, Slack/Discord/Mattermost & ChatOps)](https://docs.botkube.io/plugins/) — README oficial do kubeshop/botkube (MIT) e matriz oficial de funcionalidades comparando integrações bidirecionais (Bots: Slack, Discord, Mattermost) e unidirecionais (Sinks: Elasticsearch, Webhook); consultado em 2026-10-03.
- [Botkube Official Documentation — Plugins Architecture (Source Plugins, Executor Plugins, RBAC & Repositories Index)](https://raw.githubusercontent.com/kubeshop/botkube/main/README.md) — Documentação oficial de plugins do Botkube (v1.14) detalhando Source plugins, Executor plugins, índices botkube/botkubeExtra e ações automatizadas; consultado em 2026-10-03.
- [Botkube — Official Documentation Portal](https://github.com/kubeshop/botkube) — Portal oficial de documentação do Botkube; consultado em 2026-10-03.
