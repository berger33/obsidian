---
id: software.devops.tranche04.000316
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

# Ciclo de suporte de releases ativas (1.11, 1.12, 1.13) e política de EOL de um ano no Longhorn

## Em uma frase
A tabela oficial de releases do Longhorn define a política de ciclo de vida das versões: branches marcadas com asterisco — atualmente **1.13\*** (`1.13.0`), **1.12\*** (`1.12.1`) e **1.11\*** (`1.11.3`) — estão sob suporte ativo (`Active ✅`) e recebem patch releases periódicas, enquanto versões anteriores (`1.10` e inferiores) já encerraram manutenção ativa. O End of Life (EOL) de cada linha de release ocorre exatamente **um ano após a primeira versão estável** daquela série, conforme documentado em `Release-Schedule-&-Support`.

## Por que importa
Permanecer em séries já fora de suporte ativo (como `1.8`, `1.9` ou `1.10`) deixa o plano de armazenamento sem correções de bugs críticos de integridade de dados e sem compatibilidade com novas versões do Kubernetes.

## Como funciona
Planeje atualizações semestrais da frota para manter os clusters sempre em uma das branches marcadas como ativas na tabela oficial (`1.11*`, `1.12*` ou `1.13*`), lendo obrigatoriamente o link de `Important Note` específico da versão antes do upgrade.

## Exemplo
Durante a auditoria trimestral de ciclo de vida de infraestrutura, a equipe identifica dois clusters ainda executando Longhorn `1.10.2` (fora da coluna Active) e programa o upgrade não disruptivo para `1.11.3` e em seguida `1.12.1`.

## Limites e trade-offs
Não salte múltiplas versões menores de uma só vez sem verificar o caminho de upgrade suportado nas `Important Notes` de cada versão intermediária.

## Como verificar
Compare a versão instalada em `kubectl -n longhorn-system get settings.longhorn.io current-longhorn-version` com a tabela de releases ativas do repositório oficial.

## Conexões
- [[longhorn-v1-engine-iscsi-and-v2-spdk-data-engines]] — Veja também: Motores de dados Longhorn Engine V1 (iSCSI) e Longhorn SPDK Engine V2 (SPDK).
- [[longhorn-backing-image-manager-disk-synchronization]] — Veja também: Gerenciamento de imagens base com Longhorn Backing Image Manager.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
