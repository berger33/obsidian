---
id: software.devops.tranche04.000319
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/longhorn/longhorn/master/README.md", "https://longhorn.io/docs/latest/", "https://github.com/longhorn/longhorn"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Operação visual e por linha de comando com Longhorn UI e Longhorn CLI

## Em uma frase
O ecossistema do Longhorn inclui dois clientes oficiais mantidos em repositórios dedicados: o **Longhorn UI** (`github.com/longhorn/longhorn-ui`), um painel gráfico web intuitivo que exibe em tempo real o estado de volumes, réplicas, nós, discos, snapshots, backups e hosts; e o **Longhorn CLI** (`github.com/longhorn/cli`, `longhornctl`), uma interface de linha de comando para verificação de pré-requisitos, diagnóstico e operações automatizadas.

## Por que importa
Durante incidentes de degradação de armazenamento ou manutenção de nós, visualizar graficamente quais réplicas estão reconstruindo (`rebuilding`), quais discos estão sob pressão de espaço e acionar coleta de diagnóstico ou verificações via CLI reduz erros operacionais.

## Como funciona
Utilize o `longhornctl` em pipelines de preparação de nós para validar dependências de sistema operacional e exponha o `longhorn-ui` exclusivamente através de Ingress protegido por autenticação ou via `kubectl port-forward` para operadores autorizados.

## Exemplo
Antes de drenar um nó trabalhador para manutenção de hardware, o operador consulta o Longhorn UI (ou os CRDs correspondentes) para verificar o progresso de evacuação das réplicas daquele nó e confirmar que nenhum volume ficou com réplica única.

## Limites e trade-offs
Não exponha o serviço `longhorn-frontend` na internet ou na rede corporativa aberta sem camada de autenticação, pois o Longhorn UI concede controle administrativo completo sobre volumes, snapshots e backups do cluster.

## Como verificar
Acesse o painel `longhorn-ui` via port-forward local ou execute `longhornctl` confirmando a leitura consistente do estado de nós, discos e volumes do cluster.

## Conexões
- [[longhorn-installation-methods-kubectl-helm-and-rancher]] — Veja também: Instalação do Longhorn via kubectl apply, Helm Chart e Rancher App Marketplace.
- [[longhorn-support-bundle-diagnostics-and-security-reporting]] — Veja também: Coleta de Support Bundle para diagnóstico de bugs e reporte de vulnerabilidades no Longhorn.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
