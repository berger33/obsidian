---
id: software.devops.tranche04.000305
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
fontes: ["https://raw.githubusercontent.com/rook/rook/master/README.md", "https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/", "https://github.com/rook/rook"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Manifestos de cluster Rook para bare-metal (cluster.yaml), nuvem dinâmica (cluster-on-pvc.yaml) e teste (cluster-test.yaml)

## Em uma frase
A documentação oficial do Rook diferencia três manifestos principais de exemplo para criação do recurso `CephCluster`: `cluster.yaml`, voltado a clusters de produção em bare-metal e que exige no mínimo três nós trabalhadores; `cluster-on-pvc.yaml`, projetado para clusters de produção em ambientes de nuvem dinâmica onde os daemons consomem volumes persistentes provisionados dinamicamente; e `cluster-test.yaml`, calibrado para ambientes de laboratório de nó único como Minikube. Além disso, para que o cluster sobreviva a reinicializações dos hosts, a propriedade `dataDirHostPath` deve apontar para um caminho persistente válido nos nós.

## Por que importa
Usar configurações de teste (`cluster-test.yaml`, sem redundância entre três nós) em produção compromete a durabilidade e o quórum dos monitores Ceph, enquanto tentar aplicar `cluster.yaml` padrão em um Minikube de nó único impede a formação de quórum de três monitores e três OSDs distintos.

## Como funciona
Escolha `cluster.yaml` para bare-metal com no mínimo 3 worker nodes, `cluster-on-pvc.yaml` para provedores cloud elásticos com StorageClasses de bloco, ou o Helm Chart `rook-ceph-cluster` equivalente, verificando sempre que `dataDirHostPath` (por padrão `/var/lib/rook`) reside em disco persistente do host.

## Exemplo
Em uma nuvem pública onde os nós trabalhadores usam discos de boot efêmeros, a arquitetura adota `cluster-on-pvc.yaml` para alocar volumes de bloco dedicados aos monitores e OSDs do Ceph, garantindo sobrevivência a substituições de instância.

## Limites e trade-offs
Nunca deixe `dataDirHostPath` apontando para um diretório em memória (`tmpfs`) ou partição volátil que seja limpa no reboot do nó, pois a perda dos metadados locais dos monitores no host corrompe a identidade do cluster após reinicialização.

## Como verificar
Inspecione a especificação do recurso `CephCluster` (`kubectl -n rook-ceph get cephcluster -o yaml`) confirmando o perfil adequado ao ambiente, a contagem de monitores e o valor persistente de `dataDirHostPath`.

## Conexões
- [[rook-operator-deployment-crds-common-and-csi-operator]] — Veja também: Implantação do Rook Operator com crds.yaml, common.yaml, csi-operator.yaml e operator.yaml.
- [[rook-mon-mgr-osd-and-csi-pods-architecture]] — Veja também: Arquitetura de pods mon, mgr, osd e plugins CSI no namespace rook-ceph.

## Fontes
- [Rook GitHub — README.md (CNCF Graduated, Ceph Provider Stable, Official Releases)](https://raw.githubusercontent.com/rook/rook/master/README.md) — README oficial do Rook detalhando orquestração cloud-native do Ceph para file, block e object storage no Kubernetes, status Stable do provedor Ceph, graduação na CNCF e recomendação de usar releases oficiais em vez da branch master.; consultado em 2026-10-03.
- [Rook Documentation — Quickstart (Prerequisites, Operator, CephCluster, Toolbox)](https://rook.github.io/docs/rook/latest-release/Getting-Started/quickstart/) — Guia oficial de início rápido do Rook cobrindo versões suportadas do Kubernetes v1.31 a v1.37, arquiteturas amd64 e arm64, pré-requisitos de dispositivos brutos/LVM/PVs em modo block, manifests crds.yaml/common.yaml/csi-operator.yaml/operator.yaml/cluster.yaml e verificação via ceph status no toolbox.; consultado em 2026-10-03.
- [Rook — Official GitHub Repository](https://github.com/rook/rook) — Repositório principal Apache-2.0 do Rook com operador Ceph, CRDs, exemplos de implantação e charts Helm.; consultado em 2026-10-03.
