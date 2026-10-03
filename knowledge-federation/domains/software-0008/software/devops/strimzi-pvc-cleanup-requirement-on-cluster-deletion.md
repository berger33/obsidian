---
id: software.devops.tranche05.000454
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

# Exclusão explícita de PersistentVolumeClaims (PVCs) ao remover e recriar clusters Kafka no Strimzi

## Em uma frase
A seção *Deleting your Apache Kafka cluster* do Quickstart oficial documenta um comportamento operacional essencial: executar `kubectl -n kafka delete $(kubectl get strimzi -o name -n kafka)` remove todos os recursos customizados do Strimzi (incluindo o cluster `Kafka` e os `KafkaTopics`) mantendo o operador ativo, mas **não remove automaticamente os PersistentVolumeClaims (PVCs)** utilizados pelos brokers (por segurança contra perda acidental de dados). Por isso, para limpar completamente o armazenamento é necessário executar explicitamente **`kubectl delete pvc -l strimzi.io/name=my-cluster-kafka -n kafka`**.

## Por que importa
O Quickstart oficial alerta diretamente sobre a consequência de esquecer esse passo: **sem deletar o PVC residual, o próximo cluster Kafka que você tentar iniciar com o mesmo nome falhará**, pois tentará reutilizar o volume que pertencia ao cluster Apache Kafka anterior (cujo `cluster.id` e metadados em disco conflitam com a nova instância).

## Como funciona
Em ambientes de teste, homologação ou descomissionamento onde um cluster Kafka é deletado e posteriormente recriado do zero com o mesmo nome, remova sempre os PVCs associados com `kubectl delete pvc -l strimzi.io/name=<cluster>-kafka -n <namespace>`.

## Exemplo
Em um ambiente de CI efêmero que recriava o cluster `my-cluster` a cada bateria de testes sem apagar o namespace, o segundo teste falhava na subida do broker; adicionar `kubectl delete pvc -l strimzi.io/name=my-cluster-kafka -n kafka` ao teardown resolveu definitivamente o conflito de metadados de disco.

## Limites e trade-offs
Em clusters de produção, essa preservação padrão dos PVCs (`deleteClaim: false`) é uma proteção intencional contra exclusão acidental do CR `Kafka`; nunca habilite exclusão automática de PVCs em produção sem backup externo validado dos dados críticos.

## Como verificar
Após deletar um cluster de teste e executar `kubectl delete pvc -l strimzi.io/name=my-cluster-kafka -n kafka`, verifique com `kubectl get pvc -n kafka` que nenhum volume órfão permaneceu antes de recriar o cluster.

## Conexões
- [[strimzi-kafka-custom-resource-and-bootstrap-service]] — Veja também: Provisionamento do recurso Kafka, condição Ready e conexão via serviço my-cluster-kafka-bootstrap:9092.
- [[strimzi-cosign-keyless-container-signature-verification]] — Veja também: Verificação de assinaturas de imagens do Strimzi com Cosign (keyless desde a versão 0.49.0).

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
