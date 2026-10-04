---
id: software.devops.tranche05.000451
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md", "https://strimzi.io/quickstarts/", "https://github.com/strimzi/strimzi-kafka-operator"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Strimzi como operador declarativo de Apache Kafka no Kubernetes e OpenShift

## Em uma frase
O Strimzi (`strimzi.io`), licenciado sob Apache-2.0, fornece uma maneira nativa e declarativa de executar clusters **Apache Kafka** no **Kubernetes** e no **OpenShift** em diversas configurações de implantação. Em vez de administrar brokers, certificados TLS, configurações de segurança e tópicos manualmente, o Strimzi instala Custom Resource Definitions (**CRDs** — como `Kafka`, `KafkaTopic`, `KafkaUser`, `KafkaConnect`) e o **Strimzi Cluster Operator** (`deployment/strimzi-cluster-operator`), que observa continuamente esses recursos customizados e reconcilia pods, serviços, volumes persistentes e configurações do cluster Kafka.

## Por que importa
Operar um sistema distribuído de streaming de eventos como o Apache Kafka no Kubernetes sem um operador especializado exige gerenciar manualmente identidades de brokers, upgrades rolantes seguros, listeners internos/externos e rebalanceamento. O Strimzi transforma toda a topologia do Kafka em recursos declarativos nativos da API do Kubernetes.

## Como funciona
Implante o Strimzi Cluster Operator (via manifestos oficiais, Helm Chart ou OperatorHub no OpenShift) para provisionar e administrar clusters Apache Kafka, tópicos e usuários inteiramente via GitOps.

## Exemplo
Uma plataforma de eventos corporativa declara um recurso `kind: Kafka` chamado `my-cluster` e dezenas de recursos `kind: KafkaTopic` versionados em Git; o Strimzi Cluster Operator cria e mantém os brokers, serviços de bootstrap e tópicos sincronizados.

## Limites e trade-offs
Ao dimensionar ambientes locais de teste (como Minikube ou Docker para Kind), siga a recomendação explícita do Quickstart oficial: aloque no mínimo **4 GB de memória RAM** (`minikube start --memory=4096` e pelo menos 2 CPUs), pois o padrão de 2 GB é insuficiente para o Kubernetes somado ao operador e aos brokers Kafka.

## Como verificar
Monitore a implantação do operador com `kubectl get pod -n kafka --watch` e acompanhe seus logs com `kubectl logs deployment/strimzi-cluster-operator -n kafka -f`.

## Conexões
- [[strimzi-namespace-binding-in-install-manifests-and-rbac]] — Veja também: Alinhamento obrigatório de namespace em ClusterRoles e ClusterRoleBindings na instalação do Strimzi.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
