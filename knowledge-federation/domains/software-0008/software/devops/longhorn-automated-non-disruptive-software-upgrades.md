---
id: software.devops.tranche04.000313
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

# Upgrade automatizado e não disruptivo da pilha de software do Longhorn

## Em uma frase
O README oficial destaca como diferencial arquitetural do Longhorn o **upgrade automatizado não disruptivo**: é possível atualizar toda a pilha de software do Longhorn — incluindo o Longhorn Manager, Instance Manager, UI e os motores de armazenamento em execução — sem interromper volumes montados e ativos nas aplicações (`without disrupting running volumes`).

## Por que importa
Em ambientes produtivos 24x7, exigir downtime de todos os pods stateful a cada atualização de patch de armazenamento inviabiliza a manutenção regular de segurança. O upgrade de engine ao vivo (live upgrade) do Longhorn permite manter o plano de dados operando enquanto o binário da engine do volume é atualizado.

## Como funciona
Siga sempre a matriz de releases suportadas e as notas importantes (`Important Notes`) da versão-alvo antes de iniciar o upgrade via Helm, `kubectl` ou Rancher, utilizando apenas releases oficiais publicadas em `github.com/longhorn/longhorn/releases`.

## Exemplo
Ao atualizar o Longhorn da linha `1.11.x` para `1.12.1` em produção, o operador executa primeiro a atualização do plano de controle e em seguida aciona o upgrade concorrente controlado das engines de volumes ativos sem desmontar os PVCs dos pods de aplicação.

## Limites e trade-offs
Nunca instale ou atualize clusters de produção diretamente a partir da branch `master`, que segundo o aviso oficial do repositório é destinada exclusivamente ao desenvolvimento da próxima release e pode conter mudanças instáveis.

## Como verificar
Após concluir o upgrade do Longhorn, verifique em `volumes.longhorn.io` que `currentImage` de todos os volumes em execução corresponde à versão da nova `engineImage` sem ocorrência de erros de I/O nos pods clientes.

## Conexões
- [[longhorn-incremental-snapshots-and-change-block-backups]] — Veja também: Snapshots incrementais e backups para NFSv4 ou S3 com detecção eficiente de blocos alterados.
- [[longhorn-manager-instance-manager-and-share-manager-components]] — Veja também: Componentes Longhorn Manager, Instance Manager, Share Manager e Backing Image Manager.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
