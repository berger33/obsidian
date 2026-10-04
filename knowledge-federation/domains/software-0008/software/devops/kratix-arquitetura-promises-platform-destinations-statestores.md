---
id: software.devops.tranche12.001101
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
fontes: ["https://raw.githubusercontent.com/syntasso/kratix/main/README.md", "https://docs.kratix.io/main/quick-start", "https://github.com/syntasso/kratix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kratix: Arquitetura com Promises, Platform Cluster, Destinations e State Stores

## Em uma frase
Kratix é um framework open-source de engenharia de plataforma criado pela Syntasso sobre Kubernetes que estrutura Internal Developer Platforms por meio de contratos declarativos chamados Promises, desacoplando a API consumida por desenvolvedores da entrega assíncrona via State Stores e Destinations.

## Por que importa
Sem um framework explícito para construir serviços internos sob demanda, equipes de plataforma acumulam operadores avulsos, pipelines imperativos ou templates rígidos que misturam a interface voltada ao desenvolvedor com detalhes de infraestrutura e dificultam governança de frota no Dia 2.

## Como funciona
O controlador do Kratix roda no cluster de plataforma (`kratix-platform-system`) e introduz CRDs estruturais (`Promise`, `Work`, `WorkPlacement`, `Destination`, `BucketStateStore`, `GitStateStore`). Quando uma Promise é publicada, o Kratix registra a CRD de consumo no cluster de plataforma; ao receber uma Resource Request, executa pipelines em containers isolados e grava os manifestos resultantes num State Store (Git ou S3) monitorado por agentes GitOps (Flux ou Argo CD) nos clusters de destino.

## Exemplo
```bash
kubectl apply -f https://github.com/syntasso/kratix/releases/download/latest/kratix-quick-start-installer.yaml
kubectl get pods -n kratix-platform-system
kubectl get crds | grep platform.kratix.io
kubectl get destinations.platform.kratix.io,bucketstatestores.platform.kratix.io -A
```

## Limites e trade-offs
Tratar o cluster de plataforma do Kratix como ambiente de execução direta das cargas de trabalho finais sem isolar Destinations dedicados mistura o plano de controle da IDP com o tráfego de aplicações de usuários.

## Como verificar
Verifique se o `kratix-platform-controller-manager` está `Running`, se o `cert-manager` emitiu os certificados dos webhooks e se ao menos um `Destination` e um `StateStore` aparecem prontos no cluster.

## Conexões
- [[kratix-promise-crd-api-contrato-produtor-consumidor]] — Veja também: Kratix: Definição de Promise e Contrato de API entre Produtor e Consumidor.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://docs.kratix.io/main/quick-start) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
