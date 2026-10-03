---
id: software.devops.tranche05.000458
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

# Gerenciamento declarativo de tópicos e usuários com CRDs KafkaTopic e KafkaUser no Strimzi

## Em uma frase
Além do recurso principal `Kafka` que gerencia os brokers, o Quickstart oficial destaca que os CRDs instalados pelo Strimzi definem os esquemas para recursos customizados como **`KafkaTopic`** e **`KafkaUser`**, observados pelo operador para criar e configurar tópicos (partições, fator de replicação, retenção, compactação) e usuários (credenciais SCRAM-SHA-512 ou certificados clientes TLS mTLS e listas de controle de acesso ACLs) diretamente pela API do Kubernetes.

## Por que importa
Criar tópicos manualmente via scripts `kafka-topics.sh` ou habilitar `auto.create.topics.enable` em produção leva a tópicos com número incorreto de partições, fator de replicação 1 e ausência de rastreabilidade no Git. Declarar `KafkaTopic` e `KafkaUser` em YAML submete cada tópico e permissão de acesso ao mesmo fluxo de code review e GitOps das aplicações.

## Como funciona
Desabilite a criação automática de tópicos em clusters produtivos e gerencie todos os tópicos e credenciais de clientes por meio de manifestos `KafkaTopic` e `KafkaUser` reconciliados pelo Entity Operator do Strimzi.

## Exemplo
Quando um novo microsserviço precisa publicar eventos em um tópico particionado com autenticação mTLS, o pull request inclui um `KafkaTopic` com 12 partições e `replicas: 3` e um `KafkaUser` que gera automaticamente o `Secret` Kubernetes com os certificados do cliente.

## Limites e trade-offs
Ao remover todos os recursos do Strimzi de um namespace com `kubectl get strimzi -o name`, lembre-se de que a categoria agregada `strimzi` inclui também os recursos `KafkaTopic` e `KafkaUser` daquele namespace.

## Como verificar
Crie um manifesto `KafkaTopic` de teste, aplique no namespace do cluster e confirme `READY True` em `kubectl get kafkatopics -n kafka`.

## Conexões
- [[strimzi-minikube-versus-kubernetes-kind-local-tradeoffs]] — Veja também: Diferenças operacionais entre Minikube e Kubernetes Kind para clusters locais do Strimzi.
- [[strimzi-development-testing-and-release-guides-workflow]] — Veja também: Fluxo de build, guia de testes (TESTING.md) e checklist de release no repositório do Strimzi.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
