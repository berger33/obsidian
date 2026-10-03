---
id: software.devops.tranche05.000453
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

# Provisionamento do recurso Kafka, condição Ready e conexão via serviço my-cluster-kafka-bootstrap:9092

## Em uma frase
Para criar um cluster Apache Kafka após o operador estar em execução, aplica-se um recurso customizado `Kafka` (por exemplo, `kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-single-node.yaml -n kafka`) e aguarda-se a convergência com **`kubectl wait kafka/my-cluster --for=condition=Ready --timeout=300s -n kafka`**. Uma vez pronto, o Strimzi expõe automaticamente o serviço interno de descoberta **`<cluster-name>-kafka-bootstrap:9092`** (`my-cluster-kafka-bootstrap:9092`), pelo qual produtores (`kafka-console-producer.sh`) e consumidores (`kafka-console-consumer.sh`) conectam-se ao cluster dentro do Kubernetes.

## Por que importa
Em vez de acoplar clientes aos nomes ou IPs individuais de pods de brokers específicos (que podem mudar ou escalar), apontar todas as aplicações internas para o serviço `<cluster>-kafka-bootstrap:9092` garante descoberta resiliente dos metadados da topologia Kafka.

## Como funciona
Em pipelines de integração ou scripts de inicialização, utilize `kubectl wait kafka/<nome> --for=condition=Ready --timeout=300s` antes de iniciar aplicações produtoras e consumidoras apontadas para `<nome>-kafka-bootstrap:9092`.

## Exemplo
Para validar o cluster recém-criado `my-cluster`, o engenheiro executa `kafka-console-producer.sh --bootstrap-server my-cluster-kafka-bootstrap:9092 --topic my-topic`, envia `Hello Strimzi!` e lê a mensagem desde o início (`--from-beginning`) com `kafka-console-consumer.sh`.

## Limites e trade-offs
Como observa o Quickstart oficial, o comando `kubectl wait ... --timeout=300s` pode expirar na primeira execução se as imagens de contêiner estiverem sendo baixadas por uma conexão lenta; nesse caso, basta reexecutar o `kubectl wait` até o término do pull.

## Como verificar
Execute o par `kafka-console-producer.sh` e `kafka-console-consumer.sh` contra `my-cluster-kafka-bootstrap:9092` e confirme a entrega e leitura da mensagem de teste.

## Conexões
- [[strimzi-namespace-binding-in-install-manifests-and-rbac]] — Veja também: Alinhamento obrigatório de namespace em ClusterRoles e ClusterRoleBindings na instalação do Strimzi.
- [[strimzi-pvc-cleanup-requirement-on-cluster-deletion]] — Veja também: Exclusão explícita de PersistentVolumeClaims (PVCs) ao remover e recriar clusters Kafka no Strimzi.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
