---
id: software.devops.tranche05.000459
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

# Fluxo de build, guia de testes (TESTING.md) e checklist de release no repositório do Strimzi

## Em uma frase
A seção *Contributing* do README oficial do Strimzi estrutura a documentação interna de engenharia do operador em quatro guias fundamentais: o **Development Guide** (`development-docs/DEV_GUIDE.md`), que descreve como configurar rapidamente o ambiente para compilar o Strimzi do código-fonte; o **Test Guide** (`development-docs/TESTING.md`), leitura obrigatória para compreender como executar testes unitários e de sistema antes de submeter qualquer patch; o **Release Checklist** (`development-docs/RELEASE.md`); e o **Documentation Contributor Guide** (`strimzi.io/contributing/guide/`), além de marcar issues ideais para novos contribuidores com a label `good-start`.

## Por que importa
Um operador que gerencia armazenamento distribuído stateful como o Apache Kafka depende de uma bateria rigorosa de testes de unidade e testes de sistema para garantir que reconciliações de configuração não causem perda de quórum ou indisponibilidade de partições.

## Como funciona
Consulte `development-docs/DEV_GUIDE.md` e `development-docs/TESTING.md` ao compilar ou testar customizações do Strimzi e esclareça dúvidas arquiteturais nos canais oficiais `#strimzi` e `#strimzi-dev` no Slack da CNCF ou nas listas de discussão `cncf-strimzi-users` e `cncf-strimzi-dev`.

## Exemplo
Um engenheiro que deseja contribuir com uma melhoria no operador começa filtrando issues com a label `good-start`, configura o ambiente local seguindo `development-docs/DEV_GUIDE.md` e executa a suíte descrita em `development-docs/TESTING.md`.

## Limites e trade-offs
Observe a nota explícita no README sobre testes comunitários em arquiteturas específicas: o badge de CI para **Linux on IBM Z (`s390x`)** representa uma iniciativa conduzida pela comunidade e não é oficialmente endossado pelos mantenedores do projeto Strimzi.

## Como verificar
Verifique a execução dos testes locais conforme `development-docs/TESTING.md` antes de abrir qualquer Pull Request no repositório `strimzi/strimzi-kafka-operator`.

## Conexões
- [[strimzi-kafka-topics-and-users-declarative-management]] — Veja também: Gerenciamento declarativo de tópicos e usuários com CRDs KafkaTopic e KafkaUser no Strimzi.
- [[strimzi-dco-sign-off-and-cncf-community-meetings]] — Veja também: Conformidade DCO (git commit -s / git commit --amend -s) e reuniões comunitárias do Strimzi.

## Fontes
- [Strimzi GitHub — README.md (Apache Kafka on Kubernetes/OpenShift, Cosign Keyless Signatures, SBOM & DCO)](https://raw.githubusercontent.com/strimzi/strimzi-kafka-operator/main/README.md) — README oficial do Strimzi (Apache-2.0) detalhando operação de Apache Kafka no Kubernetes e OpenShift, assinatura de contêineres com Cosign (a partir da 0.38.0 e keyless desde a 0.49.0), publicação e verificação de SBOM em SPDX-JSON e Syft-Table, guias de desenvolvimento/teste e exigência de DCO Signed-off-by.; consultado em 2026-10-03.
- [Strimzi Official Documentation — Quick Starts (CRDs, Namespace Matching, Producer/Consumer & PVC Cleanup)](https://strimzi.io/quickstarts/) — Guia oficial de início rápido do Strimzi detalhando instalação do Cluster Operator com strimzi.io/install/latest?namespace=kafka, CRDs Kafka e KafkaTopic, envio e consumo de mensagens via my-cluster-kafka-bootstrap:9092 e obrigatoriedade de deletar PVCs residuais ao recriar clusters.; consultado em 2026-10-03.
- [Strimzi — Official GitHub Repository](https://github.com/strimzi/strimzi-kafka-operator) — Repositório oficial Apache-2.0 do Strimzi Kafka Operator.; consultado em 2026-10-03.
