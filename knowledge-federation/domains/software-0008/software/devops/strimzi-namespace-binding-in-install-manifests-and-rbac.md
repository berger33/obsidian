---
id: software.devops.tranche05.000452
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

# Alinhamento obrigatório de namespace em ClusterRoles e ClusterRoleBindings na instalação do Strimzi

## Em uma frase
O guia oficial `strimzi.io/quickstarts/` destaca um detalhe crítico ao instalar o Strimzi Cluster Operator a partir dos manifestos de instalação (`kubectl create -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka`): os arquivos YAML brutos de `ClusterRoles` e `ClusterRoleBindings` baixados de `strimzi.io` contêm por padrão o namespace `myproject`; o parâmetro de query **`?namespace=kafka`** atualiza esses arquivos em tempo real para referenciar o namespace `kafka`, enquanto a flag **`-n kafka`** no `kubectl create` garante que as definições sem namespace fixo também sejam instaladas em `kafka`.

## Por que importa
Conforme alerta a documentação oficial, **se houver divergência entre o namespace configurado nos `ClusterRoleBindings` e o namespace onde o pod do operador foi criado, o Strimzi Cluster Operator não terá as permissões RBAC necessárias para executar suas operações** e falhará ao tentar observar ou criar recursos do Kafka.

## Como funciona
Ao instalar o Strimzi no namespace `<meu-ns>`, passe sempre o mesmo nome tanto no parâmetro `?namespace=<meu-ns>` (ou substitua `myproject` via `sed`/Kustomize nos manifestos locais) quanto na flag `-n <meu-ns>` do `kubectl`.

## Exemplo
Durante um deploy em um namespace chamado `streaming`, o operador falhava com erros `Forbidden` nos logs porque o manifesto havia sido aplicado sem atualizar as referências padrão `myproject` nos `ClusterRoleBindings`; após alinhar o namespace nos bindings, a reconciliação inicia imediatamente.

## Limites e trade-offs
Verifique sempre os logs de inicialização de `deployment/strimzi-cluster-operator` após a instalação para confirmar que nenhuma exceção de permissão RBAC (`403 Forbidden`) foi emitida ao listar CRDs.

## Como verificar
Execute `kubectl auth can-i --as=system:serviceaccount:kafka:strimzi-cluster-operator get kafkas.kafka.strimzi.io -n kafka` e confirme o retorno `yes`.

## Conexões
- [[strimzi-apache-kafka-operator-for-kubernetes-and-openshift]] — Veja também: Strimzi como operador declarativo de Apache Kafka no Kubernetes e OpenShift.
- [[strimzi-kafka-custom-resource-and-bootstrap-service]] — Veja também: Provisionamento do recurso Kafka, condição Ready e conexão via serviço my-cluster-kafka-bootstrap:9092.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
