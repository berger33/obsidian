---
id: software.devops.tranche04.000315
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

# Motores de dados Longhorn Engine V1 (iSCSI) e Longhorn SPDK Engine V2 (SPDK)

## Em uma frase
A arquitetura de bibliotecas do Longhorn documentada no repositório oficial abrange dois motores principais de plano de dados: o **Longhorn Engine** (`longhorn/longhorn-engine`) apoiado por `longhorn/go-iscsi-helper`, que implementa a lógica central V1 de controlador e réplica usando cliente e servidor **iSCSI**; e o **Longhorn SPDK Engine** (`longhorn/longhorn-spdk-engine`) apoiado por `longhorn/go-spdk-helper`, que implementa a lógica central V2 de controlador e réplica sobre o **Storage Performance Development Kit (SPDK)** em espaço de usuário.

## Por que importa
Enquanto a engine V1 baseada em iSCSI oferece ampla compatibilidade e maturidade geral em qualquer kernel Linux padrão com `open-iscsi`, a engine V2 baseada em SPDK reduz sobrecarga de contexto de kernel e acelera o desempenho de IOPS e latência sobre dispositivos NVMe modernos.

## Como funciona
Para a engine V1 padrão, garanta que `open-iscsi` esteja instalado e com o daemon `iscsid` ativo em todos os nós do cluster; para adotar a engine V2 SPDK, valide os requisitos de memória hugepages, CPU e drivers NVMe na documentação oficial da versão instalada.

## Exemplo
Em um cluster de bancos de dados de alta performance com SSDs NVMe locais, a equipe avalia o motor V2 (`longhorn-spdk-engine`) em uma StorageClass dedicada enquanto mantém a StorageClass padrão com a engine V1 (`longhorn-engine`) para workloads gerais.

## Limites e trade-offs
Não tente provisionar volumes V1 em nós onde o pacote `open-iscsi` não está instalado ou em execução, nem habilite a engine V2 sem alocar previamente `hugepages` nos nós trabalhadores, sob pena de falha imediata na criação das réplicas.

## Como verificar
Verifique os pré-requisitos dos nós com a ferramenta de checagem do Longhorn (`longhornctl` / script de ambiente) e inspecione o campo `dataEngine` (`v1` ou `v2`) nos recursos `Volume` e `StorageClass`.

## Conexões
- [[longhorn-manager-instance-manager-and-share-manager-components]] — Veja também: Componentes Longhorn Manager, Instance Manager, Share Manager e Backing Image Manager.
- [[longhorn-release-support-window-and-eol-policy]] — Veja também: Ciclo de suporte de releases ativas (1.11, 1.12, 1.13) e política de EOL de um ano no Longhorn.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
