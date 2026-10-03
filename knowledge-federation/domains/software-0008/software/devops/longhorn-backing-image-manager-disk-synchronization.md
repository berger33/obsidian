---
id: software.devops.tranche04.000317
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

# Gerenciamento de imagens base com Longhorn Backing Image Manager

## Em uma frase
O componente **Longhorn Backing Image Manager** (`github.com/longhorn/backing-image-manager`) é responsável pelo download, sincronização entre discos e exclusão de imagens base (*backing images*) utilizadas como camada inferior compartilhada por volumes do Longhorn. Com uma *backing image*, múltiplos volumes de bloco podem ser inicializados rapidamente a partir de uma imagem de disco pré-populada (como uma imagem de sistema operacional para máquinas virtuais KubeVirt ou um snapshot de banco de dados de referência) sem duplicar o download em cada criação de PVC.

## Por que importa
Sem gerenciamento nativo de *backing images*, provisionar dezenas de volumes idênticos a partir de um template grande exige copiar gigabytes repetidamente pela rede a cada novo PVC, aumentando drasticamente o tempo de bootstrap.

## Como funciona
Cadastre imagens base recorrentes através do recurso `BackingImage` do Longhorn para que o `backing-image-manager` mantenha e sincronize o arquivo base diretamente nos discos dos nós onde as réplicas serão alocadas.

## Exemplo
Em um ambiente que executa máquinas virtuais sobre Kubernetes, a imagem qcow2/raw padrão do Linux corporativo é registrada como `BackingImage` no Longhorn, permitindo que novos volumes de VM iniciem instantaneamente sobre os blocos já sincronizados localmente nos nós.

## Limites e trade-offs
Monitore o espaço livre nos discos dos nós ao utilizar múltiplas `BackingImages` volumosas, removendo imagens base obsoletas que não possuam mais volumes dependentes para evitar esgotamento de capacidade de armazenamento.

## Como verificar
Consulte o recurso `backingimages.longhorn.io` no namespace `longhorn-system` e confirme que o estado do arquivo em cada disco alvo aparece como `ready`.

## Conexões
- [[longhorn-release-support-window-and-eol-policy]] — Veja também: Ciclo de suporte de releases ativas (1.11, 1.12, 1.13) e política de EOL de um ano no Longhorn.
- [[longhorn-installation-methods-kubectl-helm-and-rancher]] — Veja também: Instalação do Longhorn via kubectl apply, Helm Chart e Rancher App Marketplace.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
