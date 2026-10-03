---
id: software.devops.tranche02.000115
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md", "https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Garantia de restauração de backups entre versões N-2 menores do Velero

## Em uma frase
Na seção `Velero compatibility matrix`, o README documenta que, para cada lançamento, os mantenedores executam testes para garantir o caminho de upgrade a partir de `n-2` versões menores (`n-2 minor release`): por exemplo, antes do lançamento da `v1.10.x`, o teste verifica que backups criados pelas versões `v1.9.x` e `v1.8.x` podem ser restaurados usando a build da `v1.10.x`.

## Por que importa
Em cenários de retenção longa ou atualização gradual da frota, saber que uma versão nova restaura backups gerados até duas versões menores atrás define o salto máximo seguro durante upgrades do Velero.

## Como funciona
Atualize o Velero respeitando saltos de no máximo duas versões menores por vez e valide que os backups existentes no bucket continuam listáveis e restauráveis após o upgrade.

## Exemplo
Uma equipe em Velero `1.16` pode atualizar diretamente para `1.18` dentro da janela de compatibilidade `n-2`, validando a restauração de um backup anterior em homologação.

## Limites e trade-offs
Saltar três ou mais versões menores de uma só vez extrapola a janela `n-2` testada no pipeline de release; faça upgrades graduais ou gere um novo backup completo após cada etapa.

## Como verificar
Conferi o parágrafo final da subseção Velero compatibility matrix no README oficial de `vmware-tanzu/velero`.

## Conexões
- [[velero-kubernetes-compatibility-matrix]] — Veja também: Matriz de compatibilidade do Velero 1.14 a 1.18 com versões do Kubernetes.
- [[velero-ipv4-ipv6-and-dual-stack-support]] — Veja também: Suporte a ambientes IPv4, IPv6 e dual-stack no Velero.

## Fontes
- [Velero — GitHub README](https://raw.githubusercontent.com/vmware-tanzu/velero/main/README.md) — Visão geral do Velero para backup, restore e migração de recursos e volumes Kubernetes, matriz de compatibilidade (1.14–1.18), teste de upgrade N-2 e suporte IPv4/IPv6/dual-stack.; consultado em 2026-10-03.
- [Velero — Architecture Guide (ARCHITECTURE.md)](https://raw.githubusercontent.com/vmware-tanzu/velero/main/ARCHITECTURE.md) — Guia oficial de arquitetura do Velero cobrindo servidor em réplica única, cliente CLI, file-system backup, data mover CSI, provider plugins e diretório design/.; consultado em 2026-10-03.
