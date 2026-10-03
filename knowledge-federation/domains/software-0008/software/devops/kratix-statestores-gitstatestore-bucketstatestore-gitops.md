---
id: software.devops.tranche12.001105
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
fontes: ["https://docs.kratix.io/main/quick-start", "https://raw.githubusercontent.com/syntasso/kratix/main/README.md", "https://github.com/syntasso/kratix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kratix: State Stores (GitStateStore e BucketStateStore) e Desacoplamento GitOps

## Em uma frase
State Stores no Kratix (`GitStateStore` e `BucketStateStore`) definem o repositório Git ou bucket compatível com S3 onde o Kratix persiste os manifestos gerados pelos workflows, desacoplando a geração da aplicação nos clusters de destino.

## Por que importa
Em vez de o plano de controle da plataforma deter credenciais `cluster-admin` de escrita direta sobre dezenas de clusters de produção, o Kratix grava estado declarativo num armazenamento intermediário que cada cluster consome em modo pull via Flux ou Argo CD.

## Como funciona
Quando um `WorkPlacement` é escalado para um `Destination`, o controlador do Kratix autentica no `StateStore` referenciado pelo destino (via Secret SSH/token no `GitStateStore` ou credenciais S3/IAM no `BucketStateStore`) e escreve os arquivos YAML no caminho configurado. O agente GitOps no cluster alvo detecta a mudança e aplica os recursos.

## Exemplo
```yaml
apiVersion: platform.kratix.io/v1alpha1
kind: BucketStateStore
metadata:
  name: default-bucket-store
spec:
  endpoint: seaweedfs.kratix-platform-system.svc.cluster.local:8333
  insecure: false
  bucketName: kratix-workloads
  secretRef:
    name: bucket-credentials
    namespace: kratix-platform-system
```

## Limites e trade-offs
Usar `BucketStateStore` local inseguro (como a instância SeaweedFS do quick-start) em produção sem TLS, versionamento de objetos e controle estrito de acesso expõe os manifestos de toda a frota a adulteração.

## Como verificar
Verifique as condições de reconciliação do `GitStateStore` ou `BucketStateStore` e confirme no repositório Git ou bucket S3 que os diretórios de `dependencies` e `resources` estão sendo populados sem erros de autenticação.

## Conexões
- [[kratix-workflows-pipelines-containers-input-output-metadata]] — Veja também: Kratix: Workflows Imperativos-Declarativos com Containers (/kratix/input, /kratix/output e /kratix/metadata).
- [[kratix-destinations-scheduling-label-selectors-workplacements]] — Veja também: Kratix: Destinations, Agendamento por Label Selectors e WorkPlacements.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
