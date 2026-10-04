---
id: software.devops.tranche04.000318
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

# Instalação do Longhorn via kubectl apply, Helm Chart e Rancher App Marketplace

## Em uma frase
O Longhorn oferece três métodos oficiais de instalação e atualização documentados no repositório principal: aplicação direta de manifesto com um único comando `kubectl apply` (`install-with-kubectl`), implantação parametrizada via **Helm Chart** (`install-with-helm`) e instalação integrada pelo catálogo **Rancher App Marketplace** (`install-with-rancher`). Uma vez instalado e com os requisitos de host atendidos, o Longhorn registra seu driver CSI (`driver.longhorn.io`) e disponibiliza sua `StorageClass` para consumo imediato no cluster.

## Por que importa
Padronizar um único método de instalação por cluster é essencial porque misturar `kubectl apply` manual com releases Helm ou catálogo Rancher causa conflitos de propriedade de recursos e dificulta upgrades futuros.

## Como funciona
Em fluxos GitOps (como Argo CD ou Flux), utilize o Helm Chart oficial do Longhorn fixando a versão exata da release estável e versionando o arquivo `values.yaml` com configurações de réplicas padrão, Backup Target e seletores de nós.

## Exemplo
Ao provisionar novos clusters Kubernetes gerenciados por GitOps, a plataforma declara o chart oficial do Longhorn apontando para a versão estável `1.12.1`, configurando `defaultSettings.backupTarget` e o número padrão de réplicas por volume.

## Limites e trade-offs
Nunca atualize pelo `kubectl apply` um cluster cujo Longhorn foi instalado originalmente via Helm ou Rancher App Marketplace; mantenha o mesmo gerenciador de pacotes durante todo o ciclo de vida do cluster.

## Como verificar
Execute `kubectl get sc` e `kubectl get csidrivers` para confirmar que `driver.longhorn.io` e a `StorageClass` `longhorn` foram registrados e estão prontos para provisionar PVCs.

## Conexões
- [[longhorn-backing-image-manager-disk-synchronization]] — Veja também: Gerenciamento de imagens base com Longhorn Backing Image Manager.
- [[longhorn-ui-dashboard-and-cli-operations]] — Veja também: Operação visual e por linha de comando com Longhorn UI e Longhorn CLI.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
